# Importing necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creating an empty list to store Question objects
question_bank = []

# Iterating through the question data and creating Question objects
for question in question_data:
    # Extracting question text and correct answer from the data
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    # Creating a new Question object and adding it to the question_bank list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating a QuizBrain object with the question bank
quiz = QuizBrain(question_bank)

# Running the quiz loop until there are no more questions
while quiz.still_has_question():
    quiz.next_question()

# Displaying completion message and final score
print("You've completed the quiz.")
print(f"Your final score: {quiz.score} / {quiz.question_number}")