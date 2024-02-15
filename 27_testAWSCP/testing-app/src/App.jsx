import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AddQuestion from './AddQuestion';
import SearchQuestions from './SearchQuestions';
import QuestionList from './QuestionList';

function App() {
  const [questions, setQuestions] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    try {
      const response = await axios.get('http://localhost:5000/questions');
      setQuestions(response.data.questions);
    } catch (error) {
      console.error('Error fetching questions:', error);
    }
  };

  const deleteQuestion = async (questionId) => {
    try {
      await axios.delete(`http://localhost:5000/questions/${questionId}`);
      fetchQuestions();
    } catch (error) {
      console.error('Error deleting question:', error);
    }
  };

  const updateQuestion = async (updatedQuestion) => {
    try {
      await axios.put(`http://localhost:5000/questions/${updatedQuestion.id}`, updatedQuestion);
      fetchQuestions();
    } catch (error) {
      console.error('Error updating question:', error);
    }
  };

  const handleSearchInputChange = (e) => {
    setSearchQuery(e.target.value);
  };

  const filteredQuestions = questions.filter((question) =>
    question.question.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="App">
      <h1>Question Bank</h1>
      <AddQuestion fetchQuestions={fetchQuestions} />
      <SearchQuestions handleSearchInputChange={handleSearchInputChange} searchQuery={searchQuery} />
      <QuestionList
        filteredQuestions={filteredQuestions}
        fetchQuestions={fetchQuestions}
        deleteQuestion={deleteQuestion}
        updateQuestion={updateQuestion}
      />
    </div>
  );
}

export default App;
