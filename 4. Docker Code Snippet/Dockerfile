FROM openjdk:8-jre-slim
FROM datamechanics/spark:3.1-latest
ENV PYSPARK_MAJOR_PYTHON_VERSION=3

# Set the working directory
WORKDIR /DockerImages

# Install required Python packages
RUN pip install --upgrade pip \
    && pip install scikit-learn pandas pyspark findspark numpy

# Copy your files into the container
COPY TrainingDataset.csv .
COPY ValidationDataset.csv .
COPY predict_code.py .
COPY Training_Model.model .

# Define the entry point and command
CMD ["python", "training_code.py"]
ENTRYPOINT ["python", "prediction_code.py"]