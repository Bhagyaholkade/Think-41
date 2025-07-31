import { Link } from 'react-router-dom';

function DepartmentCard({ department }) {
  return (
    <li>
      <Link
        to={`/departments/${department.id}`}
        className="block p-2 hover:bg-gray-100 rounded transition-colors"
      >
        <span className="font-medium">{department.name}</span>
        <span className="ml-2 text-sm text-gray-500">({department.product_count})</span>
      </Link>
    </li>
  );
}

export default DepartmentCard;