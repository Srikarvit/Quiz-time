from question_model import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []
for question in question_data:
    temp = Question(question["question"], question["answer"])
    question_bank.append(temp)

quiz = quiz_brain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

    if quiz.question_no % 10 == 0:
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            break

print(f"\nYour total score was {quiz.score}/{quiz.question_no}")
