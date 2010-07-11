#!/usr/bin/env python

from distutils.core import setup
from csa.version import __version__

long_description = """The CSA library provides elementary connection-sets and operators for
combining them. It also provides an iteration interface to such
connection-sets enabling efficient iteration over existing connections
with a small memory footprint also for very large networks. The CSA
can be used as a component of neuronal network simulators or other
tools."""

setup (
    name = "csa",
    version = __version__,
    packages = ['csa',],
    author = "Mikael Djurfeldt", # add your name here if you contribute to the code
    author_email = "mikael@djurfeldt.com",
    description = "The Connection-Set Algebra implemented in Python",
    long_description = long_description,
    license = "GPLv3",
    keywords = "computational neuroscience modeling connectivity",
    url = "http://software.incf.org/software/csa/",
    classifiers = ['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Scientific/Engineering'],
    requires = ['numpy', 'matplotlib'],
)