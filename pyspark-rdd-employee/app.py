from pyspark import SparkContext

sc = SparkContext("local[*]", "EmployeeRDD")

# Read CSV
rdd = sc.textFile("data/employees.csv")

header = rdd.first()

employees = (
    rdd.filter(lambda x: x != header)
       .map(lambda x: x.split(","))
)

# --------------------------------------
# Sort employees by salary (Descending)
# --------------------------------------

sorted_salary = employees.sortBy(lambda x: int(x[3]), ascending=False)

print("\n========== Employees Sorted by Salary ==========\n")

for emp in sorted_salary.collect():
    print(emp)

# --------------------------------------
# Total salary department-wise
# --------------------------------------

dept_salary = (
    employees
    .map(lambda x: (x[2], int(x[3])))
    .reduceByKey(lambda a, b: a + b)
)

print("\n========== Department Salary ==========\n")

for dept in dept_salary.collect():
    print(f"{dept[0]} : {dept[1]}")

# --------------------------------------
# Top 3 highest-paid employees
# --------------------------------------

top3 = sorted_salary.take(3)

output = sc.parallelize([
    ",".join(emp) for emp in top3
])

output.saveAsTextFile("output/top3_highest_paid")

print("\nTop 3 employees saved successfully!")

sc.stop()