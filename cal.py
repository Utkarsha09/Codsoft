from tkinter import *
import math

window=Tk()
window.geometry('400x500')
window.config(bg="#000088")
window.title("Calculator")

calculation=""

def show(value):
    global calculation
    calculation= calculation + str(value)
    Num.set(calculation)
    # e1.config(text=calculation)

def equalpress():
    total=str(eval(calculation))
    Num.set(total)

def clear():
    global calculation
    calculation=""
    Num.set("")

Num=StringVar()
e1=Entry(window,font=("time",24),border=2,textvariable=Num)
e1.pack(pady=20)

b1=Button(window,text="C",font=("Any",10),padx=20,pady=20,command=clear)
b1.place(x=40,y=80)
b2=Button(window,text=".",font=("Any",10),padx=20,pady=20,command=lambda: show("."))
b2.place(x=120,y=80)
b3=Button(window,text="/",font=("Any",10),padx=20,pady=20,command=lambda: show("/"))
b3.place(x=200,y=80)
b4=Button(window,text="=",font=("Any",10),padx=20,pady=20,command=equalpress)
b4.place(x=280,y=80)
b5=Button(window,text="1",font=("Any",10),padx=20,pady=20,command=lambda: show("1"))
b5.place(x=40,y=150)
b6=Button(window,text="2",font=("Any",10),padx=20,pady=20,command=lambda: show("2"))
b6.place(x=120,y=150)
b7=Button(window,text="3",font=("Any",10),padx=20,pady=20,command=lambda: show("3"))
b7.place(x=200,y=150)
b8=Button(window,text="+",font=("Any",10),padx=20,pady=20,command=lambda: show("+"))
b8.place(x=280,y=150)
b9=Button(window,text="4",font=("Any",10),padx=20,pady=20,command=lambda: show("4"))
b9.place(x=40,y=220)
b10=Button(window,text="5",font=("Any",10),padx=20,pady=20,command=lambda: show("5"))
b10.place(x=120,y=220)
b11=Button(window,text="6",font=("Any",10),padx=20,pady=20,command=lambda: show("6"))
b11.place(x=200,y=220)
b12=Button(window,text="-",font=("Any",10),padx=20,pady=20,command=lambda: show("-"))
b12.place(x=280,y=220)
b13=Button(window,text="7",font=("Any",10),padx=20,pady=20,command=lambda: show("7"))
b13.place(x=40,y=290)
b14=Button(window,text="8",font=("Any",10),padx=20,pady=20,command=lambda: show("8"))
b14.place(x=120,y=290)
b15=Button(window,text="9",font=("Any",10),padx=20,pady=20,command=lambda: show("9"))
b15.place(x=200,y=290)
b16=Button(window,text="*",font=("Any",10),padx=20,pady=20,command=lambda: show("*"))
b16.place(x=280,y=290)
b17=Button(window,text="0",font=("Any",10),padx=20,pady=20,command=lambda: show("0"))
b17.place(x=120,y=360)
window.mainloop()