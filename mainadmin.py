from tkinter import *
import datetime
import os
from subprocess import call
def create_bank():
    call(["python3", "create_bank.py"])
def create_branch():
    call(["python3", "create_branch.py"])
def create_emp():
    call(["python3", "create_emp.py"])
def create_cust():
    call(["python3", "create_cust.py"])
def create_acc():
    call(["python3", "create_acc.py"])
def create_loan():
    call(["python3", "create_loan.py"])   
def loan_pay():
    call(["python3", "loan_pay.py"])      

date = datetime.datetime.now().date()
date= str(date)



class Appli(object):
  def __init__(self, master):
     self.master=master

     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=600, bg="#33E9FF")
     self.bottom.pack(fill=X)

     #top Frame design

     self.heading= Label(self.top, text="Bank Enterprise", font="arial 15 bold", bg="white")
     self.heading.place(x= 180, y=50)

     self.date_lbl = Label(self.bottom, text="Date : "+date, bg="#33E9FF")
     self.date_lbl.place(x=500, y=20)

     #buttons

     #Createbank
     self.ca= Button(self.bottom, text=" Create Bank ", font="arial 13 bold", command=create_bank, width=20)
     self.ca.place(x=40, y=20)
     self.ca_lbl = Label(self.bottom, text=">Create new Bank", bg="#33E9FF", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=20)
    
    #CreateBranch
     self.ca= Button(self.bottom, text=" Create Branch ", font="arial 13 bold", command=create_branch, width=20)
     self.ca.place(x=40, y=60)
     self.ca_lbl = Label(self.bottom, text=">Create new Branch", bg="#33E9FF", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=60)

     #CreateEmployee
     self.ca= Button(self.bottom, text=" Create Employee ", font="arial 13 bold", command=create_emp, width=20)
     self.ca.place(x=40, y=100)
     self.ca_lbl = Label(self.bottom, text=">Create new Employee", bg="#33E9FF", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=100)

     #Createcustomer
     self.Be= Button(self.bottom, text=" Add customer ", font="arial 13 bold", command=create_cust, width=20)
     self.Be.place(x=40, y=140)
     self.be_lbl = Label(self.bottom, text=">Add New Customer ", bg="#33E9FF", font="arial 13 bold")
     self.be_lbl.place(x=280, y=140)


     #createaccount
     self.ca= Button(self.bottom, text=" Create Account ", font="arial 13 bold", command=create_acc, width=20)
     self.ca.place(x=40, y=180)
     self.ca_lbl = Label(self.bottom, text=">Create Account", bg="#33E9FF", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=180)

    #CreateLoan
     self.ca= Button(self.bottom, text=" Create Loan ", font="arial 13 bold", command=create_loan, width=20)
     self.ca.place(x=40, y=220)
     self.ca_lbl = Label(self.bottom, text=">Create Loan", bg="#33E9FF", font="arial 13 bold")
     self.ca_lbl.place(x=280, y=220)
     #LoanPayment
     self.Be= Button(self.bottom, text=" Loan Payment ", font="arial 13 bold", command=loan_pay, width=20)
     self.Be.place(x=40, y=260)
     self.be_lbl = Label(self.bottom, text=">Pay Loan", bg="#33E9FF", font="arial 13 bold")
     self.be_lbl.place(x=280, y=260)




def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x700+100+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
