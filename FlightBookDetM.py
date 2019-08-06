from tkinter import *
from tkinter.ttk import *
import pymysql.cursors
import sys
from DBConnection import *
from FlightFuns import *
from ListFlightWin import *

class BookDetWindow():
    def __init__(self, master, width, height):

            self.master = master
            self.master.geometry("%sx%s+100+100" % (width, height))
            self.master.title("Booking Detail")

            lbl = Label(self.master, text="Booking Detail", font=("Arial Bold", 15))
            lbl.grid(column=8, row=1,pady=30,padx=40)

            lblFID = Label(self.master, text="Fight ID", font=("Arial Bold", 15))
            lblFID.grid(column=6, row=6,padx=20,sticky="w")

            comboFID = Combobox(self.master)
            comboFID['values']= getFlights()
            comboFID.current(1)
            comboFID.grid(column=8, row=6,padx=40,sticky="w")

            
            lblDate = Label(self.master, text="Date ", font=("Arial Bold", 15))
            lblDate.grid(column=6, row=9,padx=20,sticky="w")

            txtDate = Entry(self.master,width=30)
            txtDate.grid(column=8, row=9,padx=40,sticky="w")

            listBox= Text(self.master,width = 50)
            listBox.grid(row = 12,column= 1, columnspan = 10,pady=10)

            lblMsg = Label(self.master, text="", font=("Arial Bold", 15))
            lblMsg.grid(column=8, row=14,padx=30,pady=40)


            def VBookData():
                  
                  try:
                      
                        # Create a new record
                        t1=comboFID.get();t2=txtDate.get();
                        
                        if (t1=='' or t2==''  ):
                            lblMsg.configure(text="Please Fill All the field")
                            return
                            
                        
                        sql="SELECT * FROM fbooktab where FlightID='"+t1+"' and JourneyDate='"+t2+"'"
                        connection=GetDBCursor()
                        cursor=connection.cursor()

                        cursor.execute(sql)
                        chkresult = cursor.fetchall()
                        number_of_rows=cursor.rowcount 
                        print(number_of_rows,t1)
                        
                        listBox.insert(END, "Sno \t| CustID \t|Cust_Name\t\t|Seats\t|\n")
                        listBox.insert(END,"-----------------------------------")
                        listBox.insert(END,"\n")
                        if  number_of_rows<=0:
                              listBox.insert(END,' ** No Result Found ** ')
                              return
                                               
                        i=1
                        for row in chkresult:
                              listBox.insert(END,i)
                              listBox.insert(END,"\t|")
                              listBox.insert(END,row['CustID'])
                              listBox.insert(END," \t  |")
                              listBox.insert(END,row['CustName'])
                              listBox.insert(END,"\t\t|")
                              listBox.insert(END,row['Seats'])
                              listBox.insert(END,"\t|")
                              listBox.insert(END,"\n")
                              i=i+1
                              
                              
                            
                        

                        print('successfully Showed Seats')
                  except:
                        print("Oops! an Error occured.",sys.exc_info()[0],sys.exc_info()[1])
                        #connection.rollback()
            

            btn = Button(self.master, text=" Display ",width=10, command=VBookData)
            

            btn.grid(column=10, row=9,padx=20)
