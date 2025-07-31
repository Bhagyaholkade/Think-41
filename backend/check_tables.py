import psycopg2

try:
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()

    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("No tables found.")

    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)
