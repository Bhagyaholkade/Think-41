import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DepartmentsList from './components/departments/DepartmentsList';
import DepartmentPage from './pages/DepartmentPage';
import ProductList from './pages/ProductList';
import ProductDetail from './pages/ProductDetail';

function App() {
  return (
    <Router>
      <div className="container mx-auto px-4 py-8">
        <div className="flex flex-col md:flex-row gap-8">
          <div className="md:w-1/4">
            <DepartmentsList />
          </div>
          <div className="md:w-3/4">
            <Routes>
              <Route path="/products" element={<ProductList />} />
              <Route path="/products/:id" element={<ProductDetail />} />
              <Route path="/departments/:id" element={<DepartmentPage />} />
              <Route path="/" element={<ProductList />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;