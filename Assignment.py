
class Assignment:
	def __init__(self, title, min, max, deadline, students):
		self.title = title
		self.min = min
		self.max = max
		self.deadline = deadline
		self.teams = []
		self.remainStudents = []
		self.remainStudents.extend(students)

	# GETTERS
	def getTitle(self):
		# return a string representing the title of the assignment
		return self.title

	def getMin(self):
		# return an int representing the minimum number of students in a team
		return self.min

	def getMax(self):
		# return an int representing the maximum number of students in a team
		return self.max

	def getDeadline(self):
		# return an integer representing the deadline 
		# MM(month)DD(day)YYYY(year)HH(hour)MM(min)
		return self.deadline

	# SETTERS
	def setTitle(self, newTitle):
		self.title = newTitle

	def setMin(self, newMin):
		self.subject = newMin

	def setMax(self, newMax):
		self.Max = newMax

	def setDeadline(self, newDeadline):
		self.deadline = newDeadline


	# other methods
	def addTeam(self, newTeam):
		self.teams.append(newTeam)

	def deleteTeam(self, id):
		for team in self.teams:
			if team.id == id:
				self.teams.remove(team)
				return True
		return False

	def searchTeam(self, tags):
		# to be implemented
		print("")

	def searchStudent(self, tags):
		# to be implemented
		print("")
