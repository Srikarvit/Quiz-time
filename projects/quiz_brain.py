class quiz_brain:
    def __init__(self, question):
        self.question_no = 0
        self.question_list = question
        self.score = 0

    def still_have_questions(self):
        if self.question_no <= len(self.question_list) - 1:
            return True
        else:
            return False
        
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False)")
        self.check_answer(current_question.answer, user_answer)


    def check_answer(self, current_answer, user_answer):
        if current_answer.lower() == user_answer.lower():
            print("You got it Right")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_no}")
        else:
            print(" That's a wrong answer ")
            print(f"Your score was {self.score}/{self.question_no}")
        print(f"The correct answer was {current_answer}")