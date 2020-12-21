import cv2
import numpy as np

cap = cv2.VideoCapture('IMG_2520.MP4')#영상읽어오기

while cap.isOpened():
    ret, cv_image = cap.read()
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edge = cv2.Canny(blur, 140, 170)

    cv2.imshow("origin", cv_image)
    cv2.imshow("edge", edge)

#---------------------------------------

#warper
# 854 x 480
#   (100,450)
#   (200, 360)
    w = 854
    h = 480

    src = np.float32([[w * 0.23, h * 0.8],
                     [w * 0.12, h * 0.937],
                     [w * 0.93, h * 0.937],
                     [w * 0.72, h * 0.8]])
    dst = np.float32([[w * (-0.1), 0],
                     [0, h],
                     [w * 0.88, h],
                     [w * 0.85, 0]]) #warp좌표 , 지정좌표

    M = cv2.getPerspectiveTransform(src, dst)
    wap = cv2.warpPerspective(edge, M, (edge.shape[1], edge.shape[0]), flags = cv2.INTER_LINEAR)
#
    cv2.imshow('wap', wap)
#----------------------------------
    #차선 따기
    # rr = 0
    # th = 0 houghline 의 r theta
    out_img = np.dstack((wap, wap, wap)) * 255 #wap한 이미지를 3채널로 변경
    minLineLength = 100
    maxLineLength = 0
    the = 100
    lines = cv2.HoughLinesP(wap, 1, np.pi/180, the, minLineLength, maxLineLength)

    left = []
    right = [] #left, right(width를 기준으로) 좌표를 담음 2차원 배열으로, x,y좌표 두개씩

    #print(len(lines))

    # xx1 = 0
    # yy1 = 0
    # xx2 = 0
    # yy2 = 0 (1)

    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            # (1)
            # xx1 += x1
            # yy1 += y1
            # xx2 += x2
            # yy2 += y2
            print(lines[i])

            if (0 <= x1 < (w // 2) or 0 <= x2 < (w // 2)): left.append([x1, y1, x2, y2]) #왼쪽에 점이 있을 경우, left리스트에 담는다
            else: right.append([x1, y1, x2, y2]) #오른쪽에 점이 있을 경우, right리스트에 담는다

            cv2.line(out_img, (x1, y1), (x2, y2), (0, 255, 0), 3) #houghlineP를 하여 얻은 좌표들로 모든 직선을 긋는다

    # (1)
    # xx1 = xx1 // len(lines)
    # yy1 = yy1 // len(lines)
    # xx2 = xx2 // len(lines)
    # yy2 = yy2 // len(lines) #61 - 64 (x1, y1, x2, y2의 평균)
    #
    # a = (yy2 - yy1) // (xx2 - xx1) #기울기
    # b = -a * xx2 + yy2 #y절편
    #
    # min_x = (0 - b) // a
    # max_x = (h - 1 - b) // a

    left_x1 = 0
    left_x2 = 0
    left_y1 = 0
    left_y2 = 0 #left x1,x2/y1,y2

    right_x1 = 0
    right_x2 = 0
    right_y1 = 0
    right_y2 = 0 #right x1,x2/y1,y2

    if (len(left) > 0): #left 리스트에 좌표가 있을 경우(즉, left에서 점이 발견된 경우)
        for i in left:
            left_x1 += i[0]
            left_x2 += i[2]
            left_y1 += i[1]
            left_y2 += i[3] #left x1, x2, y1, y2의 평균을 구하기 위하여, 더해준다

        left_x1 = left_x1 // len(left)
        left_x2 = left_x2 // len(left)
        left_y1 = left_y1 // len(left)
        left_y2 = left_y2 // len(left) #left리스트의 크기로 나누어 평균을

        if (left_x1 == left_x2 or left_y1 == left_y2):
            cv2.line(out_img, (left_x1, 0), (left_x1, h - 1), (0, 0, 255), 2)
        else:
            left_a = (left_y2 - left_y1) // (left_x2 - left_x1) #기울기
            left_b = -left_a * left_x1 + left_y1 #y절편, left (x1, y1), (x2, y2)를 이용하여 기울기와 y절편을 구한다

            min_left_x = (0 - left_b) // left_a
            max_left_x = (h - 1 - left_b) // left_a #left좌표를 기준으로 최소높이와 최대높이를 구한다

            cv2.line(out_img, (min_left_x, 0), (max_left_x, h - 1), (0, 0, 255), 2) #min_left_x와 max_left_x를 통해 직선을 그어준다

    if (len(right) > 0): #right 리스트에 좌표가 있을 경우(right에서 점이 발견된 경우)
        for j in right:
            right_x1 += j[0]
            right_x2 += j[2]
            right_y1 += j[1]
            right_y2 += j[3] #right x1, x2, y1, y2의 평균을 구하기 위해 더해준다 (평균을 구하는 더 쉽고 정확한 방법은 ????? np사용 해보자ㅏㅏㅏ)

        right_x1 = right_x1 // len(right)
        right_x2 = right_x2 // len(right)
        right_y1 = right_y1 // len(right)
        right_y2 = right_y2 // len(right) #right의 리스트의 크기로 나누어 평균을 구한다

        if (right_x1 == right_x2 or right_y1 == right_y2):
            cv2.line(out_img, (right_x1, 0), (right_x1, h - 1), (0, 0, 255), 2)
        else:
            right_a = (right_y2 - right_y1) // (right_x2 - right_x1)  # 기울기
            right_b =  -right_a * right_x1 + right_y1#y절편

            min_right_x = (0 - right_b) // right_a #최소높이의 x좌표 ~> (x, 0)
            max_right_x = (h - 1 - right_b) // right_a #최대높이의 x좌표 ~> (x, height - 1)

            cv2.line(out_img, (min_right_x, 0), (max_right_x, h - 1), (0, 0, 255), 2) #min과 max좌표를 이용하여, 선 긋기
    #lines = cv2.HoughLines(wap, 1, np.pi/180, 140)
    #houghlines - (검출이미지, 거리, 각도, 임곗값, 거리약수, 각도약수, 최소각도, 최대각도)
    #houghlinesp - (이미지, 거리, 각도, 임계값, 선의 최소길이(최소 이 길이 이상인 경우 선으로 허용), 선의 최대길이(선-선))
    #thread 가 클수록 정확도가 커지고, 작ㅇ아지면 정확도는 떨어지지만 많은 선 검출 가능
    #  for line in lines:
    #     r, theta = line[0]
    #     rr += r
    #     th += theta
    #
    # re_r = np.float32(rr/len(lines))
    # re_t = np.float32(th/len(lines))
    # a = np.cos(re_t)
    # b = np.sin(re_t)
    # x0 = a*re_r
    # y0 = b*re_r
    # x1 = int(x0 + 1000*(-b))
    # y1 = int(y0 + 1000*a)
    # x2 = int(x0 - 1000*(-b))
    # y2 = int(y0 - 1000*a)

    cv2.imshow('hough', out_img)
# ----------------------------------
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break