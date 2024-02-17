{{ config(materialied='view') }}

SELECT *
from {{ source('staging', 'green_taxi_materialized_data') }}
limit 100
