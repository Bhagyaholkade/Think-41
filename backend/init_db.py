# Updated with departments table and foreign key
import sqlite3

# Connect to database (creates products.db if it doesn't exist)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create 'departments' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

# Insert sample departments
sample_departments = [
    ("Electronics",),
    ("Computers",),
    ("Accessories",),
    ("Office",),
    ("Home",)
]

cursor.executemany('INSERT OR IGNORE INTO departments (name) VALUES (?)', sample_departments)

# Modify 'products' table to include department_id
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
''')

# Update sample products with department_ids
sample_products = [
    ("Laptop", "High performance laptop", 75000, 2),
    ("Smartphone", "Latest model smartphone", 35000, 1),
    ("Headphones", "Noise-cancelling headphones", 5000, 3),
    ("Keyboard", "Mechanical RGB keyboard", 2500, 2),
    ("Monitor", "24-inch HD monitor", 12000, 2),
]

cursor.execute('DELETE FROM products')  # Clear existing data
cursor.executemany('INSERT INTO products (name, description, price, department_id) VALUES (?, ?, ?, ?)', sample_products)

conn.commit()
conn.close()