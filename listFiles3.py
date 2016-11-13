#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
'''
a = [i for i in os.listdir('.') if os.path.isdir(i)]
print a 
b = [i for i in os.listdir('.') if os.path.isfile(i) and os.path.splitext(i)[1]=='.py']
print b
exit()
'''
pdfCnt = 0
mp3Cnt = 0
if(len(sys.argv) < 2):
  print 'Please input dir\n'
  exit()
rootDir = sys.argv[1]
for fpathe,dirs,fs in os.walk(rootDir):
  for f in fs:
    if(f.endswith(".pdf")):
      #print os.path.join(fpathe,f)
      pdfCnt += 1
    elif(f.endswith(".mp3")):
      #print os.path.join(fpathe,f)
      mp3Cnt += 1

print pdfCnt
print mp3Cnt
