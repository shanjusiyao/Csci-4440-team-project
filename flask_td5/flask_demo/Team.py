import Student

class Team:
	def __init__(self, name, id, publicity, leader):
		self._name = name
		self._id = id
		self._publicity = publicity # True = public, False = private
		self._members = []
		self._members.append((1, leader))
		self._tags = []


	# GETTERS
	def getName(self):
		# return a string representing the team name
		return self._name

	def getID(self):
		# return an int representing the team id
		return self._id

	def getPublicity(self):
		# return True if team is set to be public, False otherwise
		return self._publicity

	def getLeader(self):
		# POSSIBLE REPRESENTATION EXPOSURE????
		# leader will always be the first in the list
		return (self._members)[0][1]

	def getMembers(self):
		# POSSIBLE REPRESENTATION EXPOSURE????
		ret = []
		for member in self._members:
			ret.append(member[1])
		return ret

	def getTags(self):
		ret = self._tags.copy()
		return ret

	# SETTERS
	def setName(self, newName):
		self._name = newName

	def setPublicity(self, newPub):
		self._publicity = newPub

	# other methods
	def dismiss(self):
		self._members.clear()
		self._tags.clear()

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

	def addMember(self, newMember):
		# if already exists as a team member
		for member in self._members:
			if member[1].getID() == newMember.getID():
				return False
		self._members.append((0, newMember))
		return True

	def removeMember(self, theMember):
		# only remove if theMembr exists as a member
		for member in self._members:
			if member[0] == 0 and member[1] == theMember:
				self._members.remove((0, theMember))
				return True
		return False

	def changeLeader(self, newLeader):
		# if newLeader does not exist as a member in the team
		if (0, newLeader) not in self._members:
			return False

		# processing change of position
		for member in self._members:
			if member[0] == 1:
				toMember = (0, member[1])
				self._members.remove(member)
				self._members.append(toMember)
			if member[1] == newLeader:
				toLeader = (1, member[1])
				self._members.remove(member)
				self._members.insert(0, toLeader)
		return True

# if __name__ == '__main__':
#     public = True
#     L1 = Student.Student(1, "L1", public)
#     Team1 = Team( "Team1", 1, public, L1 )
#     print(Team1.getID())
#     print(Team1.getName())
#     print(Team1.getPublicity())
    

