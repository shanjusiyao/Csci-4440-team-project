import Course
import Assignment
class Professor:
	def __init__(self, id):
		self._id = id 		# rcs (unique for each student/professor)
		self._courses = []

	# GETTERS
	def getID(self):
		# return an int representing the rcs id
		return self._id

	def getCourses(self):
		# POSSIBLE REPRESENTATION EXPOSURE????
		ret = self._courses.copy()
		return ret

	# SETTERS
	def setID(self, newID):
		self._id = newID

	# other methods
	def addCourse(self, newCourse):
		# if already in the list
		for course in self._courses:
			if course.getCRN() == newCourse.getCRN():
				return False
		# bi-directional adds
		self._courses.append(newCourse)
		newCourse.addProfessor(self)
		return True

	def removeCourse(self, theCourse):
		# remove if in the list
		for course in self._courses:
			if course.getCRN() == theCourse.getCRN():
				# bi-directional removes
				self._courses.remove(theCourse)
				theCourse.removeProfessor(self._id)
				return True
		return False

	def addStudentTag(self, student, tag):
		return student.addTag(tag)

	def deleteStudentTag(self, student, tag):
		return student.deleteTag(tag)

	def addTeamTag(self, team, tag):
		return team.addTag(tag)

	def deleteTeamTag(self, team, tag):
		return team.deleteTag(tag)

	def addStudentToTeam(self, team, student):
		return student.addTeam(team)

	def removeStudentFromTeam(self, team, student):
		return student.removeTeam(team)

	def addAssignment(self, course, title, min, max, deadline):
		newAssign = Assignment.Assignment(title, min, max, deadline, course.getStudents())
		return course.addAssignment(newAssign)

	def editAssignment(self, assignment, title, min, max, deadline):
		if assignment != None:
			if title != None:
				assignment.setTitle(title)
			if min != None:
				assignment.setMin(min)
			if max != None:
				assignment.setMax(max)
			if deadline != None:
				assignment.setDeadline(deadline)
			return True
		return False

	def deleteAssignment(self, course, assignment):
		return course.deleteAssignment(assignment)


# if __name__ == '__main__':
#     P1 = Professor("golds")
#     print(P1.getID())