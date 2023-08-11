from tkinter import *
from random import randint

root =Tk()
root.title("Password generator")
root.iconbitmap("C:/Users/Parth/Downloads/password generator.bmp")
root.geometry("500x300")


def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(my_entry.get())

    my_password =''
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_append(pw_entry.get()) 

lf = LabelFrame(root, text="Specify the desired length of the password", font=('Arial', 14))
lf.pack(pady=20)

my_entry = Entry(lf, font=('Arial', 22))
my_entry.pack(pady=20, padx=20)

pw_entry= Entry(root, text='', font=('Arial', 22))
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command= new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()