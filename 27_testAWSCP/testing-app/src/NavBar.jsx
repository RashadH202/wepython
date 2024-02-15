import React, { useState } from 'react';
import { Navbar, Nav, Form } from 'react-bootstrap';
import AddQuestionModal from './AddQuestionModal';
import SearchQuestions from './SearchQuestions';
import TestGenerator from './TestGenerator';

const NavBar = ({ fetchQuestions, handleSearchInputChange,searchQuery }) => {

    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="#home">TestingApp</Navbar.Brand>
            <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <AddQuestionModal fetchQuestions={fetchQuestions} />
            </Nav>
            <Nav >
            <Form inline="true">
                <SearchQuestions
                    handleSearchInputChange={handleSearchInputChange}
                    searchQuery={searchQuery}
                />
               
            </Form>
            </Nav>
                  <Nav >
            <Form inline="true">
            <TestGenerator />
            </Form>
            
            </Nav>
        </Navbar>
    );
};

export default NavBar;