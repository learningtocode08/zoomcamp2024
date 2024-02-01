SELECT	
		count(*) as total_trips
-- 		cast(lpep_pickup_datetime as date) as pickup
FROM public.green_taxi_trips
where cast(lpep_pickup_datetime as date) = TO_DATE('20190918','YYYYMMDD')
and cast(lpep_dropoff_datetime as date) = TO_DATE('20190918','YYYYMMDD')
;

SELECT	
		cast(lpep_pickup_datetime as date) as pickup
		,cast(lpep_dropoff_datetime as date) as dropoff
		,count(*) as total_trips
FROM public.green_taxi_trips
group by 1,2
order by 1,2
;

SELECT
		cast(lpep_pickup_datetime as date) as pickup
		,sum(trip_distance) as trip_distance
from public.green_taxi_trips
group by 1 
order by 2 desc


SELECT	
	  b."Borough"
	  ,sum(a.total_amount) as total_amount
FROM green_taxi_trips a
LEFT JOIN zones b ON a."PULocationID" = b."LocationID"
LEFT JOIN zones c ON a."DOLocationID" = c."LocationID"
where cast(lpep_pickup_datetime as date) = TO_DATE('20190918','YYYYMMDD')
-- and b."Borough" != 'Unknown'
group by 1
order by 2 desc 
;

SELECT
	  b."Zone" as pickup_zone
	  ,c."Zone" as dropoff_zone
	  ,max(a.tip_amount) as highest_tip
FROM green_taxi_trips a
LEFT JOIN zones b ON a."PULocationID" = b."LocationID"
LEFT JOIN zones c ON a."DOLocationID" = c."LocationID"
where date_trunc('month',cast(a.lpep_pickup_datetime as date)) = TO_DATE('20190901','YYYYMMDD')
and b."Zone" = 'Astoria'
-- and b."Borough" != 'Unknown'
group by 1,2
order by 3 desc
;