import random

class MathQuiz:
    def __init__(self, num_questions=100):
        self.num_questions = num_questions
        self.questions = []
        self.answers = {}
    
    def generate_questions(self):
        """Generate math questions and their answers."""
        for _ in range(self.num_questions):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(['+', '-', '*', '/'])
            
            if operator == '+':
                question = f"What is {num1} + {num2}?"
                answer = num1 + num2
            elif operator == '-':
                question = f"What is {num1} - {num2}?"
                answer = num1 - num2
            elif operator == '*':
                question = f"What is {num1} * {num2}?"
                answer = num1 * num2
            elif operator == '/':
                # Ensure division results in integer for simplicity
                num1, num2 = sorted([num1, num2], reverse=True)  # Ensure num1 >= num2
                question = f"What is {num1} / {num2} (integer division)?"
                answer = num1 // num2
            
            self.questions.append((question, answer))
    
    def run_quiz(self):
        """Run the interactive quiz."""
        print("Welcome to the Math Quiz!")
        print("Please provide your answers. Type 'q' to quit the quiz.")
        print("------------------------------------------------------")

        for idx, (question, answer) in enumerate(self.questions, start=1):
            user_answer = input(f"Question {idx}: {question} Answer: ").strip().lower()

            if user_answer == 'q':
                break

            try:
                user_answer = int(user_answer)  # Convert user input to integer
                self.answers[idx] = user_answer
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        
        print("\nQuiz completed! Here are your answers:")
        self.show_answers()

    def show_answers(self):
        """Display the quiz questions, user's answers, and correct answers."""
        for idx, (question, correct_answer) in enumerate(self.questions, start=1):
            user_answer = self.answers.get(idx, "No answer provided")
            print(f"\nQuestion {idx}: {question}")
            print(f"Your answer: {user_answer}")
            print(f"Correct answer: {correct_answer}")


def main():
    # Initialize MathQuiz object
    quiz = MathQuiz(num_questions=100)
    
    # Generate quiz questions
    quiz.generate_questions()
    
    # Run the quiz
    quiz.run_quiz()


if __name__ == "__main__":
    main()
