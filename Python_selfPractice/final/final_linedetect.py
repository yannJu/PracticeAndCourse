import cv2
import numpy as np

class LineDetect:
    def __init__(self):
        self.xlocate = None
        self.length = None

    def main(self, img):
        img = np.dstack((img, img, img)) * 255
        h = img.shape[0]
        w = img.shape[1]

        window_h = 5
        nwindows = 20
        margin = 20
        minpix = 10

        nonzero = img.nonzero()
        nony = np.array(nonzero[0])
        nonx = np.array(nonzero[1])

        left_lines = ((nonx > 205) & (nonx < 230) & (nony > 385)).nonzero()[0]
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
        elif (len(right_lines) > minpix):
            flag = 2
            rxcurrent = np.int(np.mean(nonx[right_lines]))
            rycurrent = np.int(np.mean(nony[right_lines]))
        else:
            flag = 3

        if flag != 3:
            for window in range(nwindows):
                if flag == 1:
                    window_l_x = lxcurrent - margin
                    window_l_y = lycurrent - (window + 1) * window_h
                    window_r_x = lxcurrent + margin
                    window_r_y = lycurrent - window * window_h


                    cv2.rectangle(img, (window_l_x, window_l_y), (window_r_x, window_r_y), (150, 150, 0), 2)
                    cv2.rectangle(img, (window_l_x + int(w * 0.43), window_l_y), (window_r_x + int(w * 0.43), window_r_y), (0, 150, 150), 2)

                    print(len(left_lines))
                    left_lines = ((nonx < window_r_x) & (nonx > window_l_x) & (nony < window_r_y) & (nony > window_l_y)).nonzero()[0]

                    if (len(left_lines) > minpix):
                        lxcurrent = np.int(np.mean(nonx[left_lines]))
                elif flag == 2:
                    window_l_x = rxcurrent - margin
                    window_l_y = rycurrent - (window * window_h)
                    window_r_x = rxcurrent + margin
                    window_r_y = rycurrent - ((window + 1) * window_h)

                    cv2.rectangle(img, (window_l_x, window_l_y), (window_r_x, window_r_y), (0, 150, 150), 2)
                    cv2.rectangle(img, (window_l_x - int(w * 0.43), window_l_y), (window_r_x - int(w * 0.43), window_r_y), (150, 150, 0), 2)

                    right_lines = ((nonx < window_r_x) & (nonx > window_l_x) & (nony < window_r_y) & (nony > window_l_y)).nonzero()[0]

                    if (len(right_lines) > minpix):
                        rxcurrent = np.int(np.mean(nonx[right_lines]))
                        rycurrent = np.int(np.mean(nony[right_lines]))

        cv2.imshow('img', img)

if __name__ == "__main__":
    line = LineDetect()
    cap = cv2.VideoCapture('org2.avi')
    while cap.isOpened():
        kernel_size = 3
        low_th = 140
        high_th = 180
        threshold_value = 160
        value = 255
        dila_ker = np.ones((5, 5), np.uint8)

        ret, img = cap.read()

        if ret:
            h = img.shape[0]
            w = img.shape[1]

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
            edge = cv2.Canny(blur, low_th, high_th)
            src = np.float32([[140, 320],
                              [540, 310],
                              [-350, 420],
                              [1020, 410]])

            dst = np.float32([[0, 0],
                              [w, 0],
                              [0, h],
                              [w, h]])
            M = cv2.getPerspectiveTransform(src, dst)
            the = cv2.threshold(edge, threshold_value, value, cv2.THRESH_BINARY)[1]
            warp = cv2.warpPerspective(the, M, (w, h), flags=cv2.INTER_LINEAR)
            dila = cv2.dilate(warp, dila_ker, iterations=1)
            line.main(dila)