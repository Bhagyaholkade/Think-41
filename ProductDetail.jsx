import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/products/${id}`)
      .then(res => setProduct(res.data))
      .catch(err => console.error("Error fetching product", err));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">{product.name}</h2>
      <p>Description: {product.description}</p>
      <p>Price: ₹ {product.price}</p>
      <p>Department: {product.department_name}</p>
    </div>
  );
}

export default ProductDetail;