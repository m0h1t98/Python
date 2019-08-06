from tkinter import *
from tkinter.ttk import *
import pymysql.cursors
import sys
from DBConnection import *
from FlightFuns import *
from ListFlightWin import *

class SearchFlightWindow():
    def __init__(self, master, width, height):

            self.master = master
            self.master.geometry("%sx%s+100+100" % (width, height))
            self.master.title("Toplevel Window")

            lbl = Label(self.master, text="Search Fight", font=("Arial Bold", 15))
            lbl.grid(column=8, row=1,pady=40,padx=40)

            lblFID = Label(self.master, text="Fight From", font=("Arial Bold", 15))
            lblFID.grid(column=6, row=6,padx=20,sticky="w")

            comboFIDFrm = Combobox(self.master)
            comboFIDFrm['values']= getCity()
            comboFIDFrm.current(1)
            comboFIDFrm.grid(column=8, row=6,padx=40,sticky="w")

            lblFrom = Label(self.master, text="Flight To", font=("Arial Bold", 15))
            lblFrom.grid(column=6, row=9,padx=20,sticky="w")

            comboFIDTo = Combobox(self.master)
            comboFIDTo['values']= getCity()
            comboFIDTo.current(1)
            comboFIDTo.grid(column=8, row=9,padx=40,sticky="w")

            lblDate = Label(self.master, text="Journey Date", font=("Arial Bold", 15))
            lblDate.grid(column=6, row=12,padx=20,sticky="w")

            txtDate = Entry(self.master,width=30)
            txtDate.grid(column=8, row=12,padx=40)

            

            lblMsg = Label(self.master, text="", font=("Arial Bold", 15))
            lblMsg.grid(column=8, row=22,padx=30,pady=40)


            def SearchData():
                  
                  try:
                      
                        # Create a new record
                        t1=comboFIDFrm.get();t2=comboFIDTo.get();
                        t3=txtDate.get();
                        if (t1=='' or t2=='' or t3=='' ):
                            lblMsg.configure(text="Please Fill All the field")
                            return
                            
                        
                        str="SELECT * FROM flightreg where FBoard='"+t1+"' and FDest='"+t2+"'"
                        ListFlight(str)
                            
                        

                        print('successfully Showed')
                  except:
                        print("Oops! an Error occured.",sys.exc_info()[0],sys.exc_info()[1])
                        #connection.rollback()
            

            btn = Button(self.master, text=" Save ",width=10, command=SearchData)
            

            btn.grid(column=8, row=26,pady=30)
