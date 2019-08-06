
import pymysql.cursors
import sys 

def GetDBCursor():
      connection = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db='FlightDB',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

      return connection
