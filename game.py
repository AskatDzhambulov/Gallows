import random
from tkinter import *;

from tk import canvas, root;
from firstPageClass import FirstPage;
from cell import cell;
from errorAction import head, body, armL, armR, footR, footL;


faq = '''One of the players makes a word - writes the first
and last letter of the word on paper and marks the places
for the remaining letters, for example with lines 
(there is also an option when initially all the letters of
the word are unknown). A gallows with a noose is also drawn.'''

firstData = FirstPage(faq, 'Askat', 'Dzhambulov', 'COM-17')

canvas.create_text(310, 240, text=FirstPage.about(firstData), fill="purple", font=("Helvetica", "14"))
canvas.create_text(450, 500, text=('by'+ ' ' + FirstPage.author(firstData)), fill="red", font=("Helvetica", "14"))
words =[]

with open('words.txt') as dictionary:
    for line in dictionary:
        list = [elt.strip() for elt in line.split(',')]
        words = list

def arr():
    cell()
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
    a5 = canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a6 = canvas.create_text(477, 40, text=word[-1], fill="purple", font=("Helvetica", "18"))
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

            def kord():
                if b2 ==1:
                    x1,y1 = 315, 40
                if b2 ==2:
                    x1,y1 = 347, 40
                if b2 ==3:
                    x1,y1 = 380, 40
                if b2 ==4:
                    x1,y1 = 412, 40
                if b2 ==5:
                    x1,y1 = 444, 40
                if b2 ==6:
                    x1,y1 = 477, 40
                return x1, y1

            x1, y1 = kord()

            win.append(v)
            a2 = canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))
            btn[key] ["bg"] = "green"
            if not v in wor:
                btn[key] ["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index((v))
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win) == 5:
                canvas.create_text(150, 150, text="You win!", fill="purple", font=("Helvetica", "18"))
                for i in alfabet:
                    btn[i] ["state"] = "disabled"
        else:
            error.append(v)
            btn[key] ["bg"] = "red"
            btn[key] ["state"] = "disabled"

            if len(error) == 1:
                head()
            elif len(error) == 2:
                body()
            elif len(error) == 3:
                armR()
            elif len(error) == 4:
                armL()
            elif len(error) == 5:
                footL()
            elif len(error) == 6:
                footR()
                end()
            root.update()

    btn = {}

    def gen(u, x, y):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))
    x = 265
    y = 110
    for i in alfabet[0:8]:
        gen(i, x, y)
        x = x+ 33
    x = 265
    y = 137
    for i in alfabet[8:16]:
        gen(i, x, y)
        x = x+ 33
    x = 265
    y = 164
    for i in alfabet[16:24]:
        gen(i, x, y)
        x = x+ 33
    x = 265
    y = 191
    for i in alfabet[24:26]:
        gen(i, x, y)
        x = x + 33

    def end():

        canvas.create_text(150, 150, text="You lose", fill="purple", font=("Helvetica", "18"))
        for i in alfabet:
            btn[i] ["state"] = "disabled"


btn01 = Button(root, text="Start!", width=10, height=2, command=lambda: arr( ))
btn01.place(x=258, y=542)
btn01 ["bg"] = "red"


root.mainloop()