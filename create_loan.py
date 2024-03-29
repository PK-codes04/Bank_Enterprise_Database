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
         loan_no= DoubleVar()
         amount= DoubleVar()
         loan_no = (e_loan_no.get())
         bank_id = (e_bank_id.get())
         branch_name = (e_branch_name.get())
         cust_SSN= (e_cust_SSN.get())
         loan_type = (t.get())
         amount = (e_amount.get())
         emp_SSN = (e_emp_SSN.get())
         end_date = (e_end_date.get())
         start_date = (e_start_date.get())
         b_type = (i.get())

         if (loan_no == "" or bank_id == "" or branch_name == "" or loan_type =="" or amount =="" or cust_SSN == "" or emp_SSN ==""or start_date == "" or end_date ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             query ="INSERT INTO loan(bank_id,branch_name,loan_no,amount,loan_type,start_date,end_date) VALUES (%s,'%s',%s,%s,'%s','%s','%s')" % (bank_id,branch_name,loan_no,amount,loan_type,start_date,end_date)
             cursor.execute(query)
             cursor.execute("commit")
             query ="INSERT INTO cust_banker(cust_SSN,emp_SSN,b_type) VALUES (%s,%s,'%s')" % (cust_SSN,emp_SSN,b_type)
             cursor.execute(query)
             cursor.execute("commit")
             query ="INSERT INTO borrower(cust_SSN,loan_no) VALUES (%s,%s)" % (cust_SSN,loan_no)
             cursor.execute(query)
             cursor.execute("commit")
             MessageBox.showinfo("Insert Status", "Inserted Successfully")
             con.close()


     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)
     self.bottom= Frame(master, height=1000, bg="#33E9FF")

     self.bottom.pack(fill=X)

     self.heading= Label(self.top, text="Create Loan", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=20)

     #bottom Frame Design

     #buttons and lables
     loan_no= DoubleVar()
     loan_no = Label(self.bottom, text="Loan number ", font="arial 14 bold", bg="#33E9FF")
     loan_no.place(x=40, y=50)

     bank_id = Label(self.bottom, text="Bank Id ", font="arial 14 bold", bg="#33E9FF")
     bank_id.place(x=40, y=80)

     branch_name = Label(self.bottom, text="Branch Name ", font="arial 14 bold", bg="#33E9FF")
     branch_name.place(x=40, y=110)

     loan_type = Label(self.bottom, text="Loan Type ", font="arial 14 bold", bg="#33E9FF")
     loan_type.place(x=40, y=140)

     amount= DoubleVar()
     amount = Label(self.bottom, text="Loan Amount ", font="arial 14 bold", bg="#33E9FF")
     amount.place(x=40, y=170)

     cust_SSN = Label(self.bottom, text="Customer SSN ", font="arial 14 bold", bg="#33E9FF")
     cust_SSN.place(x=40, y=200)
     
     emp_SSN = Label(self.bottom, text="Employee SSN ", font="arial 14 bold", bg="#33E9FF")
     emp_SSN.place(x=40, y=230)

     loan_type = Label(self.bottom, text="Banker Type ", font="arial 14 bold", bg="#33E9FF")
     loan_type.place(x=40, y=260)

     start_date = Label(self.bottom, text="Loan Start Date", font="arial 14 bold", bg="#33E9FF")
     start_date.place(x=40, y=290)

     end_date = Label(self.bottom, text="Loan End Date ", font="arial 14 bold", bg="#33E9FF")
     end_date.place(x=40, y=320)

     #Enteries
     
     e_loan_no= Entry(self.bottom, width= "60", textvariable=loan_no)
     e_loan_no.place(x=320, y=50)

     e_bank_id= Entry(self.bottom, width= "60")
     e_bank_id.place(x=320, y=80)

     e_branch_name= Entry(self.bottom, width= "60")
     e_branch_name.place(x=320, y=110)

     t= StringVar()
     Radiobutton(self.bottom, text="Home",  value="Home", bg="#33E9FF", variable=t).place(x=320, y=140)
     Radiobutton(self.bottom, text="Personal",  value="Personal", bg="#33E9FF", variable=t).place(x=450, y=140)
     Radiobutton(self.bottom, text="Credit Card",  value="Credit Card", bg="#33E9FF", variable=t).place(x=580, y=140)

     e_amount= Entry(self.bottom, width= "60")
     e_amount.place(x=320, y=170)

     e_cust_SSN=Entry(self.bottom, width= "60")
     e_cust_SSN.place(x=320, y=200)
     
     e_emp_SSN= Entry(self.bottom, width= "60")
     e_emp_SSN.place(x=320, y=230)

     i= StringVar()
     Radiobutton(self.bottom, text="personal banker",  value="personal banker", bg="#33E9FF", variable=i).place(x=320, y=260)
     Radiobutton(self.bottom, text="loan officer",  value="loan officer", bg="#33E9FF", variable=i).place(x=430, y=260)

     e_start_date= Entry(self.bottom, width= "60")
     e_start_date.place(x=320, y=290)
    
     e_end_date= Entry(self.bottom, width= "60")
     e_end_date.place(x=320, y=320)
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
