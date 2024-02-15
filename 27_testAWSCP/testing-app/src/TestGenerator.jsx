import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Modal, Button } from 'react-bootstrap';

const TestGenerator = () => {
    const [questions, setQuestions] = useState([]);
    const [selectedQuestions, setSelectedQuestions] = useState([]);
    const [totalQuestions, setTotalQuestions] = useState(100); // Default total number of questions
    const [showModal, setShowModal] = useState(false);
    const [userAnswers, setUserAnswers] = useState({}); // Store user's answers

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

    const generateTest = () => {
        const selected = [];

        // Select random questions to meet the total number specified by the user
        const shuffledQuestions = questions.sort(() => 0.5 - Math.random());
        for (let i = 0; i < totalQuestions && i < shuffledQuestions.length; i++) {
            selected.push(shuffledQuestions[i]);
        }

        setSelectedQuestions(selected);
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
        // Reset user's answers when closing the modal
        setUserAnswers({});
    };

    const handleUserAnswer = (questionId, selectedAnswer) => {
        setUserAnswers(prevAnswers => ({
            ...prevAnswers,
            [questionId]: selectedAnswer
        }));
    };

    const isAnswerCorrect = (questionId, selectedAnswer) => {
        const question = selectedQuestions.find(q => q.id === questionId);
        return question.correct_answer === selectedAnswer;
    };

    return (
        <div>
            <div>
                <span className='numberofquestions_nav'>Number of Questions:</span>
                <input type="number" value={totalQuestions} onChange={(e) => setTotalQuestions(e.target.value)} />
                <Button onClick={generateTest}>Practice Test</Button>
            </div>
            {/* Modal component */}
            <Modal show={showModal} onHide={handleCloseModal}>
                <Modal.Header closeButton>
                    <Modal.Title>Practice Test</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <ul>
                        {selectedQuestions.map(question => (
                            <li key={question.id}>
                                <p>{question.question}</p>
                                <ul>
                                    {question.choices.map(choice => (
                                        <li key={choice}>
                                            <label>
                                                <input
                                                    type="radio"
                                                    name={`question_${question.id}`}
                                                    value={choice}
                                                    onChange={() => handleUserAnswer(question.id, choice)}
                                                />
                                                {choice}
                                            </label>
                                        </li>
                                    ))}
                                </ul>
                                {userAnswers[question.id] && (
                                    <p>
                                        {isAnswerCorrect(question.id, userAnswers[question.id])
                                            ? 'Your answer is correct!'
                                            : `Your answer is wrong. The correct answer is: ${question.correct_answer}`}
                                    </p>
                                )}
                            </li>
                        ))}
                    </ul>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleCloseModal}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default TestGenerator;
