import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import ProductList from './pages/ProductList';
import ProductDetail from './pages/ProductDetail';
import DepartmentPage from './pages/DepartmentPage';
import DepartmentsList from './components/DepartmentsList';
import Navbar from './components/Navbar';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorBoundary from './components/ErrorBoundary';

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Simulate initial loading
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 1000);
    return () => clearTimeout(timer);
  }, []);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <LoadingSpinner size="large" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center p-6 bg-red-100 rounded-lg">
          <h2 className="text-xl font-bold mb-2">Error Loading Application</h2>
          <p className="mb-4">{error.message}</p>
          <button 
            onClick={() => window.location.reload()}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Reload Page
          </button>
        </div>
      </div>
    );
  }

  return (
    <ErrorBoundary>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          
          <div className="container mx-auto px-4 py-8">
            <div className="flex flex-col md:flex-row gap-8">
              {/* Sidebar - Hidden on mobile, shown on desktop */}
              <div className="w-full md:w-1/4 lg:w-1/5">
                <div className="sticky top-4">
                  <DepartmentsList />
                </div>
              </div>
              
              {/* Main Content Area */}
              <div className="w-full md:w-3/4 lg:w-4/5">
                <Routes>
                  <Route 
                    path="/products" 
                    element={
                      <ErrorBoundary>
                        <ProductList />
                      </ErrorBoundary>
                    } 
                  />
                  <Route 
                    path="/products/:id" 
                    element={
                      <ErrorBoundary>
                        <ProductDetail />
                      </ErrorBoundary>
                    } 
                  />
                  <Route 
                    path="/departments/:id" 
                    element={
                      <ErrorBoundary>
                        <DepartmentPage />
                      </ErrorBoundary>
                    } 
                  />
                  <Route 
                    path="/" 
                    element={
                      <ErrorBoundary>
                        <ProductList />
                      </ErrorBoundary>
                    } 
                  />
                  <Route 
                    path="*" 
                    element={
                      <div className="text-center py-20">
                        <h1 className="text-2xl font-bold mb-4">404 - Page Not Found</h1>
                        <p className="mb-4">The page you're looking for doesn't exist.</p>
                        <Link 
                          to="/" 
                          className="text-blue-500 hover:underline"
                        >
                          Return to Home
                        </Link>
                      </div>
                    } 
                  />
                </Routes>
              </div>
            </div>
          </div>
          
          <footer className="bg-gray-800 text-white py-6 mt-8">
            <div className="container mx-auto px-4 text-center">
              <p>© 2023 E-Commerce App. All rights reserved.</p>
            </div>
          </footer>
        </div>
      </Router>
    </ErrorBoundary>
  );
}

export default App;