#!/usr/bin/python
#coding=utf-8

import os
import os.path
rootdir = "stage_1"                                   # 指明被遍历的文件夹

i = 1
for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	for dirname in  dirnames:                       #输出文件夹信息
		print  "DirParent: " + parent
		print  "dirname is: " + dirname
		print  "\n\n"

	for filename in filenames:                        #输出文件信息
		print "parent is: " + parent
		print "filename is: " + filename
		print "FileFullNmae: " + os.path.join(parent,filename + "\n\n") #输出文件路径信息
	aa = "-------------%d-----------------------\n" % (i)
        print aa
	i += 1


