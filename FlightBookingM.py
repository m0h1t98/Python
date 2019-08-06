from tkinter import *
from tkinter.ttk import *
import pymysql.cursors
import sys 
import random
import datetime
from DBConnection import *
from FlightFuns import *



class FlightBookingWindow():
  def __init__(self, master, width, height):

    self.master = master
    self.master.geometry("%sx%s+100+100" % (width, height))
    self.master.title("Book The Flight")

    connection=GetDBCursor()
    cursor=connection.cursor()

    lbl = Label(self.master, text="Book Fight", font=("Arial Bold", 15))
    lbl.grid(column=8, row=1,pady=40,padx=40)

    lblFID = Label(self.master, text="Fight ID", font=("Arial Bold", 15))
    lblFID.grid(column=6, row=6,padx=40,sticky="w")

    
    comboFID = Combobox(self.master)
    comboFID['values']= getFlights()
    comboFID.current(1)
    comboFID.grid(column=8, row=6,padx=40,sticky="w")

    lblDate = Label(self.master, text="Date", font=("Arial Bold", 15))
    lblDate.grid(column=6, row=9,padx=40,sticky="w")

    txtDate = Entry(self.master,width=30)
    txtDate.grid(column=8, row=9,padx=40)

    lblSeats = Label(self.master, text="Seats", font=("Arial Bold", 15))
    lblSeats.grid(column=6, row=12,padx=40,sticky="w")

    txtSeats = Entry(self.master,width=30)
    txtSeats.grid(column=8, row=12,padx=40)

    lblCID = Label(self.master, text="Cust ID", font=("Arial Bold", 15))
    lblCID.grid(column=6, row=15,padx=40,sticky="w")

    txtCID = Entry(self.master,width=30)
    txtCID.grid(column=8, row=15,padx=40)


    lblCN = Label(self.master, text="Cust Name", font=("Arial Bold", 15))
    lblCN.grid(column=6, row=18,padx=40,sticky="w")

    txtCN = Entry(self.master,width=30)
    txtCN.grid(column=8, row=18,padx=40)

    lblMsg = Label(self.master, text="", font=("Arial Bold", 15))
    lblMsg.grid(column=8, row=27,padx=30,pady=40)


    def SaveData2():
      try:
        # Create a new record
        t1=comboFID.get();t2=txtDate.get();t3=txtSeats.get();t4=txtCID.get();t5=txtCN.get();
        if (t1=='' or t2=='' or t3=='' or t4=='' or t5==''):
              lblMsg.configure(text="Please Fill All the field")
              return
              

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

    btn2 = Button(self.master, text=" Save ",width=10,  command=SaveData2)
    

    btn2.grid(column=8, row=23,pady=30)

