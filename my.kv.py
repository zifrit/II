from tkinter import *
from tkinter import messagebox

rooot = Tk()

rooot.resizable(width=False, height=False)
rooot.geometry('300x250')
rooot.title('Window')
rooot['bg'] = '#42424d'


def last(event):
    L = login.get()
    P = password.get()

    if L and P:
        messagebox.showinfo('Info', 'Welcome user')
    elif not L and P:
        messagebox.showerror('Error 0.1', "don't")
    elif L and not P:
        messagebox.showerror('Error 0.2', "don't")
    else:
        messagebox.showwarning('Error 1.0', "don't")


tex_login = Label(rooot, text='Login', font='Comfort 20',
                  fg='#64d6de',
                  bg='#42424d')
login = Entry(font='Comfort 12',
              fg='#f0feff',
              bg='#ada5b5',
              relief='solid',
              justify='center')
tex_Password = Label(text='Pasword', font='Comfort 20',
                     fg='#64d6de',
                     bg='#42424d')
password = Entry(rooot, font='Comfort 12',
                 fg='#f0feff',
                 bg='#ada5b5',
                 relief='solid',
                 justify='center',
                 show='#')
check = Checkbutton(text='Остаться в системе', font='Comfort 15',
                    bg='#42424d',
                    fg='#fff',
                    activebackground='#42424d',
                    activeforeground='#fff')
enter = Button(text='Войти',
               relief='flat',
               activebackground='#42424d',
               activeforeground='#fff',
               width='24')

tex_login.pack()
login.pack()
tex_Password.pack()
password.pack()
check.pack()
enter.pack()

enter.bind('<Button-1>', last)

rooot.mainloop()
