import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import ProductList from './ProductList';

function DepartmentPage() {
  const { id } = useParams();
  const [department, setDepartment] = useState(null);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [deptRes, productsRes] = await Promise.all([
          axios.get(`http://localhost:5000/api/departments/${id}`),
          axios.get(`http://localhost:5000/api/departments/${id}/products`)
        ]);
        
        setDepartment(deptRes.data);
        setProducts(productsRes.data.products);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  if (loading) return <div className="p-8 text-center">Loading department...</div>;
  if (error) return <div className="p-8 text-red-500">Error: {error}</div>;
  if (!department) return <div className="p-8">Department not found</div>;

  return (
    <div className="p-4">
      <div className="mb-6">
        <h1 className="text-2xl font-bold">{department.name}</h1>
        <p className="text-gray-600">{department.product_count} products available</p>
      </div>
      
      {products.length > 0 ? (
        <ProductList products={products} />
      ) : (
        <div className="bg-yellow-50 p-4 rounded-lg border border-yellow-200">
          <p>No products found in this department</p>
        </div>
      )}
    </div>
  );
}

export default DepartmentPage;