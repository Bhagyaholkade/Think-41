import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/products")
      .then(res => setProducts(res.data))
      .catch(err => console.error("Error fetching products", err));
  }, []);

  return (
    <div className="grid grid-cols-3 gap-4 p-6">
      {products.map(product => (
        <div key={product.id} className="border p-4 rounded shadow">
          <h2 className="text-lg font-bold">{product.name}</h2>
          <p>₹ {product.price}</p>
          <p className="text-sm text-gray-600">{product.department_name}</p>
          <Link to={`/products/${product.id}`} className="text-blue-500">View Details</Link>
        </div>
      ))}
    </div>
  );
}

export default ProductList;