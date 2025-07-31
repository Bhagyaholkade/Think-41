from flask import Flask, jsonify, request
from flask_cors import CORS  # ✅ Import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS globally

# Establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # So we can return dictionary-like rows
    return conn

# Route: GET /api/products?limit=10&offset=0
@app.route("/api/products", methods=["GET"])
def get_products():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM products LIMIT ? OFFSET ?', (limit, offset))
    products = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])

# Route: GET /api/products/1
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(dict(product))

# Optional: Root route for clarity
@app.route("/")
def home():
    return "✅ Flask API is running. Use /api/products to access data."

# Main runner
if __name__ == "__main__":
    app.run(debug=True)
