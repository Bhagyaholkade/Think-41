import sqlite3

def check_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)
    
    # Check departments schema
    try:
        cursor.execute("PRAGMA table_info(departments)")
        print("Departments schema:", cursor.fetchall())
    except sqlite3.OperationalError:
        print("Departments table doesn't exist")
    
    conn.close()

if __name__ == "__main__":
    check_database()