#!/usr/bin/python
#coding=utf-8 

import os
import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]+([A-Za-z0-9_\- ]*)[\u4e00-\u9fa5]+')

filenames = os.listdir(os.getcwd())
for name in filenames:
  match = zhPattern.search(name.decode('utf-8'))
  if match:
    newName = match.groups()[0]
    os.rename(name, newName+'.rar')
