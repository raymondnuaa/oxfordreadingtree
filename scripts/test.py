#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import PythonMagick
img = PythonMagick.Image("1900.png")
img.sample('128x128')
img.write('ax.png')
'''


import PythonMagick
pdf = "aa.pdf"
p = PythonMagick.Image()
p.density('300')
p.read(pdf)
p.write('timg3.jpg')


'''
import PythonMagick
img = PythonMagick.Image()
img.density("300")
img.read("G:/oxfordtree/b.pdf") # read in at 300 dpi
img.write("G:/oxfordtree/bq.png")
'''

'''
import os
from pyPdf import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from PythonMagick import Image

reader = PdfFileReader(open("G:/oxfordtree/test/b.pdf", "rb"))
for page_num in xrange(reader.getNumPages()):
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(page_num))
    temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)
    writer.write(temp)
    temp.close()

    im = Image()
    im.density("300") # DPI, for better quality
    im.read(temp.name)
    im.write("bbsome_%d.jpg" % (page_num))

    os.remove(temp.name)
'''    
