# Importing necessary libraries and packages
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import col

# Configuring Spark application
configur = (SparkConf().setAppName("Wine-Quality-Prediction"))
spark_c = SparkContext("local", conf=configur)
spark_c.setLogLevel("ERROR")
sqlContext = SQLContext(spark_c)

# Reading the training dataset from an S3 bucket
dataFrame = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://pa2-wine/TrainingDataset.csv')
# Reading the validation dataset from an S3 bucket
validatedataFrame = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://pa2-wine/ValidationDataset.csv')

# Selecting columns up to the 11th one (excluding the 'quality' column)
WineDataFrame = dataFrame.select(dataFrame.columns[:11])
# Converting the DataFrame into an RDD of LabeledPoints
FrameOutput = dataFrame.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

# Training a Random Forest classifier
# Converting the validation DataFrame into an RDD of LabeledPoints
# Making predictions using the trained model on the validation data
training_model = RandomForest.trainClassifier(FrameOutput, numClasses=10, categoricalFeaturesInfo={}, numTrees=60, maxBins=32, maxDepth=4, seed=42)
ValidDF_Output = validatedataFrame.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))
predictions = training_model.predict(ValidDF_Output.map(lambda x: x.features))
labelsAndPredictions = ValidDF_Output.map(lambda lp: lp.label).zip(predictions)

#Computing metrics using MulticlassMetrics
wineMetrics = MulticlassMetrics(labelsAndPredictions)
#Creating a DataFrame from the RDD of predicted labels and actual labels
PredLabel_DF = labelsAndPredictions.toDF()
pred_label = labelsAndPredictions.toDF(["label", "Prediction"])
pred_label.show(truncate=False)
PredLabel_DFPandas = pred_label.toPandas()

# Calculating and printing F1 score
F1score = f1_score(PredLabel_DFPandas['label'], PredLabel_DFPandas['Prediction'], average='micro')
# Printing confusion matrix, classification report, and accuracy
print(confusion_matrix(PredLabel_DFPandas['label'], PredLabel_DFPandas['Prediction']))
print(classification_report(PredLabel_DFPandas['label'], PredLabel_DFPandas['Prediction']))
print("The f1 score is : ", F1score)
print("The Accuracy is : ", accuracy_score(PredLabel_DFPandas['label'], PredLabel_DFPandas['Prediction']))

# Saving the trained model to an S3 bucket
print("\n Model is Trained. Saving it in S3 Bucket under PA2-WINE")
training_model.save(spark_c, "s3://pa2-wine/wine-pred.model")
print("Model Saved successfully")