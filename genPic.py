#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from pyPdf import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from PythonMagick import Image, Geometry

for fpathe,dirs,fs in os.walk('stage_1'):
  for f in fs:
    fullName = os.path.join(fpathe,f)
    print fullName
    
    if(f.endswith(".pdf")):
		reader = PdfFileReader(open(fullName, "rb"))
		for page_num in xrange(reader.getNumPages()):
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
                    im.quality(50)
		    
		    picFullName = fullName[:-4]
		    im.write("%s_%da.jpg" % (picFullName, page_num))
		    		
		    os.remove(temp.name)
		    
		exit()
