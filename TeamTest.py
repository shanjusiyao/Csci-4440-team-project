import unittest
from Student import Student
from Team import Team

class TeamTest(unittest.TestCase):

    # the testing framework will automatically call for every single test we run
    # in our case, it can also serve as constructor test
    def setUp(self):
        self.public = True
        self.private = False

        self.L1 = Student(1, "L1", self.private)
        self.L2 = Student(2, "L2", self.private)

        self.M11 = Student(11, "M11", self.private)
        self.M12 = Student(12, "M12", self.private)

        # initialize Team Objects Team(name, id, publicity, leader)
        #                                              v
        #                                        Student(id, username, publicity)
        self.Team1 = Team( "Team1", 1, self.public, self.L1 )
        self.Team2 = Team( "Team2", 2, self.private, self.L2 )

    # test all getters
    def test_gets(self):
        self.assertEqual(self.Team1.getName(), "Team1")
        self.assertEqual(self.Team1.getID(), 1)
        self.assertTrue(self.Team1.getPublicity())
        self.assertEqual(self.Team1.getLeader().getID(), 1)
        self.assertEqual(len( self.Team1.getTags() ), 0)
        self.assertEqual(len( self.Team1.getMembers() ), 1)
        self.assertEqual( (self.Team1.getMembers())[0].getID(), 1)

    # test all setters
    def test_sets(self):
        self.Team1.setName("newTeam1")
        self.assertEqual(self.Team1.getName(), "newTeam1")

        self.Team1.setPublicity(self.private)
        self.assertFalse(self.Team1.getPublicity())

    def test_addAndRemoveMembers(self):
        # add two members to Team1
        self.assertTrue( self.Team1.addMember(self.M11) )
        self.assertTrue( self.Team1.addMember(self.M12) )
        self.assertEqual( len( self.Team1.getMembers() ), 3 )
        self.assertEqual( (self.Team1.getMembers())[0].getID(), 1 )
        self.assertEqual( (self.Team1.getMembers())[1].getID(), 11 )
        self.assertEqual( (self.Team1.getMembers())[2].getID(), 12 )

        # invalid add
        self.assertFalse( self.Team1.addMember(self.M11) )

        # remove one member
        self.assertTrue( self.Team1.removeMember(self.M11) )
        self.assertEqual( len( self.Team1.getMembers() ), 2 )
        self.assertEqual( (self.Team1.getMembers())[0].getID(), 1 )
        self.assertEqual( (self.Team1.getMembers())[1].getID(), 12 )

        # remove team leader should fail
        self.assertFalse( self.Team1.removeMember(self.L1) )
        # remove a non-existing member should fail
        self.assertFalse( self.Team1.removeMember(self.M11) )

        # remove another member
        self.assertTrue( self.Team1.removeMember(self.M12) )
        self.assertEqual( len( self.Team1.getMembers() ), 1 )
        self.assertEqual( (self.Team1.getMembers())[0].getID(), 1)


    def test_addAndDeleteTags(self):
        # valid adds
        self.assertTrue( self.Team1.addTag("EDT") )
        self.assertTrue( self.Team1.addTag("Tuesday") )
        self.assertEqual( len( self.Team1.getTags() ), 2 )

        # invalid adds, duplicates
        self.assertFalse( self.Team1.addTag("EDT") )
        self.assertEqual( len( self.Team1.getTags() ), 2 )

        self.assertEqual( (self.Team1.getTags())[0], "EDT" )
        self.assertEqual( (self.Team1.getTags())[1], "Tuesday" )

        # invalid deletes
        self.assertFalse( self.Team1.deleteTag("PDT") )
        self.assertEqual( len( self.Team1.getTags() ), 2 )

        # valid deletes
        self.assertTrue( self.Team1.deleteTag("EDT") )
        self.assertEqual( len( self.Team1.getTags() ), 1 )
        self.assertEqual( (self.Team1.getTags())[0], "Tuesday" )

        self.assertTrue( self.Team1.deleteTag("Tuesday") )
        self.assertEqual( len( self.Team1.getTags() ), 0 )


    def test_changeLeader(self):
        # invalid change (not a member in the team)
        self.assertFalse( self.Team1.changeLeader(self.M11) )
        self.assertEqual( len( self.Team1.getMembers() ), 1 )
        self.assertEqual( self.Team1.getLeader().getID(), 1 )

        # invalid change (already a leader)
        self.assertFalse( self.Team1.changeLeader(self.L1) )
        self.assertEqual( len( self.Team1.getMembers() ), 1 )
        self.assertEqual( self.Team1.getLeader().getID(), 1 )

        # valid change
        self.Team1.addMember(self.M11)
        self.assertEqual( len( self.Team1.getMembers() ), 2 )
        self.assertTrue( self.Team1.changeLeader(self.M11) )
        self.assertEqual( self.Team1.getLeader().getID(), 11 )

    def test_dismiss(self):
        self.Team1.dismiss()
        self.assertEqual( len( self.Team1.getMembers() ), 0 )
        self.assertEqual( len( self.Team1.getTags() ), 0 )

if __name__ == '__main__':
    unittest.main()