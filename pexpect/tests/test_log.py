#!/usr/bin/env python
import pexpect
import unittest
import os
import PexpectTestCase

from io import StringIO

class TestCaseLog(PexpectTestCase.PexpectTestCase):

    def test_log (self):
        log_message = 'This is a test.'
        mylog = StringIO()
        p = pexpect.spawn('echo', [log_message])
        p.logfile = mylog
        p.expect (pexpect.EOF)
        lf = mylog.getvalue()
        lf = lf[:-2]
        assert lf == log_message

    def test_log_logfile_read (self):
        log_message = 'This is a test.'
        mylog = StringIO()
        p = pexpect.spawn('cat')
        p.logfile_read = mylog
        p.sendline(log_message)
        p.sendeof()
        p.expect (pexpect.EOF)
        lf = mylog.getvalue()
        lf = lf[:-2]
        lf = lf.replace(unichr(4),'')
        assert lf == 'This is a test.\r\nThis is a test.', "The read log file has bad data. Note logfile_read should only record what we read from child and nothing else.\n" + repr(lf)

    def test_log_logfile_send (self):
        log_message = 'This is a test.'
        mylog = StringIO()
        p = pexpect.spawn('cat')
        p.logfile_send = mylog
        p.sendline(log_message)
        p.sendeof()
        p.expect (pexpect.EOF)
        lf = mylog.getvalue()
        lf = lf[:-2]
        assert lf == log_message, "The send log file has bad data. Note logfile_send should only record what we sent to child and nothing else."

    def test_log_send_and_received (self):

        """The logfile should have the test message three time -- once for the
        data we sent. Once for the data that cat echos back as characters are
        typed. And once for the data that cat prints after we send a linefeed
        (sent by sendline). """

        log_message = 'This is a test.'
        mylog = StringIO()
        p = pexpect.spawn('cat')
        p.logfile = mylog
        p.sendline(log_message)
        p.sendeof()
        p.expect (pexpect.EOF)
        lf = mylog.getvalue()
        lf = lf.replace(unichr(4),'')
        assert lf == 'This is a test.\nThis is a test.\r\nThis is a test.\r\n', repr(lf)

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(TestCaseLog,'test')

