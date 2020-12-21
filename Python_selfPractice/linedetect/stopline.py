import cv2
import numpy as np
import linedetect
import math

class StopLine:
    def __init__(self, video):
        self.cap = cv2.VideoCapture(video)
        self.stopflag = 0

    def findline(self, img, locate_x, locate_y, length, find_l, find_r):
        outimg = np.dstack((img, img, img))
        self.stopflag = 1
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
        rcurrent = np.mean(non_x[good_R_lst])
        rycurrent = np.mean(non_y[good_R_lst])
        print("L : ", lcurrent, " R : ", rcurrent, " LENGTH : ", math.sqrt(pow(rcurrent - lcurrent, 2) + pow(rycurrent - lycurrent, 2)))
        if length:
            print(length)
            if (length * 0.75 < int(math.sqrt(pow(rcurrent - lcurrent, 2) + pow(rycurrent - lycurrent, 2))) < length * 1.25):
                cv2.line(outimg, (int(lcurrent), int(lycurrent)), (int(rcurrent), int(rycurrent)), (150 , 170, 150), 3)
        cv2.imshow('out', outimg)
        cv2.waitKey(0)

    def processing(self):
        while self.cap.isOpened():
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            src = np.float32([[60, 355],
                              [10, 400],
                              [640 - 15, 405],
                              [640, 360]])
            dst = np.float32([[0, 0],
                              [0, 480],
                              [640, 480],
                              [640 + 50, 0]])
            M = cv2.getPerspectiveTransform(src, dst)
            warp = cv2.warpPerspective(gray, M, (640, 480), flags=cv2.INTER_LINEAR)
            if ret:
                line = linedetect.LineDetector(img)
                line.main(warp)
                if line.xlocate != None:
                    locate_x, locate_y = line.xlocate
                    length = line.length
                    if (locate_x < 640 and locate_y < 480 and warp[int(locate_y)][int(locate_x)] != 0):
                        self.findline(warp, locate_x, locate_y, length, line.x_start_l, line.x_start_r)

if __name__ == '__main__':
    stop = StopLine('22.avi')
    stop.processing()