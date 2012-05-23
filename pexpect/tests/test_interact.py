#!/usr/bin/env python
import pexpect
import unittest
import PexpectTestCase

class InteractTestCase (PexpectTestCase.PexpectTestCase):
    
    def test_interact (self):
        p = pexpect.spawn('%s interact.py' % self.PYTHONBIN)
        p.sendline ('Hello')
        p.sendline ('there')
        p.sendline ('Mr. Python')
        p.expect ('Hello')
        p.expect ('there')
        p.expect ('Mr. Python')
        p.sendeof () 
        p.expect (pexpect.EOF)

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(InteractTestCase,'test')

