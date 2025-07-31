import { Link } from 'react-router-dom';

function ProductList({ products }) {
  if (!products) return null;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map(product => (
        <div key={product.id} className="border rounded-lg overflow-hidden shadow hover:shadow-md transition-shadow">
          <div className="p-4">
            <h3 className="font-bold text-lg mb-2">{product.name}</h3>
            <p className="text-gray-800 mb-2">${product.price.toFixed(2)}</p>
            {product.department_name && (
              <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded mb-3">
                {product.department_name}
              </span>
            )}
            <Link 
              to={`/products/${product.id}`}
              className="mt-2 inline-block text-blue-600 hover:underline"
            >
              View Details
            </Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProductList;import { Link } from 'react-router-dom';

function ProductList({ products }) {
  if (!products) return null;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map(product => (
        <div key={product.id} className="border rounded-lg overflow-hidden shadow hover:shadow-md transition-shadow">
          <div className="p-4">
            <h3 className="font-bold text-lg mb-2">{product.name}</h3>
            <p className="text-gray-800 mb-2">${product.price.toFixed(2)}</p>
            {product.department_name && (
              <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded mb-3">
                {product.department_name}
              </span>
            )}
            <Link 
              to={`/products/${product.id}`}
              className="mt-2 inline-block text-blue-600 hover:underline"
            >
              View Details
            </Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProductList;