# The Repo for all text magic things!!!

## GenV
Has the code for generating SQL queries and metabase cards based on natural languages using OpenAI GPT3

### Installation
```
poetry install
```

### Using the cli 
run `poetry run genV --help` for usage, Example:

```
poetry run genV get-full-results "show me the trends in number of claims categorized by vehicle make, model, and model year"

Question:
Trends in Claims by Vehicle Make, Model, and Year.

Query:
SELECT
    toStartOfYear(created_at) AS period_start,
    vehicle_make,
    vehicle_model,
    vehicle_model_year,
    COUNT(*) AS claim_count
FROM
    all__claim
    JOIN all__vehicle USING vin
WHERE
    vehicle_make IS NOT NULL AND
    vehicle_model IS NOT NULL AND
    vehicle_model_year IS NOT NULL AND
    tenant = 'gm'
GROUP BY
    period_start,
    vehicle_make,
    vehicle_model,
    vehicle_model_year
ORDER BY
    period_start,
    vehicle_make,
    vehicle_model,
    vehicle_model_year

Results:

|    | period_start        | vehicle_make   | vehicle_model   |   vehicle_model_year |   claim_count |
|---:|:--------------------|:---------------|:----------------|---------------------:|--------------:|
|  0 | 2023-01-01 00:00:00 | Buick          | Enclave C1      |                 2021 |        132830 |
|  1 | 2023-01-01 00:00:00 | Buick          | Enclave C1      |                 2022 |         62500 |
|  2 | 2023-01-01 00:00:00 | Chevrolet      | Blazer          |                 2021 |        297416 |
|  3 | 2023-01-01 00:00:00 | Chevrolet      | Blazer          |                 2022 |        196489 |
|  4 | 2023-01-01 00:00:00 | Chevrolet      | Colorado        |                 2021 |        303449 |
|  5 | 2023-01-01 00:00:00 | Chevrolet      | Colorado        |                 2022 |        279793 |
|  6 | 2023-01-01 00:00:00 | Chevrolet      | Traverse C1     |                 2021 |        359162 |
|  7 | 2023-01-01 00:00:00 | Chevrolet      | Traverse C1     |                 2022 |        190292 |
|  8 | 2023-01-01 00:00:00 | GMC            | Acadia C1       |                 2021 |        262862 |
|  9 | 2023-01-01 00:00:00 | GMC            | Acadia C1       |                 2022 |        124485 |

Metabase URL:
https://metabase.cluster-0.internal.viaduct.ai/question/2574-trends-in-claims-by-vehicle-make,-model,-and-year.
```
