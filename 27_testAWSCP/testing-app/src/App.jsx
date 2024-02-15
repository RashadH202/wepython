import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';

import QuestionList from './QuestionList';
import NavBar from './NavBar';

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
    <Container fluid>
      <Row>
        <Col>
        <NavBar 
        handleSearchInputChange={handleSearchInputChange} 
        searchQuery={searchQuery}/>
        </Col>
      </Row>
      <Row>
{/* 
        <Col>
          <SearchQuestions handleSearchInputChange={handleSearchInputChange} searchQuery={searchQuery} />
        </Col> */}
      </Row>
      <Row>
        <Col>
          <QuestionList
            filteredQuestions={filteredQuestions}
            fetchQuestions={fetchQuestions}
            deleteQuestion={deleteQuestion}
            updateQuestion={updateQuestion}
          />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
