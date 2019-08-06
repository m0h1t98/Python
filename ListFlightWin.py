from DBConnection import *
from tkinter import *
from tkinter.ttk import *
from functools import partial

class ListFlight:
      def __init__(self,str):
            
            self._root = Tk()
            self._root.title('List of Results')
            tv = Treeview(self._root)
            tv.pack()
            tv.heading('#0', text='ID')
            tv.configure(column=('#FlightID', '#FBoard', '#FDest','#Schedule'))
            tv.heading('#FlightID', text='Flight')
            tv.heading('#FBoard', text='Boarding')
            tv.heading('#FDest', text='Destination')
            tv.heading('#Schedule', text='Schedule')
            
            
            connection=GetDBCursor()
            cursor=connection.cursor()
            cursor.execute(str)

            def getSeat(id):
                  print(id)
            cnt=1
            for row in cursor:
                  tv.insert('', 'end', '#{}'.format(row['FlightID']),text=cnt)
                  tv.set('#{}'.format(row['FlightID']),'#FlightID',row['FlightID'])
                  tv.set('#{}'.format(row['FlightID']),'#FBoard',row['FBoard'])
                  tv.set('#{}'.format(row['FlightID']),'#FDest',row['FDest'])
                  tv.set('#{}'.format(row['FlightID']),'#Schedule',row['Schedule'])
                  cnt+=1
            
			
