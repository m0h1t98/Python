
import pymysql.cursors
import sys 
from DBConnection import *

def getFlights():
      connection=GetDBCursor()
      cursor=connection.cursor()
      cursor.execute("SELECT FlightID FROM flightreg")
      Fresult = cursor.fetchall()
      arr=[]
      for d in Fresult:
            arr.append(d['FlightID'])
      return arr
def getCity():
      connection=GetDBCursor()
      cursor=connection.cursor()
      cursor.execute("SELECT FBoard FROM flightreg")
      Fresult = cursor.fetchall()
      arr=[]
      for d in Fresult:
            arr.append(d['FBoard'])
      return arr
