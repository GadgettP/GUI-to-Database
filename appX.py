import psycopg2

# Set up a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=""
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM account")

# Fetch the results of the query
results = cur.fetchall()

for row in results:
    print(row)


# Close the cursor and connection
cur.close()
conn.close()