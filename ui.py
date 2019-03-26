from tkinter import *
import pymysql
#create a window object
l = []
window = Tk()
l1 = Label(window,text="Title",)

connect=pymysql.connect(host='localhost',db='mahesh',user='root',password='root')
cursor = connect.cursor()




l1_entry = Entry(window, width=30)
l1_entry.grid(row = 0, column=1)
l1.grid(row = 0, column = 0)

l1 = Label(window, text="Author")
l2_entry = Entry(window, width=30)
l2_entry.grid(row = 1, column=1)

l1.grid(row = 1, column = 0)

l1 = Label(window, text="ISBN")
l3_entry = Entry(window, width=30)
l3_entry.grid(row = 2, column=1)

l1.grid(row = 2, column = 0)

l1 = Label(window, text="Identity")
l4_entry = Entry(window, width=30)
l4_entry.grid(row = 3, column=1)

l1.grid(row = 3, column = 0)

def insert():
    title1 = l1_entry.get()
    Author1 = l2_entry.get()
    ISBN1 = l3_entry.get()
    identity1 = l4_entry.get()
    connect = pymysql.connect(host='localhost',db='mahesh',user='root',password='root')
    with connect:
        cursor = connect.cursor()
        cursor.execute('insert into notebook3 values(%s,%s,%s,%s)',(l1_entry.get(),l2_entry.get(),l3_entry.get(),l4_entry.get(),))
def display():
    cursor.execute("select * from notebook3")
    res = cursor.fetchall()
    for i in res:
        l.append(i)
    print(l)

    
buttond = Button(window, text='display',width=20,height=2,bg='steelblue')
buttond.config(command=display)
buttond.grid(row = 4, column = 4)
buttonin = Button(window, text='click me', width=20, height=2, bg='steelblue')
buttonin.config(command=insert)
buttonin.grid(row=4,column = 2)
    


window.mainloop()
