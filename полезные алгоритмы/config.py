from tkinter import *
import sys


def h(event):
    frame1['bg'] = 'red'
    frame2['bg'] = 'white'


def y(event):
    frame2['bg'] = 'red'
    frame1['bg'] = 'white'


def print_(event):
    label1['text'] = event.char


def t():
    bt1.grid_forget()
    frame1.grid(row=0, column=0, padx=3, pady=3)
    frame2.grid(row=0, column=2, padx=3, pady=3)

    root.bind('<Button-1>', h)
    root.bind('<Button-3>', y)
    bt2.grid(row = 3)


def a():
    bt2.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()
    label1.pack()


    for i in range(61, 123):
        root.bind(chr(i), print_)


def b():
    sys.exit()


root = Tk()

root['bg'] = '#00ff95'
root.title('picture')

root.geometry('800x500')

frame1 = Frame(root, bg='white', width=400, heigh=400)
frame2 = Frame(root, bg='white', width=400, heigh=400)

label1 = Label(root, width=12, font='Ubuntu 100')

bt1 = Button(root, text='кнопка', font='Ubuntu 20', command=t)
bt2 = Button(root, text='кнопка', font='Ubuntu 20', command=b)

bt1.grid(row=0, column=0, pady=225, padx=350)


root.mainloop()
