from tkinter import *
import random, string

window=Tk()
window.maxsize(width=700,height=1000)
window.minsize(width=400,height=400)
window.config(bg="#858585")
# window.resizable(0,0)

l1=Label(window,text="Password Generator",font=("any",25),bg="#EEEEE0",width=200,height=2)
l1.pack()

l2=Label(window,text="Password Length",font=("arial",18),bg="#858585",)
l2.pack(pady=10)

PassLen=IntVar()
len=Entry(window,font=("Any",22),width=12,textvariable=PassLen)
len.pack(pady=20,padx=20)

PassStr=StringVar()
def gent():
    password=''
    for x in range(0,4):
        password=random.choice(string.ascii_lowercase)+ random.choice(string.ascii_uppercase)+ random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(PassLen.get()-4):
        password=password+random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
        PassStr.set(password)

b1=Button(window,text="Generate Password",font=("Any",16),padx=20,pady=10,command=gent)
b1.pack(pady=15)
e1=Entry(window,font=("Any",22),width=12,textvariable=PassStr)
e1.pack(pady=20,padx=20)

window.mainloop()