# PySpark Partition Assignment

## Objective

This project demonstrates partition management in PySpark using a DataFrame generated with `spark.range()`.

## Requirements

- Docker

## Build Docker Image

```bash
docker build -t pyspark-partition-app .
```

## Run Docker Container

```bash
docker run --rm pyspark-partition-app
```

## Operations Performed

1. Generate a DataFrame with **5,000,000** records using `spark.range()`.
2. Display the initial number of partitions.
3. Increase the number of partitions to **12** using `repartition()`.
4. Reduce the number of partitions to **3** using `coalesce()`.
5. Display sample records.

## Expected Output

```text
Initial Partitions: 1

Partitions after repartition(12): 12

Partitions after coalesce(3): 3

+---+
| id|
+---+
|  0|
|  1|
|  2|
|  3|
|  4|
|  5|
|  6|
|  7|
|  8|
|  9|
+---+
```