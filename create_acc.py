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
         account_no= DoubleVar()
         amount= DoubleVar()
         phone_no= DoubleVar()
         account_no = (e_account_no.get())
         bank_id = (e_bank_id.get())
         branch_name = (e_branch_name.get())
         cust_SSN= (e_cust_SSN.get())
         account_type = (t.get())
         balance = (e_balance.get())
         emp_SSN = (e_emp_SSN.get())
         overdraft = (e_overdraft.get())
         intrest_rate = (e_intrest_rate.get())
         b_type = (i.get())

         if (account_no == "" or bank_id == "" or branch_name == "" or account_type =="" or balance =="" or cust_SSN == "" or emp_SSN ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             query ="INSERT INTO account(bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft) VALUES (%s,'%s',%s,%s,'%s','%s','%s')" % (bank_id,branch_name,account_no,balance,account_type,intrest_rate,overdraft)
             cursor.execute(query)
             cursor.execute("commit")
             query ="INSERT INTO cust_banker(cust_SSN,emp_SSN,b_type) VALUES (%s,%s,'%s')" % (cust_SSN,emp_SSN,b_type)
             cursor.execute(query)
             cursor.execute("commit")
             query ="INSERT INTO depositor(cust_SSN,account_no) VALUES (%s,%s)" % (cust_SSN,account_no)
             cursor.execute(query)
             cursor.execute("commit")
             MessageBox.showinfo("Insert Status", "Inserted Successfully")
             con.close()


     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)
     self.bottom= Frame(master, height=1000, bg="#33E9FF")

     self.bottom.pack(fill=X)

     self.heading= Label(self.top, text="Create Account", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=20)

     #bottom Frame Design

     #buttons and lables
     account_no= DoubleVar()
     account_no = Label(self.bottom, text="Account number ", font="arial 14 bold", bg="#33E9FF")
     account_no.place(x=40, y=50)

     bank_id = Label(self.bottom, text="Bank Id ", font="arial 14 bold", bg="#33E9FF")
     bank_id.place(x=40, y=80)

     branch_name = Label(self.bottom, text="Branch Name ", font="arial 14 bold", bg="#33E9FF")
     branch_name.place(x=40, y=110)

     account_type = Label(self.bottom, text="Account Type ", font="arial 14 bold", bg="#33E9FF")
     account_type.place(x=40, y=140)

     balance= DoubleVar()
     balance = Label(self.bottom, text="Initial Amount ", font="arial 14 bold", bg="#33E9FF")
     balance.place(x=40, y=170)

     cust_SSN = Label(self.bottom, text="Customer SSN ", font="arial 14 bold", bg="#33E9FF")
     cust_SSN.place(x=40, y=200)
     
     emp_SSN = Label(self.bottom, text="Employee SSN ", font="arial 14 bold", bg="#33E9FF")
     emp_SSN.place(x=40, y=230)

     b_type = Label(self.bottom, text="Banker Type ", font="arial 14 bold", bg="#33E9FF")
     b_type.place(x=40, y=260)

     intrest_rate = Label(self.bottom, text="Intrest rate : NA for checking Acc ", font="arial 14 bold", bg="#33E9FF")
     intrest_rate.place(x=40, y=290)

     overdraft = Label(self.bottom, text="Overdraft : NA for savings Acc ", font="arial 14 bold", bg="#33E9FF")
     overdraft.place(x=40, y=320)

     #Enteries
     
     e_account_no= Entry(self.bottom, width= "60", textvariable=account_no)
     e_account_no.place(x=320, y=50)

     e_bank_id= Entry(self.bottom, width= "60")
     e_bank_id.place(x=320, y=80)

     e_branch_name= Entry(self.bottom, width= "60")
     e_branch_name.place(x=320, y=110)

     t= StringVar()
     Radiobutton(self.bottom, text="Savings Account",  value="Savings", bg="#33E9FF", variable=t).place(x=320, y=140)
     Radiobutton(self.bottom, text="Checking Account",  value="Checking", bg="#33E9FF", variable=t).place(x=450, y=140)

     e_balance= Entry(self.bottom, width= "60")
     e_balance.place(x=320, y=170)

     e_cust_SSN=Entry(self.bottom, width= "60")
     e_cust_SSN.place(x=320, y=200)
     
     e_emp_SSN= Entry(self.bottom, width= "60")
     e_emp_SSN.place(x=320, y=230)

     i= StringVar()
     Radiobutton(self.bottom, text="personal banker",  value="personal banker", bg="#33E9FF", variable=i).place(x=320, y=260)
     Radiobutton(self.bottom, text="loan officer",  value="loan officer", bg="#33E9FF", variable=i).place(x=450, y=260)

     e_intrest_rate= Entry(self.bottom, width= "60")
     e_intrest_rate.place(x=320, y=290)
    
     e_overdraft= Entry(self.bottom, width= "60")
     e_overdraft.place(x=320, y=320)
     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="30", command=sub)
     self.submit.place(x=320 , y=360)
     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("900x700+200+0")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
