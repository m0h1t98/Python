from tkinter import *
from tkinter.ttk import *
import pymysql.cursors
import sys 
import random
import datetime

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='FlightDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



cursor = connection.cursor()

t1='';t2='';



 
root=Tk()
root.title("Flight Regestration")
#app = Window(root)
root.geometry('500x500')

lbl = Label(root, text="Book Fight", font=("Arial Bold", 15))
lbl.grid(column=8, row=1,pady=40,padx=40)

lblFID = Label(root, text="Fight ID", font=("Arial Bold", 15))
lblFID.grid(column=6, row=6,padx=40)

#txtFID = Entry(root,width=30)
#txtFID.grid(column=8, row=6,padx=40)

cursor.execute("SELECT FlightID FROM flightreg")
Fresult = cursor.fetchall()
arr=[]
for d in Fresult:
  arr.append(d['FlightID'])
comboFID = Combobox(root)
comboFID['values']= arr
comboFID.current(1)
comboFID.grid(column=8, row=6,padx=40)

lblDate = Label(root, text="Date", font=("Arial Bold", 15))
lblDate.grid(column=6, row=9,padx=40)

txtDate = Entry(root,width=30)
txtDate.grid(column=8, row=9,padx=40)

lblSeats = Label(root, text="Seats", font=("Arial Bold", 15))
lblSeats.grid(column=6, row=12,padx=40)

txtSeats = Entry(root,width=30)
txtSeats.grid(column=8, row=12,padx=40)

lblCID = Label(root, text="Cust ID", font=("Arial Bold", 15))
lblCID.grid(column=6, row=15,padx=40)

txtCID = Entry(root,width=30)
txtCID.grid(column=8, row=15,padx=40)


lblCN = Label(root, text="Cust Name", font=("Arial Bold", 15))
lblCN.grid(column=6, row=18,padx=40)

txtCN = Entry(root,width=30)
txtCN.grid(column=8, row=18,padx=40)

lblMsg = Label(root, text="", font=("Arial Bold", 15))
lblMsg.grid(column=8, row=27,padx=30,pady=40)


def SaveData():
      
      try:
          
          # Create a new record
          t1=comboFID.get();t2=txtDate.get();t3=txtSeats.get();t4=txtCID.get();t5=txtCN.get();
          if (t1=='' or t2=='' or t3=='' or t4=='' or t5==''):
                lblMsg.configure(text="Please Fill All the field")
                return
                

          '''
          cursor.execute("SELECT * FROM flightreg where FlightID='"+t1+"'")
          chkresult = cursor.fetchall()
          number_of_rows=cursor.rowcount #chkresult[0]
          print(number_of_rows,t1)

          if  number_of_rows>0:
                lblMsg.configure(text="Sorry! ID already exist.")
                print('Sorry')
                return
          '''      
          BID='B'+str(random.randint(1000,9999))+t1[4:]
          

          now = datetime.datetime.now()
          bdate=str(now.year)+'-'+str(now.month).rjust(2, ' ')+'-'+str(now.day).rjust(2, ' ')
          sql = "INSERT INTO Fbooktab (BookID,FlightID,bdate,JourneyDate,Seats,CustID,CustName) VALUES ('"+BID+"','"+t1+"','"+bdate+"','"+t2+"','"+t3+"','"+t4+"','"+t5+"')"
          
          
          print(sql)
          #cursor = connection.cursor()
          cursor.execute(sql)
          connection.commit()
          
          print('successfully Added')
      except:
            print("Oops! an Error occured.",sys.exc_info()[0],sys.exc_info()[1])
            connection.rollback()
      finally:
            connection.close()

btn = Button(root, text=" Save ",width=10, bg="orange", fg="red",command=SaveData,bd=5)
#btn = Button(root, text="Save", bg="orange", fg="red",command=lambda i=t1: SaveData(i),bd=5)

btn.grid(column=8, row=23,pady=30)


mainloop()
