
from tkinter import *
from tkinter import messagebox
#function
def Ntask():
    task=e1.get()
    if task!= "":
        lb.insert(END, task)
        e1.delete(0, "end")
    else:
        messagebox.showwarning("Warning","Please Enter valid")

def Dtask():
    lb.delete(ANCHOR)
#mainwindow
window=Tk()
window.maxsize(width=1000,height=1000)
window.minsize(width=500,height=500)
window.title("TODO List")
window.config(bg="#FFEBCD")

l1=Label(window,text="ToDo List",font=("Any",20),bg="#8B7D6B",fg="black",width=70)
l1.pack()
frame=Frame(window)
frame.pack(pady=10)

lb=Listbox(frame,width=25,height=8,font=("Time",18),bd=0,fg="#464646",selectbackground="#a2a2a2",border=3)
lb.pack(side=LEFT,fill=BOTH)

Tlist=["task1","task2"]
for i in Tlist:
    lb.insert(END,i)

e1=Entry(window,font=("time",24),border=2)
e1.pack(pady=20)

bf=Frame(window)
bf.pack(pady=20)
#Add item
ATB=Button(bf,text='Add Task',font=("time",14),bg="#8B7D6B",padx=20,pady=10,border=5,command=Ntask)
ATB.pack(fill=BOTH,expand=True,side=RIGHT)
#Delete item
DTB=Button(bf,text="Delete Task", font=("time",14),bg="#8B7D6B",padx=18,pady=10,border=5,command=Dtask)
DTB.pack(fill=BOTH,expand=True,side=LEFT)

window.mainloop()
