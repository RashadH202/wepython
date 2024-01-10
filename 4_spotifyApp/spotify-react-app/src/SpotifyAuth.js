// SpotifyAuth.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SpotifyAuth = () => {
  const [authUrl, setAuthUrl] = useState('');

  useEffect(() => {
    const fetchAuthUrl = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:3001/');
        setAuthUrl(response.data);

        // Redirect the user to the Spotify login URL
        window.location.href = response.data;
      } catch (error) {
        console.error('Error fetching authentication URL:', error);
      }
    };

    // Call the function when the component mounts
    fetchAuthUrl();
  }, []); // Empty dependency array ensures this effect runs once when the component mounts

  return (
    <div>
      <h1>Spotify Authentication</h1>
      {/* No need for any button or link in the render function */}
    </div>
  );
};

export default SpotifyAuth;