CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.green_taxi_external_data`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://green-taxi-data/green_tripdata_2022*.parquet']
);

SELECT *
from green_taxi_external_data


CREATE OR REPLACE TABLE `ny_taxi.green_taxi_materialized_data` as 

SELECT *
from `ny_taxi.green_taxi_external_data`
;

SELECT count(*)
from `ny_taxi.green_taxi_materialized_data`;

SELECT distinct PULocationID
from `ny_taxi.green_taxi_materialized_data`;


SELECT count(*)
from `ny_taxi.green_taxi_materialized_data`
where fare_amount = 0.0