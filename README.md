# Project: Data Pipelines with Airflow:
## Project Introduction:
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

My role was to to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills.
## Prerequisites:
This project makes the folowing assumptions:
- Python 3 installed,Python 3 Libraries available are given below:
    - airflow .
    - datetime.
    - os.
- The data resides in S3.
- Apache Airflow is available.
- I created my own Redshift cluster but user will need to have his own Redshift cluster available on AWS.
-  Make sure to add following two Airflow connections:
    -   AWS credentials, named  `aws_credentials`
    -   Connection to Redshift, named  `redshift`
## Dataset:
For this project, we shall be working with two datasets that reside in S3. Here are the S3 links for each:

-   Song data:  `s3://udacity-dend/song_data`
-   Log data:  `s3://udacity-dend/log_data`
### Song Dataset

The first dataset is a subset of real data from the  [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json

```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
````
### Log Dataset

The second dataset consists of log files in JSON format generated by this  [event simulator](https://github.com/Interana/eventsim)  based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json

```

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

![](https://video.udacity-data.com/topher/2019/February/5c6c3ce5_log-data/log-data.png)

## Schema for Song Play Analysis

Using the song and log datasets, I created a star schema optimized for queries on song play analysis.This star schema has 1  _fact_  table (songplays), and 4  _dimension_  tables (users, songs, artists, time). 

[![](https://github.com/kenhanscombe/project-postgres/raw/master/sparkify_erd.png?raw=true)](https://github.com/kenhanscombe/project-postgres/blob/master/sparkify_erd.png?raw=true)

## Project Template:
Files used on the project:

Project has two directories named  `dags`  and  `plugins`. A create tables script and readme file are at root level:
- `create_tables.sql` Contains SQL queries for creating required tables
1. `dags`  directory contains:

	-   `etl_dag.py`: Defines main DAG, tasks and link the tasks in required order.

2. `plugins/operators`  directory contains:

	-   `stage_redshift.py`: Defines  `StageToRedshiftOperator`  to copy JSON data from S3 to staging tables in the Redshift via  `copy`  command.
	-   `load_dimension.py`: Defines  `LoadDimensionOperator`  to load a dimension table from staging table(s).
	-   `load_fact.py`: Defines  `LoadFactOperator`  to load fact table from staging table(s).
	-   `data_quality.py`: Defines  `DataQualityOperator`  to run data quality checks on all tables passed as parameter.
	-   `sql_queries.py`: Contains SQL queries for the ETL pipeline (provided in template).
## Repository Structure:
```
main
│   README.md                    # Project description   
|   dag.jpg                      # Pipeline DAG image
|	dag_tree.jpg                 # Pipeline DAG tree view
|   create_tables.sql            # CREATE TABLE SQL statements
│   
└───airflow                      # Airflow home
|   |               
│   └───dags                     
│   |   │ etl_dag.py  			 # DAG definition
|   |   |
|   └───plugins
│       │  
|       └───helpers
|       |   | sql_queries.py     # All sql queries needed
|       |
|       └───operators
|       |   | data_quality.py    # DataQualityOperator
|       |   | load_dimension.py  # LoadDimensionOperator
|       |   | load_fact.py       # LoadFactOperator
|       |   | stage_redshift.py  # StageToRedshiftOperator
```

## DAG:

## Code Usage

Copy the files in respective folders for your own Airflow installation and execute the DAG.
