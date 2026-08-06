class QuizBrain:
    def __init__(self, q_list):
        #Initialize the question_number to 0, then question_text set to a q_list parameter
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        #I thought that I should iterate every single question and compare
        # Turns out that there is a simple way
        # len_question = len(self.question_list)
        # for question in (self.question_number, len_question):
        #     if question != len_question:
        #         return True
        #     else:
        #         return False

        #Use conditional statement since there is no need to iterate
        return self.question_number < len(self.question_list)

    #Create a method
    def next_question(self):
        #set the question_text to question_text based on question_number then use attribute text to get the question
        current_question = self.question_list[self.question_number]
        # Increment the question_number, In my case I place it below input which is wrong
        self.question_number += 1
        #format the question_text according to the task
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        #called the check_answer method pass the argument user_answer(answer) and the correct answer
        self.check_answer(answer, current_question.answer)

    #Create a method that have a parameter user_answer and correct_answer
    def check_answer(self, user_answer, correct_answer):
        #if user_answer is the same as correct answer print then increment the score to 1
        #Use lower() to correct_answer, since my user_answer is already lower case.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score was: {self.score}/{self.question_number}\n")