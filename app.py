from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# New route for departments
@app.route("/api/departments", methods=["GET"])
def get_departments():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM departments')
    departments = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in departments])

# Updated products route with department info
@app.route("/api/products", methods=["GET"])
def get_products():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    conn = get_db_connection()
    cursor = conn.execute('''
        SELECT p.*, d.name as department_name 
        FROM products p
        LEFT JOIN departments d ON p.department_id = d.id
        LIMIT ? OFFSET ?
    ''', (limit, offset))
    products = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])

# Updated product detail route with department info
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    conn = get_db_connection()
    product = conn.execute('''
        SELECT p.*, d.name as department_name 
        FROM products p
        LEFT JOIN departments d ON p.department_id = d.id
        WHERE p.id = ?
    ''', (product_id,)).fetchone()
    conn.close()

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(dict(product))

# New route to get products by department
@app.route("/api/departments/<int:dept_id>/products", methods=["GET"])
def get_products_by_department(dept_id):
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    conn = get_db_connection()
    cursor = conn.execute('''
        SELECT p.*, d.name as department_name 
        FROM products p
        JOIN departments d ON p.department_id = d.id
        WHERE d.id = ?
        LIMIT ? OFFSET ?
    ''', (dept_id, limit, offset))
    products = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])

@app.route("/")
def home():
    return "✅ Flask API is running. Endpoints: /api/products, /api/departments"

if __name__ == "__main__":
    app.run(debug=True)