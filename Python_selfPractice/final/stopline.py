import cv2
import numpy as np
# import final_linedetect
import math
import hj_line

class StopLine:
    def __init__(self, video):
        self.cap = cv2.VideoCapture(video)

    def findline(self, img, locate_x, locate_y, length, find_l, find_r):
        outimg = np.dstack((img, img, img))
        stopflag = None
        left = None
        right = None

        window_h = 5
        window_w = 5
        L_loca_x = locate_x
        R_loca_x = locate_x
        minpix = 23

        nonzero = img.nonzero()
        non_y = np.array(nonzero[0])
        non_x = np.array(nonzero[1])
        good_L_lst = ((non_x <= L_loca_x) & (non_x >= L_loca_x - window_w) & (non_y <= locate_y + window_h) & (non_y >= locate_y - window_h)).nonzero()[0]
        good_R_lst = ((non_x >= R_loca_x) & (non_x <= R_loca_x + window_w) & (non_y <= locate_y + window_h) & (non_y >= locate_y - window_h)).nonzero()[0]

        lcurrent = np.mean(non_x[good_L_lst])
        lycurrent = np.mean(non_y[good_L_lst])
        rcurrent = np.mean(non_x[good_R_lst])
        rycurrent = np.mean(non_y[good_R_lst])

        while (len(good_L_lst) >= minpix or len(good_R_lst) >= minpix):
            if (lcurrent < find_l or rcurrent > find_r): break
            if (len(good_L_lst) >= minpix):
                good_L_lst = ((non_x <= lcurrent) & (non_x >= lcurrent - window_w) & (non_y <= lycurrent + window_h) & (non_y >= lycurrent - window_h)).nonzero()[0]
                lcurrent = np.mean(non_x[good_L_lst])
                lycurrent = np.mean(non_y[good_L_lst])
            if (len(good_R_lst) >= minpix):
                good_R_lst = ((non_x >= rcurrent) & (non_x <= rcurrent + window_w) & (non_y <= rycurrent + window_h) & (non_y >= rycurrent - window_h)).nonzero()[0]
                rcurrent = np.mean(non_x[good_R_lst])
                rycurrent = np.mean(non_y[good_R_lst])
            cv2.circle(outimg, (int(lcurrent), locate_y), 3, (0, 150, 150), 2)
            cv2.circle(outimg, (int(rcurrent), locate_y), 3, (150, 150, 0), 2)
        lcurrent = np.mean(non_x[good_L_lst])
        rcurrent = np.mean(non_x[good_R_lst])
        lycurrent = np.mean(non_y[good_L_lst])
        rycurrent = np.mean(non_y[good_R_lst])
        try:
            stop_length = math.sqrt(pow(rcurrent - lcurrent, 2) + pow(rycurrent - lycurrent, 2))
            if length:
                print(length)
                if (length * 0.75 < int(stop_length) < length * 1.25):
                    stopflag = 1
                    left = (int(lcurrent), int(lycurrent))
                    right = (int(rcurrent), int(rycurrent))
            cv2.imshow('out', outimg)
            cv2.waitKey(0)
            return stopflag, left, right
        except:
            return None, 0, 0

    def processing(self):
        center = None
        frame = 0

        while self.cap.isOpened():
            kernel_size = 3
            low_th = 140
            high_th = 180
            threshold_value = 160
            value = 255
            dila_ker = np.ones((5, 5), np.uint8)

            ret, img = self.cap.read()

            if ret:
                h = img.shape[0]
                w = img.shape[1]

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (kernel_size,kernel_size), 0)
                edge = cv2.Canny(blur, low_th, high_th)
                src = np.float32([[140, 320],
                                  [540, 310],
                                  [-350, 420],
                                  [1020, 410]])

                dst = np.float32([[0, 0],
                                  [w, 0],
                                  [0, h] ,
                                  [w, h]])
                M = cv2.getPerspectiveTransform(src, dst)
                the = cv2.threshold(edge, threshold_value, value, cv2.THRESH_BINARY)[1]
                warp = cv2.warpPerspective(the, M, (w, h), flags=cv2.INTER_LINEAR)
                dila = cv2.dilate(warp, dila_ker, iterations=1)
                stop_img = np.dstack((dila, dila, dila))

                line = hj_line.SlideWindow()
                tf, left, right, w_w_img, flag = line.w_slidewindow(dila)
                if (tf):
                    h_window, theta, center_Y, startXL, startXR = line.h_slidewindow(dila, left, right, flag)

                # if (center != None):
                #     locate_x, locate_y = center
                #     if (gray[int(locate_y)][int(locate_x)] != 0):
                #         stop, id_L, id_R = self.findline(stop_img, locate_x, locate_y, length, xL, xR)
                #         if (stop != None and frame == 0):
                #             print("STOP!")
                #             cv2.line(stop_img, id_L, id_R, (0, 0, 255), 2)
                #             frame += 1
                #         if (frame > 7):
                #             frame = 0
                # cv2.imshow('img', stop_img)
                if (cv2.waitKey(1) & 0xFF == 27):
                    break
                #

if __name__ == '__main__':
    stop = StopLine('org2.avi')
    stop.processing()