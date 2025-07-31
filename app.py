from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
    return conn

# -------------------------------
# Existing Product Endpoints
# -------------------------------
@app.route("/api/products", methods=["GET"])
def get_products():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    conn = get_db_connection()
    try:
        products = conn.execute('''
            SELECT p.*, d.name as department_name 
            FROM products p
            LEFT JOIN departments d ON p.department_id = d.id
            LIMIT ? OFFSET ?
        ''', (limit, offset)).fetchall()
        return jsonify([dict(row) for row in products])
    finally:
        conn.close()

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = get_db_connection()
    try:
        product = conn.execute('''
            SELECT p.*, d.name as department_name 
            FROM products p
            LEFT JOIN departments d ON p.department_id = d.id
            WHERE p.id = ?
        ''', (product_id,)).fetchone()
        
        if not product:
            return jsonify({"error": "Product not found"}), 404
            
        return jsonify(dict(product))
    finally:
        conn.close()

# -------------------------------
# New Department Endpoints
# -------------------------------
@app.route("/api/departments", methods=["GET"])
def get_all_departments():
    conn = get_db_connection()
    try:
        departments = conn.execute('''
            SELECT 
                d.id, 
                d.name, 
                COUNT(p.id) as product_count
            FROM departments d
            LEFT JOIN products p ON d.id = p.department_id
            GROUP BY d.id
            ORDER BY d.name
        ''').fetchall()
        return jsonify({"departments": [dict(dept) for dept in departments]})
    finally:
        conn.close()

@app.route("/api/departments/<int:dept_id>", methods=["GET"])
def get_department(dept_id):
    conn = get_db_connection()
    try:
        department = conn.execute('''
            SELECT 
                d.id, 
                d.name, 
                COUNT(p.id) as product_count
            FROM departments d
            LEFT JOIN products p ON d.id = p.department_id
            WHERE d.id = ?
            GROUP BY d.id
        ''', (dept_id,)).fetchone()
        
        if not department:
            return jsonify({"error": "Department not found"}), 404
            
        return jsonify(dict(department))
    finally:
        conn.close()

@app.route("/api/departments/<int:dept_id>/products", methods=["GET"])
def get_department_products(dept_id):
    conn = get_db_connection()
    try:
        # Verify department exists first
        dept = conn.execute(
            'SELECT name FROM departments WHERE id = ?', 
            (dept_id,)
        ).fetchone()
        
        if not dept:
            return jsonify({"error": "Department not found"}), 404

        # Get products if department exists
        products = conn.execute('''
            SELECT p.*, d.name as department_name
            FROM products p
            JOIN departments d ON p.department_id = d.id
            WHERE d.id = ?
            ORDER BY p.name
        ''', (dept_id,)).fetchall()
        
        return jsonify({
            "department": dept['name'],
            "products": [dict(product) for product in products]
        })
    finally:
        conn.close()

# -------------------------------
# Root Endpoint
# -------------------------------
@app.route("/")
def home():
    return """
    ✅ Flask API is running.<br><br>
    Available endpoints:<br>
    - /api/products<br>
    - /api/products/1<br>
    - /api/departments<br>
    - /api/departments/1<br>
    - /api/departments/1/products
    """

if __name__ == "__main__":
    app.run(debug=True)