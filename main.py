from operator import truediv
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data:
    my_question_text = i["question"]
    my_question_ans = i["correct_answer"]
    new_question = Question(my_question_text, my_question_ans)
    question_bank.append(new_question)
#print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz💀 ")
print(f"Your final score was {quiz.score}/{quiz.question_number}")


