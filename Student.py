
class Student:
	import Course
	import Team
	import Assignment
	def __init__(self, id, username, publicity):
		self._id = id 				# rcs (unique for each student/professor)
		self._username = username
		self._publicity = publicity
		self._tags = []
		self._courses = []
		self._teams = []

	# GETTERS
	def getID(self):
		# return an int representing the rcs id 
		return self._id

	def getUsername(self):
		# return a string representing the team name
		return self._username

	def getPublicity(self):
		# return True if the individual is set to be public, False otherwise
		return self._publicity

	def getTags(self):
		ret = self._tags.copy()
		return ret

	def getCourses(self):
		# POSSIBLE REPRESENTATION EXPOSURE????
		ret = self._courses.copy()
		return ret

	def getTeams(self):
		ret = self._teams.copy()
		return ret

	# SETTERS
	def setID(self, newID):
		self._id = newID

	def setUsername(self, newUsername):
		self._username = newUsername

	def setPublicity(self, newPublicity):
		self._publicity = newPublicity

	# other methods
	def addCourse(self, newCourse):
		for course in self._courses:
			if course.getCRN() == newCourse.getCRN():
				return False
		self._courses.append(newCourse)
		newCourse.addStudent(self)
		return True

	def removeCourse(self, theCourse):
		for course in self._courses:
			if course.getCRN() == theCourse.getCRN():
				self._courses.remove(theCourse)
				theCourse.removeStudent(self)
				return True
		return False

	def addTag(self, newTag):
		# don't allow duplicated tags
		for tag in self._tags:
			if tag == newTag:
				return False
		self._tags.append(newTag)
		return True

	def deleteTag(self, theTag):
		# only delete when exists
		for tag in self._tags:
			if tag == theTag:
				self._tags.remove(theTag)
				return True
		return False

	def addTeam(self, newTeam):
		for team in self._teams:
			if team.getID() == newTeam.getID():
				return False
		self._teams.append(newTeam)
		newTeam.addMember(self)
		return True

	def removeTeam(self, theTeam):
		for team in self._teams:
			if team.getID() == theTeam.getID():
				self._teams.remove(theTeam)
				theTeam.removeMember(self)
				return True
		return False

	def createTeam(self):
		# to be implemented
		print("")

	def inviteTeam(self):
		# to be implemented
		print("")

	def applyTeam(self):
		# to be implemented
		print("")

	def acceptTeam(self):
		# to be implemented
		print("")

	def declineTeam(self):
		# to be implemented
		print("")

	def teamSearch(self):
		# to be implemented
		print("")

	def studentSearch(self):
		# to be implemented
		print("")






# if __name__ == '__main__':
#     L1 = Student(1, "L1", True)
#     print(L1.getID())
#     print(L1.getUsername())
#     print(L1.getPublicity())