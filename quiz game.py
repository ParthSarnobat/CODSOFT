import tkinter as tk

from tkinter import messagebox
from random import shuffle
class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("quiz Game")
        
        self.question =[
            {
                "question": "Which is the tallest mountain in our solar system?",
                "option" : ["Everest","Olympus Mons","Ascraeus Mons", "K2"],
                "answer" : "Olympus Mons"
            },
            {
                "question": "who invented AC(Alternatic current) power?",
                "option" : ["Albert Einstaine","Michel Faraday","Thomas Edison","Nikola Tesla"],
                "answer" : "Nikola Tesla"
            } ,
            {
                "question":"what is the PH of blood?",
                "option" : ["7.40", "5.60", "8", "6.20"],
                "answer" :"7.40"
            },
            {
                "question":"How many moons does saturn have?",
                "option" :["82","62","120","145"],
                "answer" : "145"
            },
            {
                "question":"Country with the largest population",
                "option" :["China","India","Russia","UK"],
                "answer" :"India"
            }
        ]
        self.score=0
        self.current_question=0

        self.question_label=tk.Label(self.root, text="", font=("Arial",14),wraplength=400 )
        self.question_label.pack(pady=20)
        
        self.option_button=[]
        for i in range(4):
           button=tk.Button(self.root, text="", font=("Arial",14), width=30, command=lambda i=i: self.check_answer(i),
                            bg="#FFFFF2")
           button.pack(pady=5)
           self.option_button.append(button)

        self.score_label=tk.Label(self.root, text="Score:", font=("Arial0,12"))
        self.score_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.question):
            question=self.question[self.current_question]
            self.question_label.config(text=question ["question"])
            option=question["option"]
            shuffle (option)
            for i in range (4):
                self.option_button[i].config(text=option[i])
            self.score_label.config(text="score: {}".format(self.score))

        else:
            self.end_game()

    def check_answer (self, selected_option):
        question=self.question [self.current_question]
        selected_answer=question ["option"][selected_option]
        correct_answer=question ["answer"]
        if selected_answer==correct_answer:
            self.score+=1
        self.current_question +=1
        self.next_question ()

    def end_game(self):
        messagebox.showinfo("Game over", "Quiz has ended!\n Your Score: {}".format(self.score))
        self.root.destroy()

root=tk.Tk()

quiz_game=QuizGame(root)

root.mainloop()
    