from tkinter import *
import pymysql.cursors
import sys
from DBConnection import *

class FlightRegWindow():
    def __init__(self, master, width, height):

            self.master = master
            self.master.geometry("%sx%s+100+100" % (width, height))
            self.master.title("Toplevel Window")

            lbl = Label(self.master, text="Register Fight", font=("Arial Bold", 15))
            lbl.grid(column=8, row=1,pady=40,padx=40)

            lblFID = Label(self.master, text="Fight ID", font=("Arial Bold", 15))
            lblFID.grid(column=6, row=6,padx=20,sticky="w")

            txtFID = Entry(self.master,width=30)
            txtFID.grid(column=8, row=6,padx=40)

            lblFrom = Label(self.master, text="From", font=("Arial Bold", 15))
            lblFrom.grid(column=6, row=9,padx=20,sticky="w")

            txtFrom = Entry(self.master,width=30)
            txtFrom.grid(column=8, row=9,padx=40)

            lblTo = Label(self.master, text="To", font=("Arial Bold", 15))
            lblTo.grid(column=6, row=12,padx=20,sticky="w")

            txtTo = Entry(self.master,width=30)
            txtTo.grid(column=8, row=12,padx=40)

            lblSC = Label(self.master, text="Seat Capacity", font=("Arial Bold", 15))
            lblSC.grid(column=6, row=15,padx=20,sticky="w")

            txtSC = Entry(self.master,width=30)
            txtSC.grid(column=8, row=15,padx=40)

            lblSCH = Label(self.master, text="Flight Schedule", font=("Arial Bold", 15))
            lblSCH.grid(column=6, row=18,padx=20,sticky="w")

            txtSCH = Entry(self.master,width=30)
            txtSCH.grid(column=8, row=18,padx=40)

            lblMsg = Label(self.master, text="", font=("Arial Bold", 15))
            lblMsg.grid(column=8, row=22,padx=30,pady=40)


            def SaveData():
                  
                  try:
                      
                        # Create a new record
                        t1=txtFID.get();t2=txtFrom.get();
                        t3=txtTo.get();t4=txtSC.get();t5=txtSCH.get();
                        if (t1=='' or t2=='' or t3=='' or t4==''):
                            lblMsg.configure(text="Please Fill All the field")
                            return
                            
                        connection=GetDBCursor()
                        cursor=connection.cursor()

                        cursor.execute("SELECT * FROM flightreg where FlightID='"+t1+"'")
                        chkresult = cursor.fetchall()
                        number_of_rows=cursor.rowcount #chkresult[0]
                        print(number_of_rows,t1)

                        if  number_of_rows>0:
                            lblMsg.configure(text="Sorry! ID already exist.")
                            print('Sorry')
                            return
                            
                        sql = "INSERT INTO FlightReg (FlightID,FBoard,FDest,SeatCap,Schedule) VALUES ('"+t1+"','"+t2+"','"+t3+"',"+t4+",'"+t5+"')"


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

            btn = Button(self.master, text=" Save ",width=10, bg="orange", fg="red",command=SaveData,bd=5)
            #btn = Button(root, text="Save", bg="orange", fg="red",command=lambda i=t1: SaveData(i),bd=5)

            btn.grid(column=8, row=26,pady=30)
