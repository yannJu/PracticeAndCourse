import cv2
import numpy as np

cap = cv2.VideoCapture('canny2.avi')

while cap.isOpened():
    #video read
    ret, img = cap.read() #ret : video가 cap되고 있는지, img : 캡쳐된 이미지

    h = img.shape[0] #img의 높이
    w = img.shape[1] #img의 넓이

    threshold_value = 85
    value = 255

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #threshold를 위해 3채널 이미지를 gray로 변환해준다
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    the = cv2.threshold(gray, threshold_value, value, cv2.THRESH_BINARY)[1]
    #threshold(img, 픽셀문턱값, 문턱값보다 클 때 적용되는 최대값, 문턱값 적용 방법)
    #threshold_value이상의 값은 value값으로 적용된다.
    #cv2.THRESH_BINARY : 픽셀값이 threshold_value보다 크면 value, 작으면 0
    #cv2.THRESH_TRUNC : 픽셀값이 threshold_value보다 크면 threshold, 작으면 유지
    #cv2.THRESH_TOERO : 픽셀값이 threshold_value보다 크면 유지, 작으면 0

    cv2.imshow('gray', gray)
    #--------warp

    src = np.float32([[0, h * 0.73],
           [w * (-0.15), h * 0.8],
           [w * 1.07, h * 0.8],
           [w * 0.98, h * 0.73]]) #시계반대방향 (좌상, 좌하, 우하, 우상)
    dst = np.float32([[0, 0],
           [0, h],
           [w, h],
           [w, 0]])
    # dst = np.float32([[w * 0.29, 0],
    #        [w * 0.3, h * 0.88],
    #        [w * 0.56, h * 0.88],
    #        [w * 0.65, h * (-0.1)]])

    M = cv2.getPerspectiveTransform(src, dst) #기하학적 변형된 행렬
    wap = cv2.warpPerspective(the, M, (w, h), flags=cv2.INTER_LINEAR) #M을 이용하여 변환

    #cv2.imshow('wap', wap)
    #-------sliding window

    wap = np.dstack((wap, wap, wap)) * 255 #Gray이므로, 3채널로 변환
    window_h = 5
    nwindows = 30
    margin = 20
    pixels = 10
    dflag = None #window의 높이는 5, 갯수는 30

    current_x = 0
    current_y = 0 #차선의 좌표 평균값

    low_x = 0
    high_x = 0
    low_y = 0
    high_y = 0 #window를 그리기 위한 사각형 좌표값

    non = wap.nonzero()
    nony = non[0]
    nonx = non[1] #차선을 인식하기 위하여, nonzero인 부분의 인덱스를 담은 배열

    left_non = []
    right_non = [] #왼쪽차선, 오른쪽 차선을 일정한 범위내에서 판별 하기 위한 배열

    left_non = ((nonx >= w * 0.17) & (nony >= h * 0.88) & (nonx <= w * 0.28)).nonzero()[0] #왼쪽차선을 판단하는 범위
    right_non = ((nonx >= w * 0.76) & (nony >= h * 0.88) & (nonx <= w * 0.86)).nonzero()[0] #오른쪽 차선을 판단하는 범위

    if (len(left_non) > pixels): #왼쪽의 pixel의 갯수가 10 이상인 경우
        dflag = 1 #왼쪽차선으로 인식
        current_x = np.int(np.mean(nonx[left_non]))
        current_y = np.int(np.mean(nony[left_non])) #current좌표를 지정
    elif (len(right_non) > pixels): #오른쪽의 pixel의 갯수가 10 이상인 경우
        dflag = 2 #오른쪽 차선으로 인식
        current_x = np.int(np.mean(nonx[right_non]))
        current_y = np.int(np.mean(nony[right_non]))
    else: dflag = 3

    # cv2.circle(wap, (current_x, current_y), 3, (0, 255, 255), 3)
    # cv2.imshow('circle', wap)
    if (dflag != 3): #차선이 검출 되었을 때
        for window in range(0, nwindows):
            low_x = current_x - margin #좌상의 x좌표
            high_x = current_x + margin #우하의 x좌표
            low_y = current_y - (window + 1) * window_h #좌상의 y좌표, 현재 current보다 윈도우의 크기만큼 높은 좌표를 찍는다
            high_y = current_y - window * window_h #우하의 y좌표, y좌표를 계속 올려야 하므로 빼준다
            if dflag == 1: #왼쪽차선이 검출되었을 때
                cv2.rectangle(wap, (low_x, low_y), (high_x, high_y), (100, 200, 0), 1)
                #cv2.rectangle(img, (좌상 좌표), (우하 좌표), 선색, 선두께)
                cv2.rectangle(wap, (low_x + int(w * 0.58), low_y), (high_x + int(w * 0.58), high_y), (70, 10, 200), 1) #윈도우 표시

                left_non = ((nonx >= low_x) & (nony >= low_y) & (nonx <= high_x) & (nony <= high_y)).nonzero()[0] #왼쪽 차선을 윈도우 내에서 판단

                if (len(left_non) > pixels):
                    current_x = np.int(np.mean(nonx[left_non])) #왼도우 범위내에 pixel이 10 이상인 경우, current_x의 값을 평균을 통해 초기화 해준다
            else:
                cv2.rectangle(wap, (low_x - int(w * 0.58), low_y), (high_x - int(w * 0.58), high_y), (100, 200, 0), 1)
                cv2.rectangle(wap, (low_x, low_y), (high_x, high_y), (70, 10, 200), 1)

                right_non = ((nonx >= low_x) & (nony >= low_y) & (nonx <= high_x) & (nony <= high_y)).nonzero()[0]

                if (len(right_non) > pixels) :
                    current_x = np.int(np.mean(nonx[right_non]))
            #print("D : " , dflag)

    cv2.imshow('rec', wap)
    cv2.imshow('hsv', hsv)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break