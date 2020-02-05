# Written and Compiled by Prosper Chuks

from tkinter import *
import random
import time

root = Tk()
root.geometry("350x570+100+100")
root.title("Calculator")
root.resizable(False, False)


one = StringVar()
operator = ""

frame = Frame(root, width=300, height=700, bg="#343434", relief=SUNKEN)
frame.pack()

#==================================Functions================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    one.set(operator)

def clearScreen():
    global operator
    operator = ""
    one.set("")

def equals():
    global operator
    sumup = str(eval(operator))
    one.set(sumup)
    operator = ""

#===========================================================================================

mainDisplay = Entry(frame, font=('arial', 20, 'bold'), textvariable=one,
                    bd=30, bg='#343434', fg='white', insertwidth=4)
mainDisplay.grid(columnspan = 9)

#===============================789=========================================================

btn7 = Button(frame, font=('arial', 20, 'bold'), text=7, bg='#343434', bd=10, activebackground='#343434',
             command=lambda: btnClick(7), padx=15, pady=15, fg='white').grid(row=1, column=0)

btn8 = Button(frame, font=('arial', 20, 'bold'), text=8, activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick(8), padx=15, pady=15, fg='white').grid(row=1, column=1)

btn9 = Button(frame, font=('arial', 20, 'bold'), text=9, activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick(9), padx=15, pady=15, fg='white').grid(row=1, column=2)

add = Button(frame, font=('arial', 19, 'bold'), text='+', activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick('+'), padx=15, pady=15, fg='white').grid(row=1, column=3)

#================================456========================================================

btn4 = Button(frame, font=('arial', 20, 'bold'), text=4, bg='#343434', activebackground='#343434', bd=10,
             command=lambda: btnClick(4), padx=15, pady=15, fg='white').grid(row=2, column=0)

btn5 = Button(frame, font=('arial', 20, 'bold'), text=5, activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick(5), padx=15, pady=15, fg='white').grid(row=2, column=1)

btn6 = Button(frame, font=('arial', 20, 'bold'), text=6, activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick(6), padx=15, pady=15, fg='white').grid(row=2, column=2)

subtract = Button(frame, font=('arial', 20, 'bold'), text='-', activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick('-'), padx=15, pady=15, fg='white').grid(row=2, column=3)

#================================123========================================================

btn1 = Button(frame, font=('arial', 20, 'bold'), text=1, bg='#343434', activebackground='#343434', bd=10,
             command=lambda: btnClick(1), padx=15, pady=15, fg='white').grid(row=3, column=0)

btn2 = Button(frame, font=('arial', 20, 'bold'), text=2, activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick(2), padx=15, pady=15, fg='white').grid(row=3, column=1)

btn3 = Button(frame, font=('arial', 20, 'bold'), text=3, activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick(3), padx=15, pady=15, fg='white').grid(row=3, column=2)

multiply = Button(frame, font=('arial', 20, 'bold'), text='*', activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick('*'), padx=15, pady=15, fg='white').grid(row=3, column=3)

#===========================================================================================

btn0 = Button(frame, font=('arial', 20, 'bold'), text=0, bg='#343434', activebackground='#343434', bd=10,
             command=lambda: btnClick(0), padx=15, pady=15, fg='white').grid(row=4, column=0)

btnPoint = Button(frame, font=('arial', 20, 'bold'), text='.', activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick('.'), padx=15, pady=15, fg='white').grid(row=4, column=1)

btnPercent = Button(frame, font=('arial', 19, 'bold'), text='%', activebackground='#343434', bg='#343434', bd=10,
             command=lambda: btnClick('%'), padx=15, pady=15, fg='white').grid(row=4, column=2)

divide = Button(frame, font=('arial', 20, 'bold'), text='/', activebackground='#343434', bg='#343434', bd=10,
              command=lambda: btnClick('/'), padx=15, pady=15, fg='white').grid(row=4, column=3)

#===========================================================================================

btnClear = Button(frame, font=('arial', 20, 'bold'), text='C', bg='#343434', activebackground='#343434', bd=10,
            padx=30, pady=5, fg='white', command=lambda: clearScreen()).grid(row=5, column=0, columnspan=2)

btnEquals = Button(frame, font=('arial', 20, 'bold'), text='=', bg='#343434', activebackground='#343434', bd=10,
            padx=30, pady=5, fg='white', command=lambda: equals()).grid(row=5, column=2, columnspan=2)

# root.iconbitmap(r'C:\Python34\DLLs\logo2.ico')
root.mainloop()
