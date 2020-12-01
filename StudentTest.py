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
        

if __name__ == '__main__':
    unittest.main()
