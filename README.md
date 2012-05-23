Pexpect-u
=========

Pexpect-u is a fork of Pexpect by Thomas Kluyver that supports Python 3 and
unicode.

Original repo: https://bitbucket.org/takluyver/pexpect

This is a *fork of Pexpect-u* to support:

 * Direct install from pip.
 * Adding various bugfixes to pxssh.
  * Works on AIX, Solaris boxes.
  * Remove annoying ASKPASS GUI.


Install
-------

 * pip install git+git://github.com/serialx/pexpect-u.git


Original Pexpect README
-----------------------

Pexpect is a Pure Python Expect-like module

Pexpect makes Python a better tool for controlling other applications.

Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for
duplicating software package installations on different servers. It can be
used for automated software testing. Pexpect is in the spirit of Don Libes'
Expect, but Pexpect is pure Python. Unlike other Expect-like modules for
Python, Pexpect does not require TCL or Expect nor does it require C
extensions to be compiled. It should work on any platform that supports the
standard Python pty module. The Pexpect interface was designed to be easy to use.

If you want to work with the development version of the source code then please
read the DEVELOPERS document in the root of the source code tree.

Free, open source, and all that good stuff.
Pexpect Copyright (c) 2008 Noah Spurrier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.

Noah Spurrier
http://pexpect.sourceforge.net/

