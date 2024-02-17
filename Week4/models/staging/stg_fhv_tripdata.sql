{{ config(materialied='view') }}

SELECT
*
from {{ source('staging', 'fhv_taxi_materialized_data') }}

-- {% if var('is_test_run', default=true) %}

-- limit 100

-- {% endif %}


