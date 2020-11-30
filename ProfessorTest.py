import unittest
from Professor import Professor
from Student import Student
from Course import Course
from Team import Team
from Assignment import Assignment

class ProfessorTest(unittest.TestCase):

    # the testing framework will automatically call for every single test we run
    # in our case, it can also serve as constructor test
    def setUp(self):
        self.public = True
        self.private = False

        self.L1 = Student("1", "L1", self.private)
        self.M11 = Student(11, "M11", self.private)
        self.T1 = Team( "Team1", 1, self.public, self.L1 )

        self.Prof = Professor("golds")

        self.C1 = Course(10000, "CSCI-4440", 1, 75)
        self.C2 = Course(10001, "CSCI-4460", 1, 75)

    # test all getters
    def test_gets(self):
        self.assertEqual(self.Prof.getID(), "golds")
        self.assertEqual(len( self.Prof.getCourses() ), 0)

    # test all setters
    def test_sets(self):
        self.Prof.setID("silvers")
        self.assertEqual(self.Prof.getID(), "silvers")

    def test_addAndRemoveCourses(self):
        # add two courses
        self.assertTrue( self.Prof.addCourse(self.C1) )
        self.assertTrue( self.Prof.addCourse(self.C2) )
        self.assertEqual( len( self.Prof.getCourses() ), 2 )
        self.assertEqual( (self.Prof.getCourses())[0].getCRN(), 10000 )
        self.assertEqual( (self.Prof.getCourses())[1].getCRN(), 10001 )

        # invalid add
        self.assertFalse( self.Prof.addCourse(self.C1) )

        # remove one course
        self.assertTrue( self.Prof.removeCourse(self.C1) )
        self.assertEqual( len( self.Prof.getCourses() ), 1 )
        self.assertEqual( (self.Prof.getCourses())[0].getCRN(), 10001 )

        # remove a non-existing course should fail
        self.assertFalse( self.Prof.removeCourse(self.C1) )

        # remove another course
        self.assertTrue( self.Prof.removeCourse(self.C2) )
        self.assertEqual( len( self.Prof.getCourses() ), 0 )


    def test_addAndDeleteStudentTags(self):
        # valid adds
        self.assertTrue( self.Prof.addStudentTag(self.L1, "EDT") )
        self.assertTrue( self.Prof.addStudentTag(self.L1, "Tuesday") )
        self.assertEqual( len( self.L1.getTags() ), 2 )

        # invalid adds, duplicates
        self.assertFalse( self.Prof.addStudentTag(self.L1, "EDT") )
        self.assertEqual( len( self.L1.getTags() ), 2 )

        self.assertEqual( (self.L1.getTags())[0], "EDT" )
        self.assertEqual( (self.L1.getTags())[1], "Tuesday" )

        # invalid deletes
        self.assertFalse( self.Prof.deleteStudentTag(self.L1, "PDT") )
        self.assertEqual( len( self.L1.getTags() ), 2 )

        # valid deletes
        self.assertTrue( self.Prof.deleteStudentTag(self.L1, "EDT") )
        self.assertEqual( len( self.L1.getTags() ), 1 )
        self.assertEqual( (self.L1.getTags())[0], "Tuesday" )

        self.assertTrue( self.Prof.deleteStudentTag(self.L1, "Tuesday") )
        self.assertEqual( len( self.L1.getTags() ), 0 )

    def test_addAndDeleteTeamTags(self):
        # valid adds
        self.assertTrue( self.Prof.addTeamTag(self.T1, "EDT") )
        self.assertTrue( self.Prof.addTeamTag(self.T1, "Tuesday") )
        self.assertEqual( len( self.T1.getTags() ), 2 )

        # invalid adds, duplicates
        self.assertFalse( self.Prof.addTeamTag(self.T1, "EDT") )
        self.assertEqual( len( self.T1.getTags() ), 2 )

        self.assertEqual( (self.T1.getTags())[0], "EDT" )
        self.assertEqual( (self.T1.getTags())[1], "Tuesday" )

        # invalid deletes
        self.assertFalse( self.Prof.deleteTeamTag(self.T1, "PDT") )
        self.assertEqual( len( self.T1.getTags() ), 2 )

        # valid deletes
        self.assertTrue( self.Prof.deleteTeamTag(self.T1, "EDT") )
        self.assertEqual( len( self.T1.getTags() ), 1 )
        self.assertEqual( (self.T1.getTags())[0], "Tuesday" )

        self.assertTrue( self.Prof.deleteTeamTag(self.T1, "Tuesday") )
        self.assertEqual( len( self.T1.getTags() ), 0 )


    def test_addAndRemoveStudents(self):
        # valid adds
        self.assertTrue( self.Prof.addStudentToTeam(self.T1, self.M11) )
        self.assertEqual( len( self.M11.getTeams() ), 1 )
        self.assertEqual( len( self.T1.getMembers() ), 2 )

        # invalid adds, duplicates
        self.assertFalse( self.Prof.addStudentToTeam(self.T1, self.M11) )
        self.assertEqual( len( self.M11.getTeams() ), 1 )
        self.assertEqual( len( self.T1.getMembers() ), 2 )

        # valid removes
        self.assertTrue( self.Prof.removeStudentFromTeam(self.T1, self.M11) )
        self.assertEqual( len( self.M11.getTeams() ), 0 )
        self.assertEqual( len( self.T1.getMembers() ), 1 )

        # invalid remove
        self.assertFalse( self.Prof.removeStudentFromTeam(self.T1, self.M11) )
        self.assertEqual( len( self.M11.getTeams() ), 0 )
        self.assertEqual( len( self.T1.getMembers() ), 1 )


    def test_addAndRemoveAssignments(self):
        # valid adds
        # addAssignment(course, title, min, max, deadline)
        self.assertTrue( self.Prof.addAssignment(self.C1, "A1", 1, 4, 120220201159) )
        self.assertEqual( len( self.C1.getAssignments() ), 1 )

        # invalid adds, duplicates
        self.assertFalse( self.Prof.addAssignment(self.C1, "A1", 1, 4, 120220201159) )
        self.assertEqual( len( self.C1.getAssignments() ), 1 )

        A1 = (self.C1.getAssignments())[0]
        # invalid edit
        # editAssignment(self, assignment, title, min, max, deadline)
        self.assertFalse( self.Prof.editAssignment(None, "newA1", None, None, None) )

        # valid edits
        self.assertTrue( self.Prof.editAssignment(A1, "newA1", None, None, None) )
        self.assertEqual( A1.getTitle(), "newA1")

        # valid deletes
        self.assertTrue( self.Prof.deleteAssignment(self.C1, A1) )
        self.assertEqual( len( self.C1.getAssignments() ), 0 )

if __name__ == '__main__':
    unittest.main()