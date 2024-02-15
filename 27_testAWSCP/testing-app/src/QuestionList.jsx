import React from 'react';
import axios from 'axios';

const QuestionList = ({ filteredQuestions, fetchQuestions }) => {

  const deleteQuestion = async (questionId) => {
    try {
      await axios.delete(`http://localhost:5000/questions/${questionId}`);
      fetchQuestions(); // Fetch updated questions after deleting one
    } catch (error) {
      console.error('Error deleting question:', error);
    }
  };

  const updateQuestion = async (updatedQuestion) => {
    try {
      await axios.put(`http://localhost:5000/questions/${updatedQuestion.id}`, updatedQuestion);
      fetchQuestions(); // Fetch updated questions after updating one
    } catch (error) {
      console.error('Error updating question:', error);
    }
  };

  const handleChoiceChange = (e, index, question) => {
    const choices = [...question.choices];
    choices[index] = e.target.value;
    updateQuestion({ ...question, choices });
  };

  const addChoiceInput = async (question) => {
    const choices = [...question.choices, '']; // Add an empty choice
    try {
      await axios.put(`http://localhost:5000/questions/${question.id}`, { ...question, choices });
      fetchQuestions(); // Fetch updated questions after adding choice
    } catch (error) {
      console.error('Error adding choice:', error);
    }
  };

  const removeChoiceInput = async (index, question) => {
    const choices = [...question.choices.slice(0, index), ...question.choices.slice(index + 1)];
    try {
      await axios.put(`http://localhost:5000/questions/${question.id}`, { ...question, choices });
      fetchQuestions(); // Fetch updated questions after removing choice
    } catch (error) {
      console.error('Error removing choice:', error);
    }
  };

  const handleUpdateQuestion = async (question) => {
    try {
      await axios.put(`http://localhost:5000/questions/${question.id}`, question);
      fetchQuestions(); // Fetch updated questions after updating
    } catch (error) {
      console.error('Error updating question:', error);
    }
  };

  return (
    <div>
      <h2>Questions</h2>
      <ul>
        {filteredQuestions.map((question) => (
          <li key={question.id}>
            <strong>Question:</strong> 
            <input
              type="text"
              value={question.question}
              onChange={(e) => updateQuestion({ ...question, question: e.target.value })}
            />
            <br />
            <strong>Choices:</strong> 
            {question.choices.map((choice, index) => (
              <div key={index}>
                <input
                  type="text"
                  value={choice}
                  onChange={(e) => handleChoiceChange(e, index, question)}
                />
                <button onClick={() => removeChoiceInput(index, question)}>Remove</button>
              </div>
            ))}
            <button onClick={() => addChoiceInput(question)}>Add Choice</button>
            <br />
            <strong>Correct Answer:</strong> 
            <input
              type="text"
              value={question.correct_answer}
              onChange={(e) => updateQuestion({ ...question, correct_answer: e.target.value })}
            />
            <button onClick={() => deleteQuestion(question.id)}>Delete</button>
            <button onClick={() => handleUpdateQuestion(question)}>Update</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default QuestionList;
