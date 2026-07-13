import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { courseService } from '../services/api';

function DashboardPage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const userData = localStorage.getItem('user');
    if (userData) {
      setUser(JSON.parse(userData));
    }
    fetchCourses();
  }, []);

  const fetchCourses = async () => {
    try {
      const response = await courseService.getAll();
      setCourses(response.data.data || []);
    } catch (error) {
      console.error('Failed to fetch courses:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold text-gray-800">Faculty ERP</h1>
            {user && <p className="text-gray-600">Welcome, {user.full_name}</p>}
          </div>
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
          >
            Logout
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-gray-600 text-sm uppercase tracking-wide">My Courses</h2>
            <p className="text-3xl font-bold text-gray-800 mt-2">{courses.length}</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-gray-600 text-sm uppercase tracking-wide">Total Students</h2>
            <p className="text-3xl font-bold text-gray-800 mt-2">-</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-gray-600 text-sm uppercase tracking-wide">Pending Tasks</h2>
            <p className="text-3xl font-bold text-gray-800 mt-2">-</p>
          </div>
        </div>

        {/* Courses Section */}
        <div className="bg-white rounded-lg shadow">
          <div className="px-6 py-4 border-b border-gray-200">
            <h2 className="text-xl font-bold text-gray-800">My Courses</h2>
          </div>
          <div className="p-6">
            {loading ? (
              <p className="text-gray-600">Loading courses...</p>
            ) : courses.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {courses.map((course) => (
                  <div key={course.id} className="border border-gray-200 rounded-lg p-4 hover:shadow-lg transition">
                    <h3 className="font-bold text-gray-800">{course.code}</h3>
                    <p className="text-gray-600 text-sm">{course.name}</p>
                    <p className="text-gray-500 text-xs mt-2">{course.credits} Credits</p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-600">No courses assigned yet.</p>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default DashboardPage;
