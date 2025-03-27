from snowflake.snowpark import Session

# Snowflake connection parameters
connection_parameters = {
    "account": "TBTEQCX-BIB18624",
    "user": "MAR2025",
    "password": "Pune@1234567",
    "warehouse": "COMPUTE_WH",
    "database": "INTERVIEW",
    "schema": "QUESTIONS",
}

# Create a Snowflake session
session = Session.builder.configs(connection_parameters).create()

# Call the stored procedure
result = session.sql("CALL increment_counter();").collect()

# Print the result
print("Counter Value:", result[0][0])

# Close the session
session.close()
