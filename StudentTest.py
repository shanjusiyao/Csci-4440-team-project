import unittest
from Student import Student
from Course import Course
from Team import Team
from Assignment import Assignment

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.public = True
        self.private = False

        self.Stud1 = Student(1, "Stud1", self.private)
        self.Stud2 = Student(2, "S2", self.private)
        self.T1 = Team( "Team1", 1, self.public, self.L1 )
        self.T2 = Team( "Team2", 2, self.public, self.L2 )

        self.C1 = Course(10000, "CSCI-4440", 1, 75)
        self.C2 = Course(10001, "CSCI-4460", 1, 75)

    # test all getters
    def test_gets(self):
        self.assertEqual(self.Stud1.getID(), "Stud1")
        self.assertEqual(len( self.Stud1.getCourses() ), 0)
        self.assertEqual(self.Stud2.getID(), "S2")
        self.assertEqual(len( self.Stud2.getCourses() ), 0)

    # test all setters
    def test_sets(self):
        self.Stud2.setID("Stud2")
        self.assertEqual(self.Stud2.getID(), "Stud2")
        
    def test_registerAndDropCourses(self):
        # register two courses
        self.assertTrue( self.Stud1.addCourse(self.C1) )
        self.assertTrue( self.Stud1.addCourse(self.C2) )
        self.assertEqual( len( self.Stud1.getCourses() ), 2 )
        self.assertEqual( (self.Stud1.getCourses())[0].getCRN(), 10000 )
        self.assertEqual( (self.Stud1.getCourses())[1].getCRN(), 10001 )
        
        # invalid add
        self.assertFalse( self.Stud1.addCourse(self.C1) )
        self.assertFalse( self.Stud1.addCourse(self.A99) )
        
        # drop one course
        self.assertTrue( self.Stud1.removeCourse(self.C1) )
        self.assertEqual( len( self.Stud1.getCourses() ), 1 )
        self.assertEqual( (self.Stud1.getCourses())[0].getCRN(), 10001 )

        # drop a non-existing course should fail
        self.assertFalse( self.Stud1.removeCourse(self.C1) )

        # drop another course
        self.assertTrue( self.Stud1.removeCourse(self.C2) )
        self.assertEqual( len( self.Stud1.getCourses() ), 0 )
        
    def test_createAndDeleteTeams(self):
        # create two teams
        self.assertTrue( self.Stud1.addTeam(self.T1) )
        self.assertTrue( self.Stud1.addTeam(self.T2) )
        self.assertEqual( len( self.Stud1.getTeams() ), 2 )
        self.assertEqual( (self.Stud1.getTeams())[0].getName(), "Team1" )
        self.assertEqual( (self.Stud1.getTeams())[1].getName(), "Team2" )
        
        # invalid creation
        self.assertFalse( self.Stud1.addTeam(self.T1) )
        
        # delete one team
        self.assertTrue( self.Stud1.removeTeam(self.T1) )
        self.assertEqual( len( self.Stud1.getTeams() ), 1 )
        self.assertEqual( (self.Stud1.getTeams())[0].getName(), "Team1" )
        
        # delete a non-existing team should fail
        self.assertFalse( self.Stud1.removeTeam(self.T1) )
        
        # delete another team
        self.assertTrue( self.Stud1.removeTeam(self.T2) )
        self.assertEqual( len( self.Stud1.getTeams() ), 0 )
        
        
    def test_joinAndLeaveTeams(self):
        self.Stud1.addTeam(self.T1)
        
        # invite another student to the team and the student accept the invitation
        self.assertTrue( self.Stud1.inviteTeam(self.T1, self.Stud2) )
        self.assertTrue( self.Stud2.acceptTeam(self.T1) )
        self.assertEqual( len( self.Stud2.getTeams() ), 1 )
        self.assertEqual( (self.Stud2.getTeams())[0].getName(), "Team1" )
        
        self.Stud2.removeTeam(self.T1)
        # invite another student to the team and the student decline the invitation
        self.assertTrue( self.Stud1.inviteTeam(self.T1, self.Stud2) )
        self.assertTrue( self.Stud2.declineTeam(self.T1) )
        self.assertEqual( len( self.Stud2.getTeams() ), 0 )
        
        # apply for a team and the team leader accept the application
        self.assertTrue( self.Stud2.applyTeam(self.T1) )
        self.assertTrue( self.Stud1.acceptTeam(self.Stud2) )
        self.assertEqual( len( self.Stud2.getTeams() ), 1 )
        self.assertEqual( (self.Stud2.getTeams())[0].getName(), "Team1" )
        
        self.Stud2.removeTeam(self.T1)
        # apply for a team and the team leader decline the application
        self.assertTrue( self.Stud2.applyTeam(self.T1) )
        self.assertTrue( self.Stud1.declineTeam(self.Stud2) )
        self.assertEqual( len( self.Stud2.getTeams() ), 0 )
        
    def test_addAndDeleteTag(self):
        #adds
        self.assertTrue(self.Stud.addTag("Python"))
        self.assertTrue(self.Stud.addTag("Monday"))
        self.assertFalse(self.Stud.addTag("None"))
        self.assertEqual(len(self.Stud.getStudentTag()),2)

        #delete
        self.assertTrue(self.Stud.deleteTag("Python"))
        self.assertFalse(self.Stud.deleteTag("Python"))
        self.assertFalse(self.Stud.deleteTag("Java"))
        self.assertEqual(len(self.Stud.getStudentTag()),1)

        #setPrivateOrPublic
        self.assertEqual(self.Stud.public, True)
        self.setPrivate()
        self.assertEqual(self.Stud.public, False)
        self.setPublic()
        self.assertEqual(self.Stud.public, True)

        #setID
        self.assertFalse(self.Stud.setID(231))
        self.assertTrue(self.Stud.setID(661955587))
        self.assertEqual(self.Stud.getStudentID(),661955587)
        
    def test_StudentTeam(self):
        #create
        self.assertTrue(self.createTeam("Team_A", self.getStudentCourse()[0].assignment[0]))
        self.assertFalse(self.createTeam("SameTeam", self.getStudentCourse()[0].assignment[0]))
        self.assertEqual(self.getStudentTeam()[1], "Team_A")

        #invite
        self.assertTrue(self.InviteTeam(self.getStudentCourse()[0].assignment[0], self.getStudentTeam()[0], [self.L1,self.L2]))
        self.assertTrue(self.L1.acceptTeam(self.getStudentTeam()[0]))
        self.assertFalse(self.L1.acceptTeam(self.getStudentTeam()[1]))
        self.assertEqual(len(self.getStudentTeam()[0].members),2)

        #decline
        self.assertTrue(self.L2.declineTeam(self.getStudentTeam()[0]))
        self.assertFalse(self.L2.declineTeam(self.getStudentTeam()[0]))
        self.assertEqual(len(self.getStudentTeam()[0].members),2)

        #remove
        self.assertTrue(self.L1.removeTeam(self.getStudentTeam()[0]))
        self.assertEqual(len(self.getStudentTeam()[0].members),1)
        self.assertTrue(self.Stud.removeTeam(self.getStudentTeam()[0]))
        self.assertEqual(self.getStudentTeam()[0],NULL)
        

if __name__ == '__main__':
    unittest.main()
