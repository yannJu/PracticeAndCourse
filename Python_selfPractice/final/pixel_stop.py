import cv2
import numpy as np
import hj_line

class Pix_Stop:
    def __init__(self, Video):
        self.cap = cv2.VideoCapture(Video)
        self.line = hj_line.SlideWindow()
        self.oldL = 200
        self.oldR = 480
        self.stopFlag = False
    def findStop(self, roi, img):
        flag = 0#flag = 0 정지선 x /flag = 1 횡단보도/ flag = 2 출발선

        nonzero = roi.nonzero()

        lower_yellow = np.array([-20, 80, 80])
        upper_yellow = np.array([50, 255, 255])

        img = img[240:, : ]
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(img, img, mask=mask_yellow)

        cv2.imshow('bf', mask_yellow)
        cv2.imshow('aft', res)

        resnon = res.nonzero()
        resx = np.array(resnon[1])
        goodres = ((resx > 200) & (resx < 440)).nonzero()[0]

        if (len(nonzero[0]) > 1100):
            flag = 1
            if (len(goodres)):
                flag = 2

        return flag

    def process(self):
        while self.cap.isOpened():
            ret, img = self.cap.read()
            if ret:
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
                imgWarp = cv2.warpPerspective(img, M, (w, h), flags=cv2.INTER_LINEAR)
                warp = cv2.warpPerspective(canny, M, (w, h), flags=cv2.INTER_LINEAR)
                the = cv2.threshold(warp, threshhold_value, value, cv2.THRESH_BINARY)[1]
                #close = cv2.morphologyEx(warp, cv2.MORPH_CLOSE,morph_kernel)
                dila = cv2.dilate(the, morph_kernel, iterations=2)

                tf, startL, startR, w_img, flag = self.line.w_slidewindow(dila)

                if (tf):
                    h_img, theta, center, startXL, startXR = self.line.h_slidewindow(dila, startL, startR, flag)

                centerY = int(center[1])
                roi = dila[centerY - 20:centerY + 20, startXL + 25:startXR - 25]

                self.stopFlag = self.findStop(roi, imgWarp)
                if self.stopFlag == 1:
                    cv2.line(h_img, ((startXL + startXR)//2, centerY), ((startXL + startXR)//2, h), (255 , 0, 255), 2)
                    print(h - centerY)
                if self.stopFlag == 2:
                    cv2.line(h_img, (0, h//2), (w, h //2), (180,178, 40), 4)

                cv2.imshow('close', dila)
                cv2.imshow('w', w_img)
                cv2.imshow('h_img', h_img)
                cv2.imshow('roi', roi)

                if (cv2.waitKey(0) & 0xFF == 27):
                    break
            else: break
        cv2.destroyAllWindows()

if __name__ == '__main__':
    stop = Pix_Stop('org2.avi')
    stop.process()