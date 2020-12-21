import cv2
import numpy as np

s_img = cv2.imread('solidWhiteCurve.jpg')
s_height = s_img.shape[1]
s_weight = s_img.shape[0]

#-------------------------------------------
#gray -> blur -> canny -> warp -> sliding

s_gray = cv2.cvtColor(s_img, cv2.COLOR_BGR2GRAY)

kernel_size = 5
s_blur = cv2.GaussianBlur(s_gray, (kernel_size, kernel_size), 0)

low_th = 120
high_th = 180
s_canny = cv2.Canny(s_blur, low_th, high_th)

cv2.imshow("before", s_canny)
#cv2.waitKey(0)
#------------------------------------------
#960x540

w = 960
h = 540

src = np.float32([[w * 0.33, h * 0.7],
                 [w * 0.27, h * 0.851],
                 [w, h * 0.851],
                 [w * 0.677, h * 0.7]]) #변환지점 좌표
dst = np.float32([[w * 0.075, 0],
                 [w * 0.2, h],
                 [w, h],
                 [w * 0.85, 0]]) #지정해줄 좌표
#src와 dst는 좌표의 순서가 서로 같아야 하고 float32
M = cv2.getPerspectiveTransform(src, dst) #변환행렬 / 원본좌표순서, 결과좌표순서
wap = cv2.warpPerspective(s_canny, M, (s_canny.shape[1], s_canny.shape[0]), flags = cv2.INTER_LINEAR) #변환하여 img반환, img를 transform한 행렬을 이용하여 warp하여 준다.
#cv2.warpPerspective(원본이미지, 변환한 행렬, (결과 이미지 너비, 결과 이미지 높이))

cv2.imshow('wap', wap) #wap화면 출력
#cv2.waitKey(0)
#----------------------------------------
#sliding window

slide = np.dstack((wap, wap, wap)) * 255
# cv2.imshow('slide', slide)
# cv2.waitKey(0)
slide_h = wap.shape[0]
slide_w = wap.shape[1]

window_h = 5
nwindows = 30
min_pix = 10
margin = 20
y_current = 0
x_current = 0

dflag = None

s_non = wap.nonzero()
nony = s_non[0]
nonx = s_non[1]

left_idx = []
right_idx = []

left_idx = ((nonx >= w * 0.18) & (nony >= h * 0.88) & (nonx <= w * 0.28)).nonzero()[0]
right_idx = ((nonx >= w * 0.7) & (nony >= h * 0.88) & (nonx <= w * 0.8)).nonzero()[0]

if (len(left_idx) >= min_pix):
    dflag = 1
    x_current = np.int(np.mean(nonx[left_idx]))
    y_current = np.int(np.mean(nony[left_idx]))

elif (len(right_idx) >= min_pix):
    dflag = 2
    x_current = np.int(np.mean(nonx[right_idx]))
    y_current = np.int(np.mean(nony[right_idx]))

else:
    dflag = 3

# cv2.circle(slide, (x_current, y_current), 3, (0, 0, 255), 3)
# cv2.imshow('circle', slide)
# cv2.waitKey(0)

if dflag != 3:
    for w in range(0, nwindows):
        if (dflag == 1):
            window_x_min = x_current - margin
            window_x_max = x_current + margin
            window_y_min = y_current - window_h * (w + 1)
            window_y_max = y_current - window_h * w

            # print(window_y_min)

            cv2.rectangle(slide, (window_x_min, window_y_min), (window_x_max, window_y_max), (120, 150, 0), 2)
            cv2.rectangle(slide, (window_x_min + int(slide_w * 0.53), window_y_min), (window_x_max + int(slide_w * 0.53) , window_y_max), (0, 150, 120), 2)
        elif (dflag == 2):
            window_x_min = x_current - margin
            window_x_max = x_current + margin
            window_y_min = y_current - window_h * (w + 1)
            window_y_max = y_current - window_h * w

            cv2.rectangle(slide, (window_x_min - int(slide_w * 0.53), window_y_min), (window_x_max - int(slide_w * 0.53), window_y_max), (120, 150, 0), 2)
            cv2.rectangle(slide, (window_x_min, window_y_min), (window_x_max, window_y_max), (0, 150, 120), 2)

cv2.imshow('slide', slide)
cv2.waitKey(0)