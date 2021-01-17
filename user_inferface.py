from tkinter import *
from quiz_brain import QuizBrain
COLOR = '#1A5276'

class UserInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('My quiz game')
        self.window.config(bg=COLOR, padx=20, pady=20)

        self.label = Label(text=f'Your score: {self.quiz.score}/{self.quiz.question_number}', bg=COLOR, fg='white', font=('Arial', 20, 'normal'))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   text='My question',
                                                   font=('Arial', 15, 'normal'),
                                                   width=280)

        image_true = PhotoImage(file='images/true.png')
        self.button_true = Button(image=image_true, command=self.check_if_true)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file='images/false.png')
        self.button_false = Button(image=image_false, command=self.check_if_false)
        self.button_false.grid(row=2, column=1)

        self.display_question()


        self.window.mainloop()


    def display_question(self):
        self.canvas.config(bg='white')
        self.next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=self.next_question)

    def check_if_true(self):
       if self.quiz.check_answer('True'):
           self.canvas.config(bg='green')
       else:
           self.canvas.config(bg='red')
       self.label.config(text=f'Your score: {self.quiz.score}/{self.quiz.question_number}')
       if self.quiz.more_questions_available():
           self.window.after(1000, func=self.display_question)
       else:
           self.disable_buttons()


    def check_if_false(self):
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.label.config(text=f'Your score: {self.quiz.score}/{self.quiz.question_number}')
        if self.quiz.more_questions_available():
            self.window.after(1000, func=self.display_question)
        else:
            self.disable_buttons()

    def disable_buttons(self):
        self.button_true.config(state='disabled')
        self.button_false.config(state='disabled')










