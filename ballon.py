import mysql.connector
import serial
import math
import cv2
import numpy as np
import os
import random
import json


# connect to server
# requete UNIX
config = {
		'user': 'root',
		'password': 'root',
		'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
		'database': 'ma_base',
		'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
cur = link.cursor()

# on attend une entree de l'arduino
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
id = 1


while 1 :
	# bloquant tant qu'on a pas de vitesse
	#str  = ser.readline()
	speed1 = ser.readline().strip()
	print "speed reveived"
#	speed  = [int(s) for s in str.split() if s.isdigit()]
#	speed  = int(str)
	print "speed reveived into int"
	print speed1
	# Calcul de la precision

#	cv2.namedWindow("preview")
#	vc = cv2.VideoCapture(0)

#	if vc.isOpened(): # try to get the first frame
#			rval, frame = vc.read()
#	else:
#			rval = False
	# si la prise de photo fonctionne
#	if rval:
#			cv2.waitKey(1)
#			rval, frame = vc.read()
#			img = cv2.medianBlur(frame,5)
#			imgg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#			cimg = cv2.cvtColor(imgg,cv2.COLOR_GRAY2BGR)
#			circles = cv2.HoughCircles(imgg,cv2.HOUGH_GRADIENT,1,20,param1=100,param2=30,minRadius=5,maxRadius=20)
#  Il reste a refaire l'algo de la precision
#			cv2.destroyWindow("preview")
	speed =float(speed1) /3.6  # km/h vers m/s
	precision = random.randint(30,89);
	print precision 
	# calcul de la distance theorique et de la force
	# magic number (1/2)*0.420 = 0,21 et 420g = poids du balon
	force = 0.21*(speed*speed)
	print force
	distance = math.ceil(((speed*speed /10 )*math.sin(math.pi/2))*4) 
	print distance
	# Calcul du score
	# vitesse 0 - 65 -> 0 a 100
	# precision 0 -100
	score = (((100*speed)/6500)*400+(precision/100)*400)
	print score

	# pour l'id du tir

	
	# rajouter le score

	print cur.execute("""INSERT INTO presentation VALUES (%s,%s,%s,%s,%s,%s)""",(id,speed,force,int(distance),int(precision),score))
	print cur.statement
	print "fin tir"
	id = id + 1
	
link.commit()
cur.close() 
link.close() 