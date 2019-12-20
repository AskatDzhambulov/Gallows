import random
from tkinter import *;

root= Tk()
root.title('Gallows')
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def but():
    y=0
    while y < 600:
        x =0
        while x < 600:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x = x+33
        y = y+27

but()

faq = '''Let`s play'''

canvas.create_text(310, 240, text=faq, fill="purple", font=("Helvetica", "14"))
words = ["chazzan", "chazzen", "fuzzing", "buzzing", "frizzly", "muzzily", "fizzily"]

def arr():
    word = random.choice(words)
    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetica", "18"))
    a1 = canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a2 = canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a3 = canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a4 = canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a5 = canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a6 = canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetica", "18"))
    list1 = [1,2,3,4,5,6]
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    error = []
    win = []

    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]

        if v in wor:
            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = '1'

            if not v in wor:
                bnt[key] ["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index((v))
                b2 = list1[ind2]
                canvas.create_text(150, 150, text = "You win!", fill="purple", font=("Helvetica", "18"))

    bnt = {}

    def gen(u, x, y, btn=None):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))


btn01 = Button(root, text="Start!", width=10, height=2, command=lambda: arr( ))
btn01.place(x=258, y=542)
btn01["bg"] = "red"


root.mainloop()