from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import datetime


date = datetime.datetime.now().date()
date= str(date)

class Appli(object):
  def __init__(self, master):
     self.master=master
     def sub():
         bank_id= (e_bank_id.get())
         cust_ssn= (e_cust_ssn.get())
         Fname= (e_fname.get())
         Lname= (e_Lname.get())
         city= (e_city.get())
         street= (e_street.get())
         

         if (bank_id == "" or  cust_ssn =="" or Fname ==""or Lname ==""or city ==""or street ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             query ="INSERT INTO customer(bank_id,cust_ssn,Fname,Lname,city,street) VALUES (%s,%s,'%s','%s','%s','%s')" % (bank_id,cust_ssn,Fname,Lname,city,street)
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

     self.heading= Label(self.top, text="Create Customer", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=30)

     #bottom Frame Design 

     #buttons and lables
     
     bank_id = Label(self.bottom, text="Bank Id ", font="arial 14 bold", bg="#33E9FF")
     bank_id.place(x=40, y=55)

     cust_ssn = Label(self.bottom, text="Customer SSN ", font="arial 14 bold", bg="#33E9FF")
     cust_ssn.place(x=40, y=110)

     Fname = Label(self.bottom, text="First Name ", font="arial 14 bold", bg="#33E9FF")
     Fname.place(x=40, y=165)

     Lname = Label(self.bottom, text="Last Name ", font="arial 14 bold", bg="#33E9FF")
     Lname.place(x=40, y=220)

     city = Label(self.bottom, text=" City ", font="arial 14 bold", bg="#33E9FF")
     city.place(x=40, y=275)

     street = Label(self.bottom, text="Street ", font="arial 14 bold", bg="#33E9FF")
     street.place(x=40, y=330)

     #Enteries
     
     e_bank_id= Entry(self.bottom, width= "60", textvariable=bank_id)
     e_bank_id.place(x=320, y=55)
     e_cust_ssn= Entry(self.bottom, width= "60")
     e_cust_ssn.place(x=320, y=110)
     e_fname= Entry(self.bottom, width= "60")
     e_fname.place(x=320, y=165)
     e_Lname= Entry(self.bottom, width= "60")
     e_Lname.place(x=320, y=220)
     e_city= Entry(self.bottom, width= "60")
     e_city.place(x=320, y=275)
     e_street= Entry(self.bottom, width= "60")
     e_street.place(x=320, y=330)
     
     
     
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
