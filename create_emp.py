from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import datetime

from sqlalchemy import DATE, DATETIME


date = datetime.datetime.now().date()
date= str(date)

class Appli(object):
  def __init__(self, master):
     self.master=master
     def sub():
         bank_id= (e_bank_id.get())
         emp_SSN= (e_emp_SSN.get())
         Fname= (e_fname.get())
         Lname= (e_Lname.get())
         telephone_no= (e_telephone_no.get())
         start_date= (e_start_date.get())
         mgr_SSN= (e_mgr_SSN.get())
         dependant_name=(e_dependant_name.get())
         

         if (bank_id == "" or  emp_SSN =="" or Fname ==""or Lname ==""or telephone_no ==""or start_date ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
             #if (mgr_SSN==""):
                 #MessageBox.showinfo("Added emoloyee is a manager") 
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             #start_date=datetime.strptime(start_date, '%Y-%m-%d')
             #start_date=datetime.strptime(start_date, '%Y-%m-%d')
             query ="INSERT INTO employee(bank_id,emp_SSN,Fname,Lname,telephone_no,start_date) VALUES (%s,%s,'%s','%s',%s,'%s')" % (bank_id,emp_SSN,Fname,Lname,telephone_no,start_date)
             #start_date=DATETIME.DATE()
             cursor.execute(query)
             #start_date = cursor.fetchone()
             #start_date=datetime.strptime(start_date, '%Y-%m-%d')
             cursor.execute("commit")
             query ="INSERT INTO emp_dependant(emp_SSN,dependant_name) VALUES (%s, '%s')" % (emp_SSN,dependant_name)
             cursor.execute(query)
             cursor.execute("commit")
             query ="INSERT INTO management(emp_SSN,mgr_ssn) VALUES (%s, '%s')" % (emp_SSN,mgr_SSN)
             cursor.execute(query)
             cursor.execute("commit")
             MessageBox.showinfo("Insert Status", "Inserted Successfully") 
             con.close()

#("insert into bank (bank_id,bank_name) VALUES ('%d', '%s')")
     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#33E9FF")
     self.bottom.pack(fill=X)

     self.heading= Label(self.top, text="Create Employee", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=30)

     #bottom Frame Design 

     #buttons and lables
     
     bank_id = Label(self.bottom, text="Bank Id ", font="arial 14 bold", bg="#33E9FF")
     bank_id.place(x=40, y=55)

     emp_SSN = Label(self.bottom, text="Employee SSN ", font="arial 14 bold", bg="#33E9FF")
     emp_SSN.place(x=40, y=110)

     Fname = Label(self.bottom, text="First Name ", font="arial 14 bold", bg="#33E9FF")
     Fname.place(x=40, y=165)

     Lname = Label(self.bottom, text="Last Name ", font="arial 14 bold", bg="#33E9FF")
     Lname.place(x=40, y=220)

     telephone_no = Label(self.bottom, text=" Telephone Number  ", font="arial 14 bold", bg="#33E9FF")
     telephone_no.place(x=40, y=275)

     start_date = Label(self.bottom, text="Joining date: YYYY-MM-DD-", font="arial 14 bold", bg="#33E9FF")
     start_date.place(x=40, y=330)

     mgr_SSN = Label(self.bottom, text="Manager SSN:Enter NA for manager", font="arial 14 bold", bg="#33E9FF")
     mgr_SSN.place(x=40, y=385)

     dependant_name = Label(self.bottom, text="Dependant Name", font="arial 14 bold", bg="#33E9FF")
     dependant_name.place(x=40, y=440)

     #Enteries
     
     e_bank_id= Entry(self.bottom, width= "60", textvariable=bank_id)
     e_bank_id.place(x=320, y=55)
     e_emp_SSN= Entry(self.bottom, width= "60")
     e_emp_SSN.place(x=320, y=110)
     e_fname= Entry(self.bottom, width= "60")
     e_fname.place(x=320, y=165)
     e_Lname= Entry(self.bottom, width= "60")
     e_Lname.place(x=320, y=220)
     e_telephone_no= Entry(self.bottom, width= "60")
     e_telephone_no.place(x=320, y=275)
     e_start_date= Entry(self.bottom, width= "60")
     e_start_date.place(x=320, y=330)
     e_mgr_SSN= Entry(self.bottom, width= "60")
     e_mgr_SSN.place(x=320, y=385)
     e_dependant_name= Entry(self.bottom, width= "60")
     e_dependant_name.place(x=320, y=440)
     
     
     
     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="30", command=sub)
     self.submit.place(x=320 , y=550)
     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("900x700+200+0")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
