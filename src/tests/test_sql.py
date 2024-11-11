from pyspark.sql import SparkSession


def test_spark():
    # Initialize the Spark session
    spark_session = SparkSession.builder.appName(
        "PySpark DataFrame Operations"
    ).getOrCreate()

    # Ensure Spark session is active
    assert spark_session is not None, "Spark session initialization failed"
    spark_session.stop()


def test_pyspark_operations():

    # 1. Initialize Spark Session
    spark = SparkSession.builder.appName("ExampleDataProcessing").getOrCreate()

    # Test 1: Create Data (Simulate table creation)
    data = [
        (1, "Alice", "Developer", 85000.00),
        (2, "Bob", "Designer", 65000.00),
        (3, "Nathan", "Student", -30000.00),
    ]
    columns = ["id", "name", "position", "salary"]

    # Create DataFrame
    employees_df = spark.createDataFrame(data, columns)

    # Verify DataFrame creation
    assert employees_df.count() == 3, "There should be 3 records in the DataFrame"

    # Test 2: Further operations on DataFrame (e.g., updates, filtering)
    employees_df = employees_df.withColumn(
        "salary", (employees_df["salary"] + 1000).cast("double")
    )
    updated_salaries = employees_df.select("name", "salary").collect()
    assert (
        updated_salaries[0].salary == 86000.0
    ), "Alice's salary should be updated to 86000.0"

    # Stop the Spark session
    print("ALL tests pass")
