from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry


root = Tk()
root.geometry("1300x600+0+0")
root.title("Hospital Managment System")


nvalue=StringVar()
avalue=IntVar()
dvalue=StringVar()
gvalue=StringVar()
rvalue=IntVar()

def add():
    co=sqlite3.connect('hms.db')
    cur=co.cursor()

    cur.execute("insert into hospital(name, age, gender, dob, reference) values(?,?,?,?,?)",(nvalue.get(),
                                                               avalue.get(),
                                                               gvalue.get(),
                                                               dvalue.get(),
                                                               rvalue.get(),
                                                               ))
    co.commit()
    fetch()
    clear()
    co.close()

def clear():
    nvalue.set("")
    avalue.set("")
    dvalue.set("")
    gvalue.set("")
    rvalue.set("")

def getv(ev):
    row=table.focus()
    content=table.item(row)
    rowx=content['values']
    nvalue.set(rowx[0])
    avalue.set(rowx[1])
    dvalue.set(rowx[2])
    gvalue.set(rowx[3])
    rvalue.set(rowx[4])
def update():

    co = sqlite3.connect('hms.db')
    cur = co.cursor()
    cur.execute("UPDATE hospital SET age=?,gender=?,dob=?, reference=? WHERE name=?",
                                                                ( avalue.get(), gvalue.get(),dvalue.get(),rvalue.get(), nvalue.get()))
    co.commit()
    fetch()
    clear()
    co.close()
def delete():
    co = sqlite3.connect('hms.db')
    cur = co.cursor()
    cur.execute("delete from hospital where reference=?",(rvalue.get(),))
    co.commit()
    fetch()
    clear()
    co.close()



l=Label(root,text="Hospital Managment System",font=("Impact 30"),bg="darkblue", fg="white").pack(fill=X)
f1=Frame(root,bg="lightblue")
f1.place(x=10,y=50,height="550",width="500")
m1=Label(f1,text="Manage Patients",font=("Times New Roman", 25 ,"bold"),bg="lightblue").grid(row=0,column=1,pady=15)
m2=Label(f1,text="Patient Name",font="lucida 20",bg="lightblue").grid(row=1,column=0,pady=10)
m3=Label(f1,text="Age",font="lucida 18",bg="lightblue").grid(row=2,column=0,pady=10)
m4=Label(f1,text="Gender",font="lucida 18",bg="lightblue").grid(row=3,column=0,pady=10)
m5=Label(f1,text="D.O.B",font="lucida 18",bg="lightblue").grid(row=4,column=0,pady=10)
m6=Label(f1,text="Reference No.",font="lucida 18",bg="lightblue").grid(row=5,column=0,pady=10)


e1=Entry(f1,textvariable=nvalue,font="lucida 18").grid(row=1,column=1,pady=10,padx=10)
e2=Entry(f1,textvariable=avalue,font="lucida 18").grid(row=2,column=1,pady=10,padx=10)

options=['None', 'Male', 'Female', 'Other']

e3=ttk.OptionMenu(f1, gvalue, *options )
# ttk.Radiobutton(f1,variable=gvalue, value='Female', text='Female').grid(row=3, column=1)
# ttk.Radiobutton(f1,variable=gvalue, value='Other', text='Other').grid(row=4, column=1)
#     #e3["values"]=("Male","Female","Other")
e3.grid(row=3,column=1)
e4=DateEntry(f1,textvariable=dvalue,font="lucida 18").grid(row=4,column=1,pady=10,padx=10)
e5=Entry(f1,textvariable=rvalue,font="lucida 18").grid(row=5,column=1,pady=10,padx=10)


f3=Frame(f1,bg="lightblue")
f3.place(x=20,y=450,height=80,width=450)


b1=Button(f3,text="Add",command=add,font="lucida 20 bold",bg="darkblue", fg="white").pack(side=LEFT,padx=5)
b2=Button(f3,text="Delete",command=delete,font="lucida 20 bold",bg="darkblue", fg="white").pack(side=LEFT,padx=5)
b3=Button(f3,text="Update",command=update,font="lucida 20 bold",bg="darkblue", fg="white").pack(side=LEFT,padx=5)
b4=Button(f3,text="Clear",command=clear,font="lucida 20 bold",bg="darkblue", fg="white").pack(side=LEFT,padx=5)


#value=StringVar()

#e=Entry(f1,textvariable=value).pack()

#Label(f1,text="Manage Patients",font="lucida 15 bold").grid(row=1,column=10)
#f1.grid(row=1,column=0)
f2=Frame(root,bg="lightblue")
f2.place(x=530,y=50,height="550",width="800")
f4=Frame(f2,bg="lightblue")
f4.place(x=300,y=0,width=200,height=45)
Label(f4,text="Patient Info.",font=("Times New Roman", 25 ,"underline bold"),bg="lightblue").pack(pady="10")
Label(f2,text="Refrence No.",font="lucida 18",bg="lightblue").place(x=10,y=80)
refvalue=StringVar()
e6=Entry(f2,textvariable=refvalue,font="lucida 20").place(x=200,y=80)
Button(f2,text="Submit",bg="darkblue", fg="white", font="lucida 15 bold").place(x=150,y=150)

tableF=Frame(f2)
tableF.place(x=10,y=200,width=750,height=320)
xscroll=Scrollbar(tableF,orient=HORIZONTAL)
yscroll=Scrollbar(tableF,orient=VERTICAL)
table=ttk.Treeview(tableF,columns=("name of patient","age","gender","d.o.b","refrence no."),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)
xscroll.config(command=table.xview)
yscroll.config(command=table.yview)
table.heading("name of patient",text="Name Of Patient")
table.heading("age",text="Age")
table.heading("gender",text="Gender")
table.heading("refrence no.",text="Refrence No.")
table.heading("d.o.b",text="D.O.B")
table['show']='headings'
table.column("name of patient",width=200)
table.column("age",width=150)
table.column("gender",width=150)
table.column("d.o.b",width=150)
table.column("refrence no.",width=150)
table.pack(fill=BOTH,expand=1)
table.bind("<ButtonRelease-1>",getv)
def  fetch():
    co = sqlite3.connect('hms.db')
    cur = co.cursor()
    cur.execute("select * from hospital")
    rows=cur.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert("",END,values=row)
            co.commit()
        co.close()
#fetch()





root.mainloop()

#lumpy.class_diagram()