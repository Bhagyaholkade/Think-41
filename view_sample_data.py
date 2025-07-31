import sqlite3

# Connect to your local database file
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Run a SELECT query to get 5 sample records from the products table
cursor.execute("SELECT * FROM products LIMIT 5;")
rows = cursor.fetchall()

# Print the sample rows
for row in rows:
    print(row)

conn.close()

