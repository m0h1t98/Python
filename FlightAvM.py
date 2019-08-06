from tkinter import *
from tkinter.ttk import *
import pymysql.cursors
import sys
from DBConnection import *
from FlightFuns import *
from ListFlightWin import *

class FlightAvWindow():
    def __init__(self, master, width, height):

            self.master = master
            self.master.geometry("%sx%s+100+100" % (width, height))
            self.master.title("Toplevel Window")

            lbl = Label(self.master, text="Check Seats Avilability", font=("Arial Bold", 15))
            lbl.grid(column=8, row=1,pady=40,padx=40)

            lblFID = Label(self.master, text="Fight ID", font=("Arial Bold", 15))
            lblFID.grid(column=6, row=6,padx=20,sticky="w")

            comboFID = Combobox(self.master)
            comboFID['values']= getFlights()
            comboFID.current(1)
            comboFID.grid(column=8, row=6,padx=40,sticky="w")

            
            lblDate = Label(self.master, text="Journey Date", font=("Arial Bold", 15))
            lblDate.grid(column=6, row=9,padx=20,sticky="w")

            txtDate = Entry(self.master,width=30)
            txtDate.grid(column=8, row=9,padx=40,sticky="w")

            

            lblMsg = Label(self.master, text="", font=("Arial Bold", 15))
            lblMsg.grid(column=8, row=14,padx=30,pady=40)


            def ChkAvData():
                  
                  try:
                      
                        # Create a new record
                        t1=comboFID.get();t2=txtDate.get();
                        
                        if (t1=='' or t2==''  ):
                            lblMsg.configure(text="Please Fill All the field")
                            return
                            
                        
                        sql="SELECT * FROM seatsummary where FlightID='"+t1+"' and JourneyDate='"+t2+"'"
                        connection=GetDBCursor()
                        cursor=connection.cursor()

                        cursor.execute(sql)
                        chkresult = cursor.fetchall()
                        number_of_rows=cursor.rowcount 
                        print(number_of_rows,t1)
                        total=0;av=0;
                        if  number_of_rows>0:
                              
                              for x in chkresult:
                                    print(x)
                                    total=x['SeatCap']
                                    av=x['AvSeats']
                                                         
                              lblMsg.configure(text="Avilable Seats : "+str(av)+" \n Cap :"+str(total))
                        else:
                              cursor.execute("SELECT SeatCap FROM FlightReg where FlightID='"+t1+"'")
                              chkresult = cursor.fetchall()
                              for x in chkresult:
                                    print(x)
                                    total=x['SeatCap']
                                    av=total
                              lblMsg.configure(text="Avilable Seats : "+str(av)+" \n Cap :"+str(total))
                            
                        

                        print('successfully Showed Av')
                  except:
                        print("Oops! an Error occured.",sys.exc_info()[0],sys.exc_info()[1])
                        #connection.rollback()
            

            btn = Button(self.master, text=" Save ",width=10, command=ChkAvData)
            

            btn.grid(column=8, row=26,pady=30)
