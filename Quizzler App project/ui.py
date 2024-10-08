from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterphase:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.label.config(padx=20, pady=20)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width= 280,
                                                     text="Here goes the question",
                                                     fill=THEME_COLOR,
                                                     font=('arial', 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.FALSE_IMG = PhotoImage(file='../Quizzler App project/images/false.png')
        self.TRUE_IMG = PhotoImage(file='../Quizzler App project/images/true.png')
        self.true_button = Button(image=self.TRUE_IMG, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)
        self.false_button = Button(image=self.FALSE_IMG, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.label.config(text='')
            self.canvas.itemconfig(self.question_text, text=f"You have successfully "
                                                            f"completed the Quiz\nYou have scored {self.quiz.score}/10")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback( self.quiz.check_answer('True'))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        if not is_right:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_question)




