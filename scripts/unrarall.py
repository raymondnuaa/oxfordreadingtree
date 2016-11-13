#!/usr/bin/python
#coding=utf-8 

import os
import re

os.system('ls')

zhPattern = re.compile('\.rar')

filenames = os.listdir(os.getcwd())
for name in filenames:
  match = zhPattern.search(name.decode('utf-8'))
  if match:
    cmd = 'rar x %s unrar ' %  name
    print os.system(cmd)
