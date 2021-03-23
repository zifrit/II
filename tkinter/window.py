from tkinter import messagebox
from tkinter.filedialog import *
from tkinter import *


spisok = [123, 1265]


def Register():
    column_lb1.grid_forget()
    column_lb2.grid_forget()
    input_en1.grid_forget()
    input_en2.grid_forget()
    bt1.grid_forget()
    bt2.grid_forget()
    window.geometry('400x350')
    window.title('Register')

    column_lb3.grid(row = 0, padx = 160)
    column_lb4.grid(row = 2, pady=10)
    column_lb5.grid(row = 4)
    input_en3.grid(row = 1)
    input_en4.grid(row = 3, pady=10)
    input_en5.grid(row = 5, pady=10)
    bt3.grid(row = 6)


def Save():
    window.geometry('250x250')
    window.title('Window')
    column_lb3.grid_forget()
    column_lb4.grid_forget()
    column_lb5.grid_forget()
    input_en3.grid_forget()
    input_en4.grid_forget()
    input_en5.grid_forget()
    bt3.grid_forget()
    column_lb1.grid(row=0, padx=60)
    input_en1.grid(row=1, pady=10)
    column_lb2.grid(row=2, )
    input_en2.grid(row=3, pady=10)
    bt1.grid(row=4, pady=15)
    bt2.grid(row=5)
    print(spisok)


def a ():
    if (input_en4.get() == input_en1.get()) and input_en5.get() == input_en2.get():
        messagebox.showinfo('!', 'Welcome user',)
    elif (input_en4.get() != input_en1.get()) or input_en5.get() != input_en2.get():
        messagebox.showwarning('!', 'check your logs and password')


window = Tk()

window.resizable(width=False, height=False)
window.geometry('250x250')
window.title('Window')
window['bg'] = '#42424d'

column_lb1 = Label(window, font='Times, 20', text='Username', bg='#42424d', fg='#c8baff')
column_lb2 = Label(window, font='Times, 20', text='Password', bg='#42424d', fg='#c8baff')
column_lb3 = Label(window, font='Times, 20', text='Name', bg='#42424d', fg='#c8baff')
column_lb4 = Label(window, font='Times, 20', text='NewLogin', bg='#42424d', fg='#c8baff')
column_lb5 = Label(window, font='Times, 20', text='NewPassword', bg='#42424d', fg='#c8baff')


input_en1 = Entry(window, font='Times, 11')
input_en2 = Entry(window, font='Times, 11', show='#')
input_en3 = Entry(window, font='Times, 15')
input_en4 = Entry(window, font='Times, 15')
input_en5 = Entry(window, font='Times, 15')


bt1 = Button(window, text='Ввойти', font='Times, 13', bg='#72729e', fg='#c8baff',command = a)
bt2 = Button(window, text='Регистрация', font='Times, 9', bg='#72729e', fg='#c8baff', command = Register)
bt3 = Button(window, text='Сохранить', font='Times, 12', bg='#72729e', fg='#c8baff', command = Save)


column_lb1.grid(row=0, padx=60)
input_en1.grid(row=1, pady=10)
column_lb2.grid(row=2, )
input_en2.grid(row=3, pady=10)
bt1.grid(row=4, pady=15)
bt2.grid(row=5)
window.mainloop()
