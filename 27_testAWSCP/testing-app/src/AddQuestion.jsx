import React, { useState } from 'react';
import axios from 'axios';

const AddQuestion = ({ fetchQuestions }) => {
  const [newQuestion, setNewQuestion] = useState({
    question: '',
    choices: [''],
    correct_answer: ''
  });

  const handleInputChange = (e, index) => {
    const { value } = e.target;
    const choices = [...newQuestion.choices];
    choices[index] = value;
    setNewQuestion({ ...newQuestion, choices });
  };

  const addChoiceInput = () => {
    setNewQuestion({ ...newQuestion, choices: [...newQuestion.choices, ''] });
  };

  const removeChoiceInput = (index) => {
    const choices = [...newQuestion.choices];
    choices.splice(index, 1);
    setNewQuestion({ ...newQuestion, choices });
  };

  const addQuestion = async () => {
    try {
      await axios.post('http://localhost:5000/questions', newQuestion);
      setNewQuestion({ question: '', choices: [''], correct_answer: '' });
      fetchQuestions();
    } catch (error) {
      console.error('Error adding question:', error);
    }
  };

  return (
    <div>
      <h2>Add New Question</h2>
      Question<input
        type="text"
        placeholder="Question"
        value={newQuestion.question}
        onChange={(e) => setNewQuestion({ ...newQuestion, question: e.target.value })}
      />
      {newQuestion.choices.map((choice, index) => (
        <div key={index}>
            Choice:
          <input
            type="text"
            placeholder={`Choice ${index + 1}`}
            value={choice}
            onChange={(e) => handleInputChange(e, index)}
          />
          <button onClick={() => removeChoiceInput(index)}>Remove</button>
        </div>
      ))}
      <button onClick={addChoiceInput}>Add Choice</button>
      <input
        type="text"
        placeholder="Correct Answer"
        value={newQuestion.correct_answer}
        onChange={(e) => setNewQuestion({ ...newQuestion, correct_answer: e.target.value })}
      />
      <button onClick={addQuestion}>Add Question</button>
    </div>
  );
};

export default AddQuestion;
