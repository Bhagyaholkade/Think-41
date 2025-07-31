import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import ProductList from './ProductList';

function DepartmentPage() {
  const { id } = useParams();
  const [department, setDepartment] = useState(null);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

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
        console.error("Error fetching department data", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  if (loading) return <div className="p-4">Loading department...</div>;
  if (!department) return <div className="p-4">Department not found</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-2">{department.name}</h1>
      <p className="text-gray-600 mb-4">{department.product_count} products</p>
      
      {products.length > 0 ? (
        <ProductList products={products} />
      ) : (
        <p>No products found in this department</p>
      )}
    </div>
  );
}

export default DepartmentPage;