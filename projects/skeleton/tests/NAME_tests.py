#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tool import *
import NAME

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"
