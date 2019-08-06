from tkinter import *
import pymysql.cursors
import sys 


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

lbl = Label(root, text="Register Fight", font=("Arial Bold", 15))
lbl.grid(column=8, row=1,pady=40,padx=40)

lblFID = Label(root, text="Fight ID", font=("Arial Bold", 15))
lblFID.grid(column=6, row=6,padx=40)

txtFID = Entry(root,width=30)
txtFID.grid(column=8, row=6,padx=40)

lblFrom = Label(root, text="From", font=("Arial Bold", 15))
lblFrom.grid(column=6, row=9,padx=40)

txtFrom = Entry(root,width=30)
txtFrom.grid(column=8, row=9,padx=40)

lblTo = Label(root, text="To", font=("Arial Bold", 15))
lblTo.grid(column=6, row=12,padx=40)

txtTo = Entry(root,width=30)
txtTo.grid(column=8, row=12,padx=40)

lblSC = Label(root, text="Seat Capacity", font=("Arial Bold", 15))
lblSC.grid(column=6, row=15,padx=40)

txtSC = Entry(root,width=30)
txtSC.grid(column=8, row=15,padx=40)

lblMsg = Label(root, text="", font=("Arial Bold", 15))
lblMsg.grid(column=8, row=20,padx=30,pady=40)


def SaveData():
      
      try:
          
          # Create a new record
          t1=txtFID.get();t2=txtFrom.get();t3=txtTo.get();t4=txtSC.get();
          if (t1=='' or t2=='' or t3=='' or t4==''):
                lblMsg.configure(text="Please Fill All the field")
                return
                

          
          cursor.execute("SELECT * FROM flightreg where FlightID='"+t1+"'")
          chkresult = cursor.fetchall()
          number_of_rows=cursor.rowcount #chkresult[0]
          print(number_of_rows,t1)

          if  number_of_rows>0:
                lblMsg.configure(text="Sorry! ID already exist.")
                print('Sorry')
                return
                
          sql = "INSERT INTO FlightReg (FlightID,FBoard,FDest,SeatCap) VALUES ('"+t1+"','"+t2+"','"+t3+"',"+t4+")"
          
          
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

btn.grid(column=8, row=18,pady=30)


mainloop()
