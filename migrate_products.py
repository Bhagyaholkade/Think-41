import sqlite3

def migrate():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Add department_id column if it doesn't exist
    cursor.execute("PRAGMA table_info(products)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'department_id' not in columns:
        cursor.execute("ALTER TABLE products ADD COLUMN department_id INTEGER")
        print("Added department_id column to products table")
        
        # Set default department (e.g., Electronics)
        cursor.execute("UPDATE products SET department_id = 1 WHERE department_id IS NULL")
        print("Set default department for existing products")
    
    # Add foreign key constraint
    cursor.execute("PRAGMA foreign_keys = ON")
    conn.commit()
    conn.close()
    print("Migration complete")

if __name__ == "__main__":
    migrate()