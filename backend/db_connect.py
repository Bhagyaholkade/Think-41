import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="your_db_name",      # Replace with your DB name
        user="your_username",         # Replace with your DB user
        password="your_password",     # Replace with your password
        port=5432
    )
