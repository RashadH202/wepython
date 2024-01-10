// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import SpotifyAuth from './SpotifyAuth';
import './App.css';

const NavigationBar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-list">
        <li className="nav-item">
          <Link to="/login" className="nav-link">
            Login with Spotify
          </Link>
        </li>
        {/* Add other navigation links as needed */}
      </ul>
    </nav>
  );
};

const App = () => {
  return (
    <Router>
      <NavigationBar />
      <Routes>
        <Route path="/login" element={<SpotifyAuth />} />
        {/* Add other routes as needed */}
      </Routes>
    </Router>
  );
};

export default App;