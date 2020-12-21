#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import Int32MultiArray
import time
import math

class SlideWindow:

	def __init__(self):
		self.left_fit = None
		self.right_fit = None
		self.leftx = None
		self.rightx = None
		self.center_old = 320
		self.left_old = 180
		self.right_old = 500

	def w_slidewindow(self, img):
		flag = 0
		height, width = img.shape

		roi_img = img[height-150:height-100,:].copy()

		roi_height, roi_width = roi_img.shape

		cf_img = np.dstack((roi_img,roi_img,roi_img))

		window_height = 20
		window_width = 50

		minpix = window_height*window_width*0.05
		n_windows = roi_width//window_width//2
		pts_center = np.array([[roi_width//2,0],[roi_width//2, roi_height]], np.int32)
		cv2.polylines(cf_img, [pts_center],False, (0,120,120),1)

		nonzero = roi_img.nonzero()
		nonzeroy = np.array(nonzero[0])
		nonzerox = np.array(nonzero[1])

		x_center = self.center_old
		y_center = roi_height//2 # 160

		left_idx = 0
		right_idx = 0

		find_left = False
		find_right = False

		left_start_x = None
		left_start_y = None

		right_start_x = None
		right_start_y = None

		dist_threshold = 340
		dist = None

		for i in range(0,n_windows):
			if find_left is False:
				win_left_y_low = y_center - window_height//2
				win_left_y_high = y_center + window_height//2

				win_left_x_high = x_center - left_idx*window_width
				win_left_x_low = x_center - (left_idx+1)*window_width

			if find_right is False:
				win_right_y_low = y_center - window_height//2
				win_right_y_high = y_center + window_height//2

				win_right_x_low = x_center + right_idx*window_width
				win_right_x_high = x_center + (right_idx+1)*window_width


			cv2.rectangle(cf_img, (win_left_x_low, win_left_y_low), (win_left_x_high, win_left_y_high), (0,255,0), 1)
			cv2.rectangle(cf_img, (win_right_x_low, win_right_y_low), (win_right_x_high, win_right_y_high), (0,0,255), 1)

			good_left_inds = ((nonzeroy >= win_left_y_low) & (nonzeroy < win_left_y_high) & (nonzerox >= win_left_x_low) & (nonzerox < win_left_x_high)).nonzero()[0]
			good_right_inds = ((nonzeroy >= win_right_y_low) & (nonzeroy < win_right_y_high) & (nonzerox >= win_right_x_low) & (nonzerox < win_right_x_high)).nonzero()[0]

			if len(good_left_inds) > minpix and find_left is False:
				find_left = True

				left_start_x = np.int(np.mean(nonzerox[good_left_inds]))
				left_start_y = roi_height//2

				for i in range(len(good_left_inds)):
					cv2.circle(cf_img, (nonzerox[good_left_inds[i]], nonzeroy[good_left_inds[i]]), 1, (0,255,0), -1)
			else:
				left_idx += 1


			print('l',len(good_left_inds))
			print('r',len(good_right_inds))
			if len(good_right_inds) > minpix and find_right is False:
				find_right = True

				right_start_x = np.int(np.mean(nonzerox[good_right_inds]))
				right_start_y = roi_height//2

				for i in range(len(good_right_inds)):
					cv2.circle(cf_img, (nonzerox[good_right_inds[i]], nonzeroy[good_right_inds[i]]), 1, (0,0,255), -1)
			else:
				right_idx += 1


			if left_start_x is not None and right_start_x is not None:
				dist = right_start_x - left_start_x
				self.center_old = np.int((right_start_x+left_start_x)/2)
				if dist_threshold < dist and dist < dist_threshold + 80:
					print('flag = 1 ',dist)
					cv2.circle(cf_img, (right_start_x, right_start_y),3, (255,0,0),-1)
					cv2.circle(cf_img, (left_start_x, left_start_y), 3, (255,0,0),-1)
					self.left_old = left_start_x
					self.right_old = right_start_x
					flag = 1
					return True, left_start_x, right_start_x, cf_img, flag
				dist_from_old_L = abs(left_start_x - self.left_old)
				dist_from_old_R = abs(right_start_x - self.right_old)

				if dist_from_old_L < 70:
					print('flag = 2 ',dist)
					self.center_old = left_start_x + 55
					right_start_x = left_start_x+dist_threshold
					cv2.circle(cf_img,(left_start_x,left_start_y), 3, (0,0,255), -1)
					cv2.circle(cf_img,(right_start_x,left_start_y), 3, (0,255,255), -1)
					self.left_old = left_start_x
					self.right_old = right_start_x
					flag =2
					return True, left_start_x, right_start_x, cf_img, flag

				else:
					print('flag = 3 ',dist)
					self.center_old = right_start_x - 55
					left_start_x = right_start_x - dist_threshold
					cv2.circle(cf_img,(right_start_x,right_start_y), 3, (0,0,255), -1)
					cv2.circle(cf_img,(left_start_x,right_start_y), 3, (0,255,255), -1)
					self.left_old = left_start_x
					self.right_old = right_start_x
					flag = 3
					return True, left_start_x, right_start_x, cf_img, flag

			elif left_start_x is not None:
				dist_from_center = self.center_old - left_start_x
				dist_from_old = abs(left_start_x - self.left_old)
				print('flag = 2 ',dist_from_center)
				print('flag = 2 ',dist_from_old)

				if dist_from_center>30 and dist_from_old < 70 :
					self.center_old = left_start_x + 55
					right_start_x = left_start_x+dist_threshold
					cv2.circle(cf_img,(left_start_x,left_start_y), 3, (0,0,255), -1)
					cv2.circle(cf_img,(right_start_x,left_start_y), 3, (0,255,255), -1)
					self.left_old = left_start_x
					self.right_old = right_start_x
					flag =2
					return True, left_start_x, right_start_x, cf_img, flag

			elif right_start_x is not None:
				dist_from_center = right_start_x - self.center_old
				dist_from_old = abs(right_start_x - self.right_old)
				print('flag = 3 ',dist_from_center)
				print('flag = 3 ',dist_from_old)
				if dist_from_center>30 and dist_from_old < 70:
					self.center_old = right_start_x - 55
					left_start_x = right_start_x - dist_threshold
					cv2.circle(cf_img,(right_start_x,right_start_y), 3, (0,0,255), -1)
					cv2.circle(cf_img,(left_start_x,right_start_y), 3, (0,255,255), -1)
					self.left_old = left_start_x
					self.right_old = right_start_x
					flag =3
					return True, left_start_x, right_start_x, cf_img, flag

		return False, left_start_x, right_start_x, cf_img,flag

	def h_slidewindow(self, img, x_left_start, x_right_start, flag):
		h, w = img.shape
		center_point = w // 2
		output_img = np.dstack((img,img,img))
		nonzero = img.nonzero()
		nonzeroy = np.array(nonzero[0])
		nonzerox = np.array(nonzero[1])
		x_left = x_left_start
		x_right = x_right_start
		y_start = h//2 + 140
		window_height = 15
		window_width = 15

		find_left = False
		find_right = False

		minpix = window_width * window_height // 30
		n_windows = 5
		# print('nwindows',n_windows)
		left_idx = 0
		right_idx = 0
		center_x = np.zeros((5),dtype = 'f')
		center_y = np.zeros((5),dtype = 'f')
		center=np.zeros((5,2),dtype='f')

		size_center=0
		for i in range(n_windows):
			cv2.rectangle(output_img, (x_left - window_width, y_start - i * window_height), (x_left+ window_width, y_start - (i + 1) * window_height), (0,255,255),1)
			cv2.rectangle(output_img, (x_right - window_width, y_start - i * window_height), (x_right + window_width, y_start - (i + 1) * window_height), (255,0,255),1)
			good_left_inds = ((nonzerox >= x_left - window_width) & (nonzerox < x_left+ window_width) & (nonzeroy < y_start - i * window_height) & (nonzeroy >= y_start - (i + 1) * window_height)).nonzero()[0]
			good_right_inds = ((nonzerox >= x_right -window_width) & (nonzerox <= x_right + window_width) & (nonzeroy < y_start - i * window_height) & (nonzeroy >= y_start - (i + 1) * window_height)).nonzero()[0]

			# for j in range(len(good_left_inds)):
			#     cv2.circle(output_img, (nonzerox[good_left_inds[j]], nonzeroy[good_left_inds[j]]), 1, (0,255,0), -1)
			#
			# for j in range(len(good_right_inds)):
			#     cv2.circle(output_img, (nonzerox[good_right_inds[j]], nonzeroy[good_right_inds[j]]), 1, (0,0,255), -1)

			if len(good_left_inds) > minpix:
				find_left = True
				x_left = np.int(np.mean(nonzerox[good_left_inds]))
			else:
				find_left = False

			if len(good_right_inds) > minpix:
			    find_right = True
			    x_right = np.int(np.mean(nonzerox[good_right_inds]))
			else:
				find_right = False

			if find_left and find_right:
				center_point = np.int((x_left +x_right)/2)
			elif find_left:
				center_point = x_left + 170
			elif find_right:
				center_point = x_right - 170
		
			if i < 5:
			    # center[i] = np.array([center_point,y_start - i*window_height - 10])
			    center_x[i] = np.array([center_point])
			    center_y[i] = np.array([y_start - i*window_height - 10])
			    size_center+=1

			# print('center',center_point)
			# print('y',y_start - (i*window_height) -3)
			# cv2.circle(output_img, (center_point,y_start - i*window_height - 10 ),3,(0,0,255),1)
		fp1 = np.polyfit(center_y,center_x,1)
		f1 = np.poly1d(fp1)
		returns_x = f1(center_y)
		cv2.line(output_img,(returns_x[0],center_y[0]),(returns_x[size_center-1],center_y[size_center-1]),(0,0,255))

		for i in range(5):
			cv2.circle(output_img,(returns_x[i],center_y[i]),3,(0,0,255),-1)
		cv2.circle(output_img,(center_x[0],center_y[0]),9,(255,50,0),-1)

		# steer_theta=math.degrees(math.atan((center_x[0]-returns_x[size_center-1] )/(center_y[size_center-1]-center_y[0])))
		steer_theta=math.degrees(math.atan((240-returns_x[size_center-1] )/(center_y[size_center-1]-295)))
		cv2.line(output_img,(240,295),(returns_x[size_center-1],center_y[size_center-1]),(0,255,255))
			# line_fitter.fit(center.reshape(-1,1),center_y)
		# y_predicted = line_fitter.predict(center_x)

		return output_img ,steer_theta

def pub_motor(Angle, Speed):
	drive_info = [Angle, Speed]
	drive_info = Int32MultiArray(data = drive_info)
	pub.publish(drive_info)

if __name__ == '__main__':
	global pub

	rospy.init_node('my_driver')
	pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
	
	oldL = 0
	oldR = 0
	line = SlideWindow()
	cap = cv2.VideoCapture('/home/user/catkin_ws/src/xycar_simul/src/org2.avi')
	rate = rospy.Rate(30)

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

			tf, startL, startR, w_img, flag = line.w_slidewindow(dila)

			if tf:
				h_img, theta= line.h_slidewindow(dila, startL, startR, flag)
				oldL = startL
				oldR = startR
			else:
				h_img, theta= line.h_slidewindow(dila, oldL, oldR, flag)
			
			pub_motor(theta, 20)
