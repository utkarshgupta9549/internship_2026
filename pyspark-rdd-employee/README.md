# PySpark Employee RDD Assignment

## Requirements

- Docker

---

## Build Docker Image

```bash
docker build -t employee-rdd .
```

---

## Run Container

```bash
docker run --rm employee-rdd
```

---

## Project Tasks

The application performs:

1. Read employee CSV into RDD
2. Sort employees by salary (Descending)
3. Calculate department-wise total salary
4. Save Top 3 highest-paid employees into output folder

---

## Dataset

```
id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000
```