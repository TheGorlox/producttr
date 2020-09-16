from datetime import date, datetime
class Workday:
	# __animal_type
	# __mood
	# __name
	def __init__(self):
		self.__activity_list=[]
		self.__date = datetime.today()
	
	def update(self,Aname):
		present=False
		for a in self.__activity_list:
			if a.get_name()==Aname:
				present = True
		if present==False:
			self.__activity_list.append(activity(Aname))
	def get_date(self):
		return self.__date
	def get_activities(self):
		return self.__activity_list

class activity:
	def __init__(self,Aname):
		self.__name = Aname
		# self.__start_time
		# self.__tot_time
	def get_name(self):
		return self.__name
