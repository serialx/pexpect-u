
import unittest
import sys
import os

class PexpectTestCase(unittest.TestCase):
    def setUp(self):
        self.PYTHONBIN = sys.executable
        self.original_path = os.getcwd()
        newpath = os.path.dirname(__file__)
        os.chdir(newpath)
        print '\n', self.id(),
        unittest.TestCase.setUp(self)
    def tearDown(self):
        os.chdir (self.original_path)

