from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from user_inferface import UserInterface

question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]

quiz = QuizBrain(question_bank)

ui = UserInterface(quiz)




