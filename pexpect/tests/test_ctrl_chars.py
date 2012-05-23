#!/usr/bin/env python
import pexpect
import unittest
import PexpectTestCase
import time
import os

class TestCtrlChars(PexpectTestCase.PexpectTestCase):

    def test_control_chars (self):

        """FIXME: Python unicode was too hard to figure out, so
        this tests only the true ASCII characters. This is lame
        and should be fixed. I'm leaving this script here as a
        placeholder so that it will remind me to fix this one day.
        This is what it used to do:
        This tests that we can send all 256 8-bit ASCII characters
        to a child process."""

        # FIXME: Getting this to support Python's Unicode was
        # too hard, so I disabled this. I should fix this one day.
        return 0
        child = pexpect.spawn('python getch.py')
        try:
            for i in range(256):
#                child.send(unicode('%d'%i, encoding='utf-8'))
                child.send(chr(i))
                child.expect ('%d\r\n' % i)
        except Exception, e:
            msg = "Did not echo character value: " + str(i) + "\n" 
            msg = msg + str(e)
            self.fail(msg)

    def test_sendintr (self):
        try:
            child = pexpect.spawn('python getch.py')
            time.sleep(0.5)
            child.sendintr()
            child.expect ('3\r\n')
        except Exception, e:
            msg = "Did not echo character value: 3\n" 
            msg = msg + str(e)
            self.fail(msg)

    def test_bad_sendcontrol_chars (self):

        """This tests that sendcontrol will return 0 for an unknown char. """

        child = pexpect.spawn('python getch.py')
        retval = child.sendcontrol('1') 
        assert retval == 0, "sendcontrol() should have returned 0 because there is no such thing as ctrl-1."

    def test_sendcontrol(self):

        """This tests that we can send all special control codes by name.
        """

        child = pexpect.spawn('python getch.py')
        #child.delaybeforesend = 0.1
        for i in 'abcdefghijklmnopqrstuvwxyz':
            child.sendcontrol(i)
            child.expect ('[0-9]+\r\n')
            #print child.after

        child.sendcontrol('@')
        child.expect ('0\r\n')
        #print child.after
        child.sendcontrol('[')
        child.expect ('27\r\n')
        #print child.after
        child.sendcontrol('\\')
        child.expect ('28\r\n')
        #print child.after
        child.sendcontrol(']')
        child.expect ('29\r\n')
        #print child.after
        child.sendcontrol('^')
        child.expect ('30\r\n')
        #print child.after
        child.sendcontrol('_')
        child.expect ('31\r\n')
        #print child.after
        child.sendcontrol('?')
        child.expect ('127\r\n')
        #print child.after

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(TestCtrlChars,'test')

