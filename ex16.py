#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erace %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "Now I'M going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

all_lines = "%s\n%s\n%s\n" % (line1, line2, line3)

target.write(all_lines)

print "And finally, we close it."
target.close()
