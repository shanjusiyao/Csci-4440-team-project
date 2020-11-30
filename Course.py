
class Course:
	import Student
	import Professor
	import Assignment
	import Team
	def __init__(self, crn, subject, section, size):
		self.CRN = crn
		self.subject = subject
		self.section = section
		self.size = size
		self.students = []
		self.professors = []
		self.assignments = []
		self.previousTeams = []

	# GETTERS
	def getCRN(self):
		# return a 5 digit integer representing the course registration number
		return self.CRN

	def getSubject(self):
		# return a string in the form XXXX-####
		return self.subject

	def getSection(self):
		# return an integer representing the section number
		return self.section

	def getSize(self):
		# return an integer representing the course size
		return self.size

	def getStudents(self):
		# POSSIBLE REPRESENTATION EXPOSURE???
		return self.students

	def getProfessors(self):
		# POSSIBLE REPRESENTATION EXPOSURE???
		return self.professors

	def getAssignments(self):
		# POSSIBLE REPRESENTATION EXPOSURE???
		return self.assignments

	def getPreviousTeams(self):
		# POSSIBLE REPRESENTATION EXPOSURE???
		return self.previousTeams

	# SETTERS
	def setCRN(self, newCRN):
		self.CRN = newCRN

	def setSubject(self, newSubject):
		self.subject = newSubject

	def setSection(self, newSection):
		self.Section = newSection

	def setSize(self, newSize):
		self.size = newSize

	# other methods
	def addStudent(self, newStudent):
		# if already in the course
		for student in self.students:
			if student.id == newStudent.id:
				return False
		self.students.append(newStudent)
		return True

	def addProfessor(self, newProfessor):
		# if already in the course
		for prof in self.professors:
			if prof.id == newProfessor.id:
				return False
		self.professors.append(newProfessor)
		return True

	def addAssignment(self, newAssignment):
		# if invalid duplicated title
		for assign in self.assignments:
			if assign.title == newAssignment.title:
				return False
		self.assignments.append(newAssignment)
		return True

	def removeStudent(self, id):
		# if student's in the course
		for student in self.students:
			if student.id == id:
				self.students.remove(student)
				return True
		return False

	def removeProfessor(self, id):
		# if student's in the course
		for prof in self.professors:
			if prof.getID() == id:
				self.professors.remove(prof)
				return True
		return False

	def deleteAssignment(self, assignment):
		for assign in self.assignments:
			if assign == assignment:
				self.assignments.remove(assign)
				return True
		return False

# if __name__ == '__main__':
# 	public = True
#     L1 = Student(1, "L1", private)

