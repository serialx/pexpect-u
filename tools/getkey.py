'''
This currently just holds some notes.
This is not expected to be working code.

$Revision: 120 $
$Date: 2002-11-27 20:13:04 +0100 (Wed, 27 Nov 2002) $
'''

import tty, termios, sys

def getkey():
    file = sys.stdin.fileno()
    mode = termios.tcgetattr(file)
    try:
        tty.setraw(file, termios.TCSANOW)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(file, termios.TCSANOW, mode)
    return ch

def test_typing ():
    s = screen (10,10)
    while 1:
        ch = getkey()
        s.type(ch)
        print str(s)
        print

