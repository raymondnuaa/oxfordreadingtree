#!/usr/bin/python
#coding=utf-8

import os
import os.path
rootdir = 'unrar' 

for parent,dirnames,filenames in os.walk(rootdir):
  for dirname in  dirnames:
    print "parent is:" + parent
    print  "dirname is" + dirname

  for filename in filenames:
    print "parent is": + parent
    print "filename is:" + filename
    print "the full name of the file is:" + os.path.join(parent,filename)

