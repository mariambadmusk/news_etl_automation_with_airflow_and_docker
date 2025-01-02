# Use the Airflow base image
FROM apache/airflow:2.10.4

USER root

# Install dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH=$AIRFLOW_HOME
ENV PYTHON_VERSION=3.10.12

# Create necessary directories
WORKDIR $AIRFLOW_HOME

# Copy your requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

