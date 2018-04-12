## Passage-Capture Notes

- Download fresh set of passage / flow data for all dam sites 2010 - 2018
- Create job to load them into BigQuery
- Normalize

Example normalization query for species data: 

```
SELECT 
  PARSE_DATE("%m/%d/%Y", date) AS count_date,
  dam,
  ChinookAdult AS chinook_adult,
  ChinookJack AS chinook_jack,
  CohoAdult AS coho_adult,
  CohoJack AS coho_jack,
  Steelhead AS steelhead,
  WildSteelhead AS wild_steelhead,
  Sockeye AS sockeye,
  Pink AS pink,
  Chum AS chum,
  Lamprey AS lamprey,
  Shad As shad
FROM `passive-capture.passage_data.daily_counts`
ORDER BY count_date;
```

## Aggregate weather data from NOAA: https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt


## Example for snow data grouped by year month
```
SELECT
  CONCAT(
    CAST(EXTRACT(YEAR FROM date) AS STRING), 
    CAST(EXTRACT(MONTH FROM date) AS STRING)
  ) AS year_month,
  stations.name,
  stations.latitude,
  stations.longitude,
  weather.id,
  weather.element,
  SUM(weather.value) AS snow_total,
  AVG(DISTINCT weather.value) AS snow_average,
  MIN(weather.value) AS snow_min,
  MAX(weather.value) AS snow_max
FROM
  `bigquery-public-data.ghcn_d.ghcnd_stations` AS stations
  JOIN `bigquery-public-data.ghcn_d.ghcnd_201*` AS weather
  ON weather.id = stations.id
WHERE
  stations.latitude > 43
  AND stations.latitude < 49
  AND stations.longitude > -123
  AND stations.longitude < -120
  AND element = 'SNWD'
GROUP BY
  year_month,
  stations.name,
  stations.latitude,
  stations.longitude,
  weather.id,
  weather.element
ORDER BY
year_month
```

## Conversation with Martin


Use either ARIMA or Prophet for time series analysis on each time series data. Then use Multivariate Regression Analysis


## Prophet

capture time series data and log of one species at a time
replace nulls with 0's
replace -inf with 0

## Add holidays to Prophet data

http://www.fpc.org/documents/metadata/FPC_Adult_Metadata.html

These are the times we consider 'bonus'