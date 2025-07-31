import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function DepartmentsList() {
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:5000/api/departments')
      .then(res => {
        setDepartments(res.data.departments);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching departments", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="p-4">Loading departments...</div>;

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-bold mb-4">Shop by Department</h2>
      <ul className="space-y-2">
        <li>
          <Link to="/products" className="text-blue-500 hover:underline">
            All Products
          </Link>
        </li>
        {departments.map(dept => (
          <li key={dept.id}>
            <Link 
              to={`/departments/${dept.id}`} 
              className="text-blue-500 hover:underline"
            >
              {dept.name} ({dept.product_count})
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DepartmentsList;