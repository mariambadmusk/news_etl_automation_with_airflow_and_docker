# News ETL Project

## Project Overview
The News ETL Project streamlines the local automatation process of extracting, transforming, and loading news data into a structured database. By using Apache Airflow, Docker, and Postgres, this project ensures a seamless and efficient workflow for managing news articles. 

*** The same project can be found in [this repository](https://github.com/mariambadmusk/aws_driven_news_aggregation_and_sentiment_data_pipeline); however, it employs AWS cloud services for enhanced scalability and high availability.


### Prerequisites
- Docker Desktop installed on your machine.
- A Linux environment.

## Features
- **Data Extraction**: Fetch news articles from NewsDataApi.
- **Data Transformation**: Clean and normalise the data.
- **Data Loading**: Store the transformed data into a Postgres database.
- **Data Persistence**: Ensure data remains in Postgres, managed through Docker containers.


### Setup
1. Build and start the Docker containers:
    ```bash
    docker-compose up -d --build
    ```

2. Access the Airflow web interface:
    - Open your browser and navigate to `http://localhost:8080`.
    - Use the default credentials (username: `airflow`, password: `airflow`).

### Configuration
Update the `docker-compose.yaml` file with your specific settings:
- **Airflow**: Configuration for the Airflow service.
- **Postgres**: Database connection details for the Postgres service.
- **PgAdmin**: Configuration for the PgAdmin service.

### Environment Variables
Use a `.env` file to configure environment settings for Postgres and PgAdmin. Here is an example of the `.env` file:
```env
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin

NEWSDATA_API_KEY =

```

### Additional Information
- The Docker image can be found at the following URL: [Docker Hub](https://hub.docker.com/).
- Ensure that the `requirements.txt` file is up-to-date with all necessary dependencies to ensure compatibility with the Apache Airflow image.



## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/news_etl.git
    ```
2. Navigate to the project directory:
    ```bash
    cd news_etl
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
     ```


### Note on Image Size
The Docker image size is relatively large due to the inclusion of the `torch` package. Without `torch`, the image size is less than 2GB. 


