# Importing necessary libraries
# Importing sys for accessing command-line arguments
# Importing SparkConf, SparkContext, and SQLContext for configuring and working with Spark
# Importing RandomForestModel for loading a pre-trained random forest model
# Importing LabeledPoint for representing labeled data points in Spark MLlib
# Importing Vectors for working with vector data structures in Spark MLlib
# Importing MulticlassMetrics for evaluating multiclass classification results
import sys
from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.tree import RandomForestModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.evaluation import MulticlassMetrics

# Configuring Spark application
configur = (SparkConf().setAppName("Wine-Quality-Prediction"))
spark_c = SparkContext("local", conf=configur)
spark_c.setLogLevel("ERROR")
sqlContext = SQLContext(spark_c)

# Checking if a command line argument is provided
if len(sys.argv) == 2:
    testFile = sys.argv[1]
# Read trained model from an S3 bucket
print("\n \n Trained Model is being read \n \n")
model = RandomForestModel.load(spark_c, "s3://pa2-wine/wine-pred.model/")
print(model)

# Reading the test dataset (ValidationDataset.csv) from an S3 bucket
# Converting the DataFrame into an RDD of LabeledPoints
wine_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://pa2-wine/ValidationDataset.csv')
wine_OutputDF = wine_df.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))
# Making predictions using the trained model on the test data
quality_pred = model.predict(wine_OutputDF.map(lambda x: x.features))
quality_label_pred = wine_OutputDF.map(lambda lp: lp.label).zip(quality_pred)
# Computing metrics using MulticlassMetrics
metrics = MulticlassMetrics(quality_label_pred)

# Printing overall statistics for the wine quality prediction
print("\n\n------Wine Quality Prediction Statistics-------")
print("Weighted precision = %s" % metrics.weightedPrecision)
print("Weighted F(1) Score = %s" % metrics.weightedFMeasure())
