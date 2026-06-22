from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("Sales DataFrame Assignment") \
    .getOrCreate()

# Read CSV into DataFrame
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

# ----------------------------------------
# Sort products by sales (Descending)
# ----------------------------------------

print("\n========== Products Sorted by Sales ==========\n")

sorted_df = df.orderBy(col("sales").desc())

sorted_df.show()

# ----------------------------------------
# Top 3 highest-selling products
# ----------------------------------------

print("\n========== Top 3 Products ==========\n")

top3 = sorted_df.limit(3)

top3.show()

# ----------------------------------------
# Filter products with sales > 80000
# ----------------------------------------

filtered = df.filter(col("sales") > 80000)

filtered.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

print("Filtered products saved successfully!")

spark.stop()