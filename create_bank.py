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
         bank_name= (e_bank_name.get())
         

         if (bank_id == "" or  bank_name ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "acadmysqldb001p.uta.edu", user="psk7459" , password="Asha123456789", database="psk7459")
             cursor= con.cursor()
             query ="INSERT INTO bank(bank_id,bank_name) VALUES (%s,'%s')" % (bank_id,bank_name)
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

     self.heading= Label(self.top, text="Create Bank", font="arial 18 bold", bg="white")
     self.heading.place(x= 370, y=30)

     #bottom Frame Design 

     #buttons and lables
     
     bank_id = Label(self.bottom, text="Bank Id ", font="arial 14 bold", bg="#33E9FF")
     bank_id.place(x=40, y=55)

     fname = Label(self.bottom, text="Bank Name ", font="arial 14 bold", bg="#33E9FF")
     fname.place(x=40, y=110)

     #Enteries
     
     e_bank_id= Entry(self.bottom, width= "60", textvariable=bank_id)
     e_bank_id.place(x=320, y=55)
     e_bank_name= Entry(self.bottom, width= "60")
     e_bank_name.place(x=320, y=110)
     
     
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
