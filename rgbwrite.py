import xml.etree.ElementTree as et
import numpy as np
import cv2
import time
tree = et.ElementTree(file = 'color.xml')
root = tree.getroot()
avgb = avgg = avgr = 0
for img in tree.findall('images/image'):
	img_file = img.attrib['file']
	#print img_file	
	for elem in img: 
		w,y,x,h = [int(elem.attrib[at]) for at in elem.attrib]
		#print w,y,x,h
		image = cv2.imread(img_file)
		print image
		cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),1)
		#print image		
		#cv2.imshow("image",image)
		for i in range(y,y+h):
			for j in range(x,x+w):
				b,g,r = image[i][j]
				avgb+=b
				avgg+=g
				avgr+=r
		avgb /= h*w
		avgg /= h*w
		avgr /= h*w 
		print("b: "+str(avgb)+ " g: "+str(avgg)+" r: "+str(avgr))	
		f = open("rgb.txt",'a')
		f.write(str(avgb)+" "+str(avgg)+" "+str(avgr)+ "\n")
		cv2.waitKey(25)
		#time.sleep(3)
f.close()
#cv2.destroyAllWindows()
