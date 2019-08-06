from tkinter import *
import pymysql.cursors
import sys 
from FlightRegM import *
from FlightBookingM import *
from SearchFlightM import *
from FlightAvM import *
from FlightBookDetM import *

root=Tk()
root.title("Flight Regestration")
#app = Window(root)
root.geometry('500x500')


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def reg():
      top1 = Toplevel()
      FlightRegWindow(top1, "460", "460")
def book():
      top2 = Toplevel()
      FlightBookingWindow(top2, "460", "460")

def searchFlight():
      top3 = Toplevel()
      SearchFlightWindow(top3, "460", "460")
def FlightAv():
      top4 = Toplevel()
      FlightAvWindow(top4, "460", "460")
def bookDetail():
      top5 = Toplevel()
      BookDetWindow(top5, "490", "490")
      
#menu
menubar = Menu(root)

Fregmenu = Menu(menubar, tearoff=0)
Fregmenu.add_command(label="FlightMaster", command=reg)
#filemenu.add_separator()
#filemenu.add_command(label="Open", command=donothing)

Fbookmenu = Menu(menubar, tearoff=0)
Fbookmenu.add_command(label="Book Flight", command=book)
Fbookmenu.add_command(label="Book Detail", command=bookDetail)

FSearchmenu = Menu(menubar, tearoff=0)
FSearchmenu.add_command(label="Search Flight", command=searchFlight)


FSearchmenu.add_command(label="Flight Avilability", command=FlightAv)

Fexitmenu = Menu(menubar, tearoff=0)
Fexitmenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Flight", menu=Fregmenu)
menubar.add_cascade(label="Booking", menu=Fbookmenu)
menubar.add_cascade(label="Searching", menu=FSearchmenu)

menubar.add_cascade(label="Exit Window", menu=Fexitmenu)

root.config(menu=menubar)

root.mainloop()
