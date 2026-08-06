from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Create an empty list
question_bank = []

#for loop each data from question_data
for question in question_data:
    #get the data text and answer
    question_text = question["question"]
    question_answer = question["correct_answer"]

    #Create an object called question, then pass the question_text/answer
    question = Question(question_text, question_answer)

    #this is my own code which is a shortcut,
    # and above is the instructor code which is better in code readability
    # question = Question(question["text"], question["answer"])

    #append the question to the empty list create earlier
    question_bank.append(question)
quiz = QuizBrain(question_bank)
# print(quiz.still_has_question())
#
while quiz.still_has_question():
    quiz.next_question()
print("You've Completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")