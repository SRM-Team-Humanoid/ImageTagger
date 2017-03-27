import cv2
import numpy as np

f = open("rgb.txt", 'r')
bgrlist = f.read().split('\n')
for bgr in bgrlist[:-1]:
	bgr = map(int,bgr.split())
	im = np.asarray(bgr).reshape(1,1,3)
	#print im
	v = max(bgr)
	delta = max(bgr)-min(bgr)
	if v == 0:
		s = 0
	else:
		s = delta/v
	if v == bgr[2]:
		h = 60*(bgr[1]-bgr[0])/delta
	elif v == bgr[1]:
		h = 120+60*(bgr[0] - bgr[2])/delta
	elif v == bgr[0]:
		h = 240+60*(bgr[2]-bgr[1])/delta
	h=h/2
	hsv = [h,s,v]
	print hsv
	#print type(hsv)
Range=17
hsvUpper=np.array([h+Range,255,255])
hsvLower=np.array([h-Range,100,100])
#hsvLower=np.array([30,100,100])
#hsvUpper=np.array([90,255,255])
print hsvLower,hsvUpper


cap=cv2.VideoCapture(1)
while (True):
	_,c = cap.read()
	#cv2.imshow('Frame',c)
	hsvFeed = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsvFeed, hsvLower, hsvUpper)
	erode = cv2.erode(mask,None,iterations = 1)
        dilate = cv2.dilate(erode,None,iterations = 10)
	cv2.imshow('mask', mask)
	im,contours,hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if len(contours)>0:
 		m = max(contours, key=cv2.contourArea)
        	x, y, w, h = cv2.boundingRect(m)
		cv2.rectangle(c,(x,y),(x+w,y+h),(0,255,0),2)	
		 
	cv2.imshow('Frame',c)
	if (cv2.waitKey(25) & 0xFF == 27) :
		break
cap.release()
cv2.destroyAllWindows()
