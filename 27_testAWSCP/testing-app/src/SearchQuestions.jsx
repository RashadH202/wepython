import React from 'react';

const SearchQuestions = ({ handleSearchInputChange, searchQuery }) => {
  return (
    <div>
      <h2>Search</h2>
      <input
        type="text"
        placeholder="Search questions..."
        value={searchQuery}
        onChange={handleSearchInputChange}
      />
    </div>
  );
};

export default SearchQuestions;
