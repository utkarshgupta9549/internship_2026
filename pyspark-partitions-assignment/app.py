from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("PySpark Partition Assignment") \
    .getOrCreate()

# Create DataFrame with 5 million records
df = spark.range(5000000)

# Display initial number of partitions
print("Initial Partitions:", df.rdd.getNumPartitions())

# Increase partitions to 12
df_repartition = df.repartition(12)
print("Partitions after repartition(12):", df_repartition.rdd.getNumPartitions())

# Reduce partitions to 3
df_coalesce = df_repartition.coalesce(3)
print("Partitions after coalesce(3):", df_coalesce.rdd.getNumPartitions())

# Display sample records
df_coalesce.show(10)

spark.stop()