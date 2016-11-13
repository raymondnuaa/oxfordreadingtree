# -*- coding:utf-8 -*-  

import PythonMagick
import PIL.Image as Image  
import os,sys  

'''
for i in range(1, 9, 2):
	image1 = PythonMagick.Image("six_%d.jpg" % i)
	size1 = image1.size()
	
	image2 = PythonMagick.Image("six_%d.jpg" % (i+1))
	size2 = image2.size()  
	
	aw = size1.width()  + size2.width()
	ah = size1.height() + size2.height()
	
	height = max(size1.height(), size2.height())
	
	toImage = Image.new('RGBA', (aw, height))  
	
	
	fromImage = Image.open("six_%d.jpg" % i)
	toImage.paste(fromImage, (0, 0))  
	
	fromImage = Image.open("six_%d.jpg" % (i+1))
	toImage.paste(fromImage, (size1.width(), 0)) 
	
	toImage = toImage.resize((640, height*640/aw))
	#toImage = toImage.rotate(-90)
	  
	toImage.save("psix%d.jpg" % i) 
	
	#print aw, ah
	#exit()
'''

im = Image.open('six_9.jpg') 
w  = im.size[0]
h  = im.size[1]

out = im.resize((640, h*640/w))
#out = out.rotate(90)
out.save('psix9.jpg')



