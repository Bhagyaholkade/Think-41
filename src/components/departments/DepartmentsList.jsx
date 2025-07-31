import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import DepartmentCard from './DepartmentCard';

function DepartmentsList() {
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDepartments = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/departments');
        setDepartments(response.data.departments);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchDepartments();
  }, []);

  if (loading) return <div className="p-4">Loading departments...</div>;
  if (error) return <div className="p-4 text-red-500">Error: {error}</div>;

  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4 border-b pb-2">Shop by Department</h2>
      <ul className="space-y-2">
        <li className="mb-3">
          <Link 
            to="/products" 
            className="block p-2 hover:bg-gray-100 rounded font-medium text-blue-600"
          >
            All Products
          </Link>
        </li>
        {departments.map(dept => (
          <DepartmentCard key={dept.id} department={dept} />
        ))}
      </ul>
    </div>
  );
}

export default DepartmentsList;