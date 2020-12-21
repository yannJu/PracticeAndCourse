#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import Int32MultiArray
import time
import math

def lineDetect(img):
		xyLst = list()
		h, w = img.shape

		window_h = 5
		nwindows = 20
		margin = 20
		minpix = 10

		nonzero = img.nonzero()
		nony = np.array(nonzero[0])
		nonx = np.array(nonzero[1])

		left_lines = ((nonx > 180) & (nonx < 230) & (nony > 385)).nonzero()[0]
		right_lines = ((nonx > 470) & (nonx <510) & (nony > 385)).nonzero()[0]

		lxcurrent = 0
		lycurrent = 0
		rxcurrent = 0
		rycurrent = 0
		center = None

		if (len(left_lines) > minpix):
			flag = 1
			lxcurrent = np.int(np.mean(nonx[left_lines]))
			lycurrent = np.int(np.max(nony[left_lines]))
			origin_x = lxcurrent
			origin_y = lycurrent
		elif (len(right_lines) > minpix):
			flag = 2
			rxcurrent = np.int(np.mean(nonx[right_lines]))
 			rycurrent = np.int(np.mean(nony[right_lines]))
			origin_x = rxcurrent
			origin_y = rycurrent
		else:
			flag = 3

		if flag != 3:
			for window in range(nwindows):
				if flag == 1:
					window_l_x = lxcurrent - margin
 					window_l_y = lycurrent - (window + 1) * window_h
					window_r_x = lxcurrent + margin
					window_r_y = lycurrent - window * window_h

					xyLst.append((lxcurrent, window_l_y))

					left_lines = ((nonx < window_r_x) & (nonx > window_l_x) & (nony < window_r_y) & (nony > window_l_y)).nonzero()[0]

					if (len(left_lines) > minpix):
						lxcurrent = np.int(np.mean(nonx[left_lines]))
				elif flag == 2:
					window_l_x = rxcurrent - margin
					window_l_y = rycurrent - (window + 1) * window_h
					window_r_x = rxcurrent + margin
					window_r_y = rycurrent - (window * window_h)

					xyLst.append((rxcurrent, window_l_y))

					right_lines = ((nonx < window_r_x) & (nonx > window_l_x) & (nony < window_r_y) & (nony > window_l_y)).nonzero()[0]

					if (len(right_lines) > minpix):
						rxcurrent = np.int(np.mean(nonx[right_lines]))
						rycurrent = np.int(np.mean(nony[right_lines]))
			x1, y1 = xyLst[0]
			x2, y2 = xyLst[-1]
			return math.degrees(math.atan((x2 - x1)/(y2 - y1)))

def pub_motor(Angle, Speed):
	drive_info = [Angle, Speed]
	drive_info = Int32MultiArray(data = drive_info)
	pub.publish(drive_info)
 
def start():
	global pub
	Angle = 0
	old_Angle = 0

	rospy.init_node('my_driver')
	pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
	
	cap = cv2.VideoCapture('/home/user/catkin_ws/src/xycar_simul/src/track-s.mkv')
	rate = rospy.Rate(30)
	cnt = 0

	while cap.isOpened():
		ret, img = cap.read()
		if ret:
			rate.sleep()
			blur_kernel = 5
			low_th = 130
			upper_th = 150
			threshhold_value = 160
			value = 255
			morph_kernel = np.ones((3, 3), np.uint8)

			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			h, w = gray.shape
			blur = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)
			canny = cv2.Canny(blur, low_th, upper_th)
			src = np.float32([[140, 320],
									[540, 310],
									[-350, 420],
									[1020, 410]])

			dst = np.float32([[0, 0],
									[w, 0],
									[0, h] ,
									[w, h]])
			M = cv2.getPerspectiveTransform(src, dst)
			warp = cv2.warpPerspective(canny, M, (w, h), flags=cv2.INTER_LINEAR)
			the = cv2.threshold(warp, threshhold_value, value, cv2.THRESH_BINARY)[1]
			dila = cv2.dilate(the, morph_kernel, iterations=2)

			Angle = lineDetect(dila)
			if (Angle != None):
				pub_motor(Angle * 4, 20)
				old_Angle = Angle
			else:
				pub_motor(old_Angle, 20)
if __name__ == '__main__':
	start()
