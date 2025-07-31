import { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import axios from 'axios';

function ProductList({ products: propProducts }) {
  const [products, setProducts] = useState(propProducts || []);
  const [loading, setLoading] = useState(!propProducts);
  const location = useLocation();

  useEffect(() => {
    if (!propProducts && location.pathname === '/products') {
      axios.get("http://localhost:5000/api/products")
        .then(res => {
          setProducts(res.data);
          setLoading(false);
        })
        .catch(err => {
          console.error("Error fetching products", err);
          setLoading(false);
        });
    }
  }, [location.pathname, propProducts]);

  if (loading) return <p>Loading products...</p>;

  return (
    <div className="grid grid-cols-3 gap-4">
      {products.map(product => (
        <div key={product.id} className="border p-4 rounded shadow">
          <h2 className="text-lg font-bold">{product.name}</h2>
          <p>${product.price}</p>
          {product.department_name && (
            <p className="text-sm text-gray-600">{product.department_name}</p>
          )}
          <Link to={`/products/${product.id}`} className="text-blue-500">
            View Details
          </Link>
        </div>
      ))}
    </div>
  );
}

export default ProductList;