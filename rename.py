#!/usr/bin/python
#coding=utf-8 

import os
import re
import sys
import string

zhPattern = re.compile(u'(.*)\u7684+([A-Za-z0-9_\- ]*)[\u4e00-\u9fa5]+')

rootDir = sys.argv[1]
filenames = os.listdir(rootDir)

for name in filenames:
  match = zhPattern.search(name.decode('utf-8'))
  if match:
    stage = string.capwords(match.groups()[0])
    cate  = string.capwords(match.groups()[1])
    stage = stage.replace(' ', '_')
    cate  = cate.replace(' ', '_')
    #os.rename(name, newName)
    print (stage, cate)
