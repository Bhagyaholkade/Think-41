import sqlite3

# Connect to database (creates products.db if it doesn't exist)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create 'products' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL
)
''')

# Insert sample products
sample_products = [
    ("Laptop", "High performance laptop", 75000),
    ("Smartphone", "Latest model smartphone", 35000),
    ("Headphones", "Noise-cancelling headphones", 5000),
    ("Keyboard", "Mechanical RGB keyboard", 2500),
    ("Monitor", "24-inch HD monitor", 12000),
]

cursor.executemany('INSERT INTO products (name, description, price) VALUES (?, ?, ?)', sample_products)

conn.commit()
conn.close()

print("✅ Database initialized with sample data.")
