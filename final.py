#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, errno
import sys
import re
import string
import MySQLdb

from pyPdf import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from PythonMagick import Image, Geometry

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def pathHandle(fpathe, zhPattern, wwwDir):
    dirInfo = fpathe.split(os.sep)
    if(len(dirInfo) != 3):
        print "dir length wrong, exit..."
        exit()
    match = zhPattern.search(dirInfo[1].decode('utf-8'))
    if match:
        stage = string.capwords(match.groups()[0]).replace(' ', '_')
        cate  = string.capwords(match.groups()[1]).replace(' ', '_')
    else:
        print "dir format issue, failed!"
        exit()
    pdfName = string.capwords(dirInfo[2]).replace(' ', '_')
    print(stage, cate, pdfName, f)
    newDir = wwwDir + os.sep.join([stage, cate, pdfName]) 
    return newDir, stage, cate, pdfName

if(len(sys.argv) < 2):
    print 'Please input dir\n'
    exit()

rootDir = sys.argv[1]

zhPattern = re.compile(u'(.*)\u7684+([A-Za-z0-9_\- ]*)[\u4e00-\u9fa5]+')
wwwDir    = "/alidata/www/eway/oxford/trees/"

conn = MySQLdb.connect(host='localhost',user='root',passwd='8c759b2234',port=3306, db='oxford', unix_socket='/tmp/mysql.sock')
cur  = conn.cursor()

for fpathe,dirs,fs in os.walk(rootDir):
    for f in fs:
        fullName = os.path.join(fpathe,f)
        #print fullName
    
        if(f.endswith(".pdf")):
            newDir,stage,cate,pdfName = pathHandle(fpathe, zhPattern, wwwDir)
            mkdir_p(newDir)
            print newDir

            reader = PdfFileReader(open(fullName, "rb"))
            print fullName
            pageCnt = reader.getNumPages()

            values = [stage, cate, pdfName, pageCnt]
            cur.execute('insert into trees (stage, category, title, pages) values(%s, %s, %s, %s)', values)
            
            for page_num in xrange(pageCnt):
                writer = PdfFileWriter()
                writer.addPage(reader.getPage(page_num))
                temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)
                writer.write(temp)
                temp.close()
                
                im = Image()
                im.density("300") # DPI, for better quality
                im.read(temp.name)
                
                imSize = im.size()
                width  = imSize.width()
                height = imSize.height()
                
                newSize = Geometry("%dx%d" % (640, height*640/width))
                im.resize(newSize)
                im.quality(80)
                
                #picFullName = fullName[:-4]
                picNewName = "%s%s%d.jpg" % (newDir, os.sep, page_num)
                #print picNewName
                #print type(picNewName)
                #print type(picNewName.encode("utf-8"))
                im.write(picNewName.encode("utf-8"))
                 
                
                os.remove(temp.name)
                
            
        elif(f.endswith(".mp3")):
            newDir,stage,cate,pdfName = pathHandle(fpathe, zhPattern, wwwDir)
            mkdir_p(newDir)
            finalMp3 = newDir+os.sep+"1.mp3"
            orgMp3   = os.path.join(fpathe, f).decode("utf-8")
            cpCmd    = "cp \"%s\" %s" % (orgMp3, finalMp3)
            #print finalMp3, orgMp3
            #print type(finalMp3), type(orgMp3)
            print cpCmd
            #print type(cpCmd)
            os.system(cpCmd.encode("utf-8"))
            
conn.commit()
cur.close()
conn.close()
