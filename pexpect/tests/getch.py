#!/usr/bin/env python
import sys, tty, termios
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#for i in range(256):
# Current Python unicode support was too hard to figure out.
# This only tests the true ASCII characters now:
for i in range(126):
    c = getch()
    a = ord(c) # chr(a)
    print a

