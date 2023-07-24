
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












# from tkinter import *
# # window=Tk()
# # window.title("Welcome to HVPM")
# # window.minsize(width=200,height=400)
# # window.maxsize(width=500,height=900)
# # window.mainloop()
#
#
# # window=Tk()
# # l1=Label(window,text="HVPM COET",bg="black",fg="white",width=30,height=20)
# # # l1.pack()
# # # l1.grid(row=0,column=1)
# # l1.place(x=50,y=100)
# # window.mainloop()
#
# # window=Tk()
# # i1=photoImage(file="C:/Users/HP/PycharmProjects/pythonProject2/test.png")
# # l1=Label(window,image=i1)
# # l1.pack()
# # window.mainloop()
#
# # window=Tk()
# # b1=Button(window,text="Enter",bg="green",fg="Red")
# # b1.pack()
# # window,mainloop()
#
# # window=Tk()
# # e1=Entry(window,width=20,bd=6,font=("Calibri",20))
# # e1.pack()
# # window.mainloop()
#
# # window=Tk()
# # window.title("Welcome")
# # window.minsize(width=250,height=250)
# # l1=Label(window,text="Employee Name")
# # l1.place(x=0,y=10)
# # v=StringVar()
# # def edtech():
# #     x=v.get()
# #     print(x)
# #     l2.config(text=x)
# # e1=Entry(window,width=20,bd=4,font=("calibri",10),textvariable=v)
# # e1.place(x=99,y=15)
# # b1=Button(window,text="Enter",fg="grey",bg="pink",command=edtech)
# # b1.place(x=120,y=60)
# # l2=Label(window,text="Nothing",fg="black",bg="grey")
# # l2.place(x=120,y=100)
# # cb1=Checkbutton(window,text="Male")
# # cb1.pack()
# # cb1=Checkbutton(window,text="Female")
# # cb1.pack()
# # window=Tk()
# # f1=Frame(window,)
# # f1.pack()
# # f2=Frame(window,)
# # f2.pack(side=BOTTOM)
# # l3=Label(f1,text="My Name")
# # l3.pack()
# # l4=Label(f2,text="Bottom")
# # l4.pack()u
# # lb1=Listbox(window,width=20)
# # lb1.pack()
# # l5=["Tony","puppy","kitty","fluy"]
# # for i in l5:
# #     lb1.insert(END,i)
# # def utech():
# #     lb1.delete(ANCHOR)#select items
# # b1=Button(window,text="Remove",bg="red",command=utech)
# # b1.pack()
# # window.mainloop()
#
# # from tkinter import messagebox
# # window=Tk()
# # v=IntVar()
# # def utech():
# #     print(v.get())
# # rb1=Radiobutton(window,text="yes",value=1,variable=v)
# # rb1.pack()
# # rb2=Radiobutton(window,text="NO",value=0,variable=v)
# # rb2.pack()
# # b1=Button(window,text="Enter",command=utech)
# # b1.pack()
# # window.mainloop()
#
# from tkinter import messagebox
# window=Tk()
# v=StringVar()
# def utech():
#     if v.get()=="":
#         messagebox.showwarning("Caution","Its Empty")
#     else:
#         messagebox.showinfo("Successful",v.get())
# e1=Entry(window,font=("calibri",18),width=20,textvariable=v)
# e1.pack()
# b1=Button(window,text="Enter",command=utech)
# b1.pack()
# window.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# window=Tk()
# window.title("Welcome ")
# window.minsize(width=600,height=400)
# window.maxsize(width=700,height=900)
# l1=Label(window,text="ToDo List",font=("Any",30,"bold"),bg="green",fg="black",width=600,height=2)
# l1.pack()
# l2=Label(window,text="Add Items",fg="black",font=("Any",20))
# l2.place(x=20,y=120)
# v=StringVar()
# def Utech():
#     x = v.get()
#     print(x)
#     e1.config(text=x)
# e1=Entry(window,width=30,bd=2,font=("calibri",20),textvariable=v)
# e1.place(x=20,y=170)
# b1=Button(window,text="Submit",bg="black",fg="white",font=("Any",10),border=0,command=Utech)
# b1.place(x=470,y=170)
# l3=Label(window,text="Tasks",fg="black",font=("Any",20))
# l3.place(x=20,y=230)
#
# f1=Frame(window,)
# f1.pack()
# f2=Frame(window,)
# f2.pack(side=BOTTOM)
# l3=Label(f1,text="My Name")
# l3.pack()
#
# lb1=Listbox(window,width=20)
# lb1.pack()
# i=StringVar()
# l5=[i]
# # i=input()
# for i in l5:
#     lb1.insert(END,i)
#
# def Atech():
#     x = i.get()
#     print(x)
#     e2.config(text=x)
# e2=Entry(window,width=30,bd=2,font=("calibri",20),textvariable=i)
# e2.pack()
# b2=Button(window,text="Edit",bg="red",command=Atech)
# b2.pack()
# def utech():
#     lb1.delete(ANCHOR)#select items
# b3=Button(window,text="REMOVE",bg="red",command=utech)
# b3.pack()
#
# window.mainloop()