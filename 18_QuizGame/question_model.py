# Define the Question class
class Question:
    def __init__(self, q_text, q_answer):
        # Initialize a new Question object with text and answer attributes
        self.text = q_text  # Store the question text
        self.answer = q_answer  # Store the correct answer