from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master

     def upd():
         loan_no= DoubleVar()
         loan_no = (e_loan_no.get())
         if (loan_no == "" ):
             MessageBox.showinfo("loan_no is required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             cursor.execute("select amount from loan where loan_no='" + loan_no + "'")
             myresul = cursor.fetchall()
             for x in myresul:
                 print(x)
                 fb.insert(0,x)
             cursor.execute("commit")
             MessageBox.showinfo("Update Status", "Payment Successful")
             con.close()




     def dept():
         amtn= dp.get()
         loan_no= DoubleVar()
         loan_no = (e_loan_no.get())        
         con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
         cursor= con.cursor()
         cursor.execute("update loan set amount= amount - ('" + amtn + "') where loan_no='" + loan_no + "'")
         cursor.execute("commit")

         con.close()
         upd()

     
     def sub():
         loan_no= DoubleVar()
         loan_no = (e_loan_no.get())
         amtn= dp.get()

         if (loan_no == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             cursor.execute("select amount from loan where loan_no='" + loan_no + "'")
             myresult = cursor.fetchall()
             for x in myresult:
                 print(x)
                 lb.insert(0,x)
             cursor.execute("commit")
             query ="INSERT INTO payment(loan_no,amount) VALUES (%s,%s)" % (loan_no,amtn)
             cursor.execute(query)
             cursor.execute("commit")
             con.close()
             

             


     #frames

     self.top= Frame(master, height=100 , bg= "white")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#33E9FF")
     self.bottom.pack(fill=X)

     

     self.heading= Label(self.top, text="Loan Payment", font="arial 18 bold", bg="white")
     self.heading.place(x= 265, y=30)

     #bottom Frame Design

     #buttons and lables
     loan_no= DoubleVar()
     loan_no = Label(self.bottom, text="Loan number ", font="arial 14 bold", bg="#33E9FF")
     loan_no.place(x=40, y=55)

     detail = Label(self.bottom, text="Current Balance ", font="arial 14 bold", bg="#33E9FF")
     detail.place(x=40, y=110)

     amt = Label(self.bottom, text="Amount ", font="arial 14 bold", bg="#33E9FF")
     amt.place(x=40, y=165)

     upb = Label(self.bottom, text="Updated Balance ", font="arial 14 bold", bg="#33E9FF")
     upb.place(x=40, y=220)

     #Enteries
     
     e_loan_no= Entry(self.bottom, width= "60", textvariable=loan_no)
     e_loan_no.place(x=320, y=55)

     lb= Entry(self.bottom, width="60" )
     lb.place(x=320 , y= 110)

     dp= Entry(self.bottom, width="60" )
     dp.place(x=320 , y= 165)

     fb= Entry(self.bottom, width="60" )
     fb.place(x=320 , y= 220)





     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="52", command=sub)
     self.submit.place(x=45 , y=270)

     self.dep= Button(self.bottom, text=" Loan Payment ", font="arial 15 bold", width="52", command=dept)
     self.dep.place(x=45 , y=330)

     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
