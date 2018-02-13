import unittest
from GitHub import getUserRepos, getCommitCount

class TestGitHub(unittest.TestCase):
    
    def testGitHub01A(self):
        self.assertIn("TwitchEmpire", getUserRepos("julasevich"))
                    
    def testGitHub01b(self):
        self.assertNotIn("HelloWorld", getUserRepos("julasevich"))

    def testGitHub01b(self):
        self.assertEqual(1, getCommitCount("julasevich", "TwitchEmpire"))
                         
    def testGitHub02A(self):
        self.assertIn("Triangle567", getUserRepos("julasevi567"))
                    
    def testGitHub02b(self):
        self.assertNotIn("HelloWorld", getUserRepos("julasevi567"))

    def testGitHub02b(self):
        self.assertNotEqual(1, getCommitCount("julasevi567", "Triangle567"))

    def testGitHub03A(self):
        self.assertEqual([], getUserRepos("FakeUsername23424"))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
