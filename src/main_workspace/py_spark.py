from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# 1. Initialize Spark Session
spark = SparkSession.builder.appName("ExampleDataProcessing").getOrCreate()

# 2. Create Data (Using a PySpark DataFrame instead of SQLite)
data = [
    (1, "Alice", "Developer", 85000.00),
    (2, "Bob", "Designer", 65000.00),
    (3, "Nathan", "Student", -30000.00),
]
columns = ["id", "name", "position", "salary"]
employees_df = spark.createDataFrame(data, columns)

# Display initial data
print("Initial data:")
employees_df.show()

# 3. Update Record (for Alice, change salary to 90000)
employees_df = employees_df.withColumn(
    "salary", when(col("name") == "Alice", 90000.00).otherwise(col("salary"))
)

print("Updated data after Alice's salary adjustment:")
employees_df.show()

# 4. Delete Record (Remove entry for Bob)
employees_df = employees_df.filter(col("name") != "Bob")

print("Data after deleting Bob's record:")
employees_df.show()

# 5. Query 1: Find employees with salary > 80000
high_salary_employees = employees_df.filter(col("salary") > 80000)
print("Employees with salary greater than 80k:")
high_salary_employees.show()

# 6. Query 2: Count the number of employees
employee_count = employees_df.count()
print(f"Total number of employees: {employee_count}")

# Stop the Spark session
spark.stop()
