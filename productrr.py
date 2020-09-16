from win32gui import GetWindowText, GetForegroundWindow
import os, time
import Workday
from datetime import datetime, date

now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
session = Workday.Workday()
dt_string = now.strftime("%m/%d/%Y %H:%M")
# print("date and time =", dt_string)	
clear = lambda: os.system('cls')
prevwind = 'null'
starttime = time.time()
def updateconsole(arr):
	clear()
	print("session: ", session.get_date().strftime("%m/%d/%Y %H:%M"))
	session.update(prevwind)
	for a in session.get_activities():
		print(a.get_name())


while True:

	if prevwind ==GetWindowText(GetForegroundWindow()):
		pass
	else:
		
		prevwind = GetWindowText(GetForegroundWindow())
		updateconsole([starttime,prevwind])
		
	
