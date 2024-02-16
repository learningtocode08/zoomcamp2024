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

CREATE OR REPLACE TABLE `ny_taxi.green_taxi_partitioned_table`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS 
SELECT * from `ny_taxi.green_taxi_materialized_data`;


SELECT distinct PULocationID
from `ny_taxi.green_taxi_materialized_data`
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30'

SELECT distinct PULocationID
from `ny_taxi.green_taxi_partitioned_table`
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30'