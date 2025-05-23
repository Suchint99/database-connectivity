#Complete Code

from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
from lib2to3.fixer_util import Number
# import filedialog module 
from tkinter import filedialog 
from PIL import Image 


top = tkinter.Tk()

db=sqlite3.connect('test11.db')
cur =db.cursor()
cur.execute("DROP TABLE IF EXISTS student")
cur.execute("CREATE TABLE student (rno INTEGER PRIMARY KEY ,name TEXT (20) NOT NULL,fathers_name TEXT (50),address TEXT (50),city text(20),country text(20),pin text(20),mobno TEXT(10), email text(30), gender text(20),studimage text(80))")

# Use three label to show rno,name address and three entry to enter rno name address
# we can use any layout for placement of all these labels and entry pack,grid or place

L1 = Label(top, text="Rno")
L1.grid(row = 0, column = 0)
E1 = Entry(top, bd =5)
E1.grid(row = 0, column = 1)
L2 = Label(top, text="Name")
L2.grid(row = 1, column = 0)
E2 = Entry(top, bd =5)
E2.grid(row = 1, column = 1)
L3 = Label(top, text="Fathers name")
L3.grid(row = 2, column = 0)
E3 = Entry(top, bd =5)
E3.grid(row = 2, column = 1)
L4 = Label(top, text="Address")
L4.grid(row = 3, column = 0)
E4 = Entry(top, bd =5)
E4.grid(row = 3, column = 1)
L5 = Label(top, text="City")
L5.grid(row = 4, column = 0)
E5 = Entry(top, bd =5)
E5.grid(row = 4, column = 1)

L6 = Label(top, text="Country")
L6.grid(row = 5, column = 0)
E6 = Entry(top, bd =5)
E6.grid(row = 5, column = 1)

L7 = Label(top, text="Pin")
L7.grid(row = 6, column = 0)
E7 = Entry(top, bd =5)
E7.grid(row = 6, column = 1)

L8 = Label(top, text="Mobile No")
L8.grid(row = 7, column = 0)
E8 = Entry(top, bd =5)
E8.grid(row = 7, column = 1)

L9 = Label(top, text="Email")
L9.grid(row = 8, column = 0)
E9 = Entry(top, bd =5)
E9.grid(row = 8, column = 1)

L10 = Label(top, text="Select Gender")
L10.grid(row = 9, column = 0)
v = IntVar() 
Radiobutton(top, text='Male', variable=v, value=1).grid(row = 9, column = 1)
Radiobutton(top, text='Female', variable=v, value=2).grid(row = 9, column = 2)
# This method can insert one record in the tabel
def insert1():
    #Read data from entry boxes
    rno = E1.get()
    name = E2.get()
    fathersname = E3.get()
    address = E4.get()
    city = E5.get()
    country = E6.get()
    pin = E7.get()
    mobno = E8.get()
    email = E9.get()
    studimage = E10.get()
    a =  v.get()
    
    if(a==1):
     gender="Male"
    else:
     gender="Female"
    cur=db.cursor()
    
    qry="insert into student (rno,name,fathers_name,address,city,country,pin,mobno,email,gender,studimage) values(?,?,?,?,?,?,?,?,?,?,?);"
    #This is parameterised sql statement. first prepare SQL with ? in place of data 
    #and in second step pass actual value in same order     
    cur.execute(qry,(rno,name,fathersname,address,city,country,pin,mobno,email,gender,studimage))
    db.commit()
    print ("one record added successfully")

def delete1():
    #Read data from entry boxes
    rno = E1.get()
    
    cur=db.cursor()
    qry="DELETE from student where rno = ?; "
    cur.execute(qry,(rno))
       
    db.commit()
    print("Record delete succesfully")

def update1():
    #Read data from entry boxes
    rno = E1.get()
    name = E2.get()
    fathersname = E3.get()
    address = E4.get()
    city = E5.get()
    country = E6.get()
    pin = E7.get()
    mobno = E8.get()
    email = E9.get()
    a =  v.get()
    
    
    if(a==1):
     gender="Male"
    else:
     gender="Female"
    
    cur=db.cursor()
    qry="update student set name= ? , fathers_name=?, address =? ,city=?,country=?,pin=? , mobno=?,email=? ,gender=? where rno = ?; "
    cur.execute(qry,(name,fathersname,address,city,country,pin,mobno,email,gender,rno))
       
    db.commit()
    print("Record updated succesfully")
# Function for opening the  
# file explorer window 
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"),                                                                                                        ("all files", 
                                                     "*.*")))  
    E9.delete(0,'end')
    E10.insert(0,filename)  
    
    
def show() :
    rno = E1.get()
    qry="SELECT * from student where rno=?;"
    cur=db.cursor()
    cur.execute(qry,(rno,))
    
    record=cur.fetchone()
    #e1.insert(0,record[0])
    E1.delete(0,'end')
    E2.delete(0,'end')
    E3.delete(0,'end')
    E4.delete(0,'end')
    E5.delete(0,'end')
    E6.delete(0,'end')
    E7.delete(0,'end')
    E8.delete(0,'end')
    E9.delete(0,'end')
    E10.delete(0,'end')
    E1.insert(0,record[0])
    E2.insert(0,record[1])
    E3.insert(0,record[2])
    E4.insert(0,record[3])
    E5.insert(0,record[4])
    E6.insert(0,record[5])
    E7.insert(0,record[6])
    E8.insert(0,record[7])
    E9.insert(0,record[8])
    gen=record[9]
    if(gen=="Male"):
     v.set(1)
    else:
     v.set(2)
    # creating a object  
    im = Image.open(record[10])  
    im.show()
    
   
    
    
BInsert = tkinter.Button(text ='Insert', command=insert1)
BInsert.grid(row = 10, column = 0)

BUpdate = tkinter.Button(text ='Update',command=update1)
BUpdate.grid(row = 10, column = 1)

BDelete = tkinter.Button(text ='Delete',command=delete1)
BDelete.grid(row = 11, column = 0)

BSelect = tkinter.Button(text ='Show', command=show)
BSelect.grid(row = 11, column = 1)
button_explore = Button(top,  
                        text = "Upload Image", 
                        command = browseFiles)  
button_explore.grid(row=12,column=0)
E10 = Entry(top, bd =5)
E10.grid(row = 12, column = 1)



#label = Label(top)
#label.pack()

cur =db.cursor()

top.mainloop()
db.close()