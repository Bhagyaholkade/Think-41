import zipfile
import os
import csv
import sqlite3

ZIP_NAME = "ecommerce-dataset-main copy.zip"
EXTRACTED_FOLDER = "extracted_data"
INNER_ZIP = os.path.join(EXTRACTED_FOLDER, "ecommerce-dataset-main", "archive.zip")
INNER_FOLDER = os.path.join(EXTRACTED_FOLDER, "archive")
CSV_FILE = os.path.join(INNER_FOLDER, "products.csv")

# Step 1: Extract outer zip
if not os.path.exists(EXTRACTED_FOLDER):
    os.makedirs(EXTRACTED_FOLDER)

print(f"📦 Extracting: {ZIP_NAME}")
with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
    zip_ref.extractall(EXTRACTED_FOLDER)

# Step 2: Extract inner zip (archive.zip)
print(f"📦 Extracting nested: ecommerce-dataset-main/archive.zip")
with zipfile.ZipFile(INNER_ZIP, 'r') as zip_ref:
    zip_ref.extractall(INNER_FOLDER)

# Step 3: Read products.csv
if not os.path.exists(CSV_FILE):
    print("❌ 'products.csv' not found in extracted archive.")
    exit()

print("📄 Found products.csv, inserting into database...")

# Step 4: Read and map columns
with open(CSV_FILE, 'r', encoding='utf-8') as file:
    dr = csv.DictReader(file)
    headers = dr.fieldnames

    print(f"📋 Available columns in CSV: {headers}")

    # Try to map known possible alternatives
    def guess_column(name, options):
        for opt in options:
            if opt in headers:
                return opt
        return None

    col_id = guess_column('id', ['id', 'product_id'])
    col_name = guess_column('name', ['name', 'product_name'])
    col_category = guess_column('category', ['category', 'product_category'])
    col_price = guess_column('price', ['price', 'retail_price'])

    if not all([col_id, col_name, col_category, col_price]):
        print("❌ Could not automatically map required columns.")
        exit()

    rows = [(row[col_id], row[col_name], row[col_category], row[col_price]) for row in dr]

# Step 5: Insert into SQLite database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Ensure table exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL
    )
''')

# Insert rows
cursor.executemany("INSERT OR IGNORE INTO products (id, name, category, price) VALUES (?, ?, ?, ?)", rows)

conn.commit()
conn.close()

print(f"✅ Inserted {len(rows)} products into database.")
