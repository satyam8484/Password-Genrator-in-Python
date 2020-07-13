from tkinter import *
import string
import random

window = Tk()
window.geometry('400x350')
window.resizable(0, 0)


def Genrate_password():
    s = string.ascii_letters + string.punctuation + string.digits
    l1 = list(s)
    plen = int(e1.get())
    pwd = "".join(random.sample(l1, plen))
    l2.config(text="Your Password")
    pass_entry.delete(0, END)
    pass_entry.insert(0, pwd)


f1 = Frame(bg='black')
f1.pack(side=TOP, fill=BOTH)

head = Label(f1, text="Password Genrator", bg='black', fg='white', font=('Helvitika', 16, 'bold'), height=2)
head.pack(side=TOP, fill=BOTH)

l1 = Label(text="Enter password Length", font=('Helvetica', 12, 'bold'))
l1.pack(side=TOP, pady=(20, 10))

e1 = Entry(width=5)
e1.pack(side=TOP, pady=10)

b1 = Button(text="Genrate", command=Genrate_password)
b1.pack(side=TOP, pady=10)

l2 = Label(text="", font=('Helvetica', 12, 'bold'), fg='red')
l2.pack(side=TOP, pady=10)

pass_entry = Entry(text="", font=('Helvetica', 10, 'bold'), )
pass_entry.pack(side=TOP, pady=10)

window.mainloop()
