# Define the QuizBrain class
class QuizBrain:
    def __init__(self, q_list):
        # Initialize a new QuizBrain object with question number, score, and a list of questions
        self.question_number = 0  # Keep track of the current question number
        self.score = 0  # Keep track of the user's score
        self.question_list = q_list  # Store the list of Question objects

    def still_has_question(self):
        # Check if there are still questions in the list
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Display the next question and get user input for the answer
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"q. {self.question_number}; {current_question.text} (true or false?):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Check if the user's answer is correct and update the score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score} / {self.question_number}")
            print("\n")