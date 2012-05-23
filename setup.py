from distutils.core import setup
import sys

kwargs = {}
if sys.version_info[0] >= 3:
    from setuptools import setup
    kwargs['use_2to3'] = True

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'Topic :: System', 
    'Topic :: System :: Shells',
    'Topic :: Terminals',
    'Topic :: Utilities',
]

long_description = """Pexpect-U is a fork of `pexpect <http://pexpect.sourceforge.net/>`_,
a pure-Python module to control interactive programs running in a virtual terminal.

Pexpect-U is unicode-aware, and compatible with Python 3 (using distribute to
run 2to3 during setup). It requires Python 2.6 or above."""

setup (name='pexpect-u',
    version='2.5.dev',
    packages=['pexpect', 'pexpect.tests'],
    package_data={'pexpect.tests': ['*.vt', '*.txt', '*.data', '*.sh']},
    description='Pexpect is a pure Python Expect. It allows easy control of other applications.',
    long_description=long_description,
    author='Noah Spurrier',
    author_email='noah@noah.org',
    maintainer='Thomas Kluyver',
    maintainer_email='thomas@kluyver.me.uk',
    url='http://pexpect.sourceforge.net/',
    license='MIT license',
    platforms='UNIX',
    classifiers=classifiers,
    **kwargs
)



