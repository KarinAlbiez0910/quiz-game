import html
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score= 0


    def next_question(self):

        self.question_text = self.questions_list[self.question_number].text
        html.unescape(self.question_text)
        self.question_answer = self.questions_list[self.question_number].answer
        self.question_number = self.question_number + 1
        return f'Q{self.question_number}: {self.question_text} (True or False) '.title()

    def more_questions_available(self):
        if self.question_number <= len(self.questions_list) - 1:
            return True
        else:
            return False

    def check_answer(self, answer):
        if answer.lower() == self.question_answer.lower():
            self.score = self.score + 1
            return True
        else:
            return False

    def your_score(self):
        print('You have completed the quiz')
        print(f'Your score is {self.score}/{self.question_number}.')




