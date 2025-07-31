import sqlite3

def initialize_database():
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Create departments table (with IF NOT EXISTS)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        ''')
        
        # Insert sample departments
        departments = [
            ("Electronics",),
            ("Computers",),
            ("Accessories",),
            ("Office",),
            ("Home",)
        ]
        cursor.executemany('INSERT OR IGNORE INTO departments (name) VALUES (?)', departments)
        
        # Create products table with proper foreign key syntax
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id)
        );
        ''')
        
        # Insert sample products
        products = [
            ("Laptop", "High performance laptop", 75000, 2),
            ("Smartphone", "Latest model smartphone", 35000, 1),
            ("Headphones", "Noise-cancelling headphones", 5000, 3),
            ("Keyboard", "Mechanical RGB keyboard", 2500, 2),
            ("Monitor", "24-inch HD monitor", 12000, 2),
        ]
        cursor.executemany('''
            INSERT INTO products (name, description, price, department_id)
            VALUES (?, ?, ?, ?)
        ''', products)
        
        conn.commit()
        print("✅ Database initialized successfully!")
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_database()