#!/usr/bin/python
#coding=utf-8

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

global cnt, cntList
cnt = 0
cntList = []
def gci(filepath):
  global cnt
  global cntList
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)            
    if os.path.isdir(fi_d):
      gci(fi_d)                  
      cnt += 1
    else:
      #print os.path.join(filepath,fi_d)
      #print (fi_d)
      #print cnt
      cntList.append(cnt)
      cnt = 0
      pass

#递归遍历/root目录下所有文件
rootDir = sys.argv[1]
gci(rootDir)
print max(cntList)
