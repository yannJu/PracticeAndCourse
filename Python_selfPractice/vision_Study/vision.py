#사진 먼저 캡쳐해서 roi 따서 허프라인....... 차선인식 해서 오기............
#(전처리) ~> 블러, 캐니, edge / filtering
#image cv2로 받아서 채널이 몇개인지, height, width출력 , gray, blur, canny(이미지를 여러장 만들어서, thread조절해보기), warp(roi빼고,)
import cv2
import numpy as np

img = cv2.imread('solidWhiteCurve.jpg') #사진 읽어오기
height = img.shape[1] #높이
width = img.shape[0] #너비
#print channel, height, width ----------
print("Height : ", height)
print("Width : ", width) #H, W
print(len(img[0][0])) #채널
#---------------------------------------

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray scale, 3channel 을 1channel로, 흑백으로 변환
#cvtColor - (변환할 이미지, 변환옵션(?) ~ 원본 이미지 색상2결과이미지 색상)
kernel_size = 5
blur = cv2.GaussianBlur(gray, (kernel_size,kernel_size), 0) #blur, noise제거, grayscale이 된 이미지를, 커널사이즈를 조절하여 노이즈를 제거하여줌
#GaussianBlur - (변환할 이미지, (kernelxkernel(홀수)), SigmaX)
#한픽셀을 kernel x kernel 의 평균값
#kernel ~> 각좌표 주변을 포함한 작은 공간
#sigmaX ~>
#테두리 외삽법........
# cv2.imshow('img', img)
# cv2.imshow('blur', blur)
# cv2.waitKey(0)

#---------------------------------------
low_th = 120 #하한값
high_th = 180 #상한값
#edge = cv2.Canny(blur, 100, 180) #canny
#edge = cv2.Canny(blur, 110, 160) #canny
edge = cv2.Canny(blur, low_th, high_th) #canny, 윤곽선 표시, low_th이하의 값은 버리고, high_th이상의 값을 채택, 사이의 값은 연결된 선인 경우 채택
#Canny - (원본,하한, 상한, 커널크기, l2그레디언트)
#그레디언트 T/F에 따라 크기 계산 식이 다름 F일시 근사값(default)
cv2.imshow('edge', edge) #canny화면 출력

#---------------------------------------

#warper
# (383, 381) (610, 381)
# (281, 460) (752, 460)
# 960 x 540, 650
#
# (360, 381) (650, 381)
# (260, 460) (760, 460)

w = 960
h = 540 #전체 사진의 넓이와 높이
# roi = edge[:, 260:800]  # roi영역 설정

# cv2.imshow('roi', roi)
# cv2.waitKey(0)

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
wap = cv2.warpPerspective(edge, M, (edge.shape[1], edge.shape[0]), flags = cv2.INTER_LINEAR) #변환하여 img반환, img를 transform한 행렬을 이용하여 warp하여 준다.
#cv2.warpPerspective(원본이미지, 변환한 행렬, (결과 이미지 너비, 결과 이미지 높이))

cv2.imshow('wap', wap) #wap화면 출력
#cv2.waitKey(0)
#----------------------------------
#hough
def get_X(y, a, b):
    return (y - b) // a

out_img = np.dstack((wap, wap, wap)) * 255 #3채널로 변경하여 주기 위해
thr = 140 #임계값 설정
minLineLength = 100
maxLineLength = 0
the = 100
lines = cv2.HoughLinesP(wap, 1, np.pi / 180, the, minLineLength, maxLineLength)
    #houghlinesp - (이미지, 거리, 각도, 임계값, 선의 최소길이(최소 이 길이 이상인 경우 선으로 허용), 선의 최대길이(선-선))
    #thread 가 클수록 정확도가 커지고, 작ㅇ아지면 정확도는 떨어지지만 많은 선 검출 가능

left = [] #wid / 2보다 작을 경우 left로 인식하고, left리스트에 담음
right = [] #wid / 2보다 클 경우 right로 인식하고, right리스트에 담음

left_x1 = 0
left_x2 = 0
left_y1 = 0
left_y2 = 0 #left (x1,y1) (x2, y2)

right_x1 = 0
right_x2 = 0
right_y1 = 0
right_y2 = 0 #right (x1,y1) (x2, y2)

#290

for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        if (0 <= x1 < w // 2 or 0 <= x2 < w // 2): left.append([x1, y1, x2, y2])
        else: right.append([x1, y1, x2, y2]) #x1혹은 x2가 w/2보다 작은경우 left/ 큰경우 right 리스트에 담아준다([x1, y1, x2, y2]배열로)

if len(left) > 0: #left에 최소 1개의 좌표가 존재할 경우
    for i in left:
        left_x1 += i[0]
        left_x2 += i[2]
        left_y1 += i[1]
        left_y2 += i[3] #[x1, y1, x2, y2]의 순으로 되어있기 때문에 각각의 변수에 더해준다

    left_x1 = left_x1 // len(left)
    left_x2 = left_x2 // len(left)
    left_y1 = left_y1 // len(left)
    left_y2 = left_y2 // len(left) #각변수를 left의 리스트의 크기로 나누어 줌으로써 평균을 구함

    if (left_x1 == left_x2 or left_y1 == left_y2): #만약 x좌표 혹은 y좌표의 평균이 같을 경우, 그냥 선을 그어주도록 한다
        cv2.line(out_img, (left_x1, 0), (left_x1, height - 1), (0, 0, 255), 3)
    else:
        left_a = (left_y2 - left_y1) // (left_x2 - left_x1) #두 좌표를 이용하여 기울기를 구함
        left_b = -left_a * left_x1 + left_y1 #a와 x1, y1좌표를 이용하여 y좌표를 구함

        min_left_x = get_X(0, left_a, left_b) #(0 - left_b) // left_a #y가 0일때의 x좌표
        max_left_x = get_X(height - 1, left_a, left_b) #(height - 1 - left_b) // left_a #y가 height - 1일때의 x좌표

        cv2.line(out_img, (min_left_x, 0), (max_left_x, height - 1), (0, 0, 255), 3) #min, max를 이용하여 선을 그어줌

if len(right) > 0: #최소 1개의 right좌표가 존재할 경우
    for i in right:
        right_x1 += i[0]
        right_x2 += i[2]
        right_y1 += i[1]
        right_y2 += i[3] #[x1, y1, x2, y2] 의 순으로 되어있기 때문에 각각의 변수에 더해줌

    right_x1 = right_x1 // len(right)
    right_x2 = right_x2 // len(right)
    right_y1 = right_y1 // len(right)
    right_y2 = right_y2 // len(right) #각변수를 right의 리스트의 크기로 나누어 평균 구함

    if (right_x1 == right_x2 or right_y1 == right_y2): #x혹은 y의 좌표의 평균이 같을 경우
        cv2.line(out_img, (right_x1, 0), (right_x1, height - 1), (0, 0, 255), 3) #좌표 하나를 이용하여 선 긋기
    else:
        right_a = (right_y2 - right_y1) // (right_x2 - right_x1) #두 좌표의 평균을 이용하여 기울기 구함
        right_b = -right_a * right_x1 + right_y1 #기울기와 좌표를 이용하여 y절편을 구함

        min_right_x = get_X(0, right_a, right_b) #(0 - right_b) // right_a
        max_right_x = get_X(height - 1, right_a, right_b)#(height - 1 - right_b) // right_a # y = 0 , y = height - 1 일때의 x좌표를 구함

        cv2.line(out_img, (min_right_x, 0), (max_right_x, height - 1), (0, 0, 255), 3) #min, max좌표를 이용하여 선 긋기
# print("lines : ", lines)
# for i in range(len(lines)):
#     for x1, y1, x2, y2 in lines[i]:
#         if (x1 > 500):
#             xx2 += x1
#             x2_cnt += 1
#         elif (x1 < 500):
#             xx1 += x1
#             x1_cnt += 1
#
#         if (x2 > 500):
#             xx2 += x2
#             x2_cnt += 1
#         elif (x2 < 500):
#             xx1 += x2
#             x1_cnt += 1
#         print("x1 : ", x1_cnt, "x2 : ", x2_cnt)
#         cv2.circle(out_img, (((xx2/x2_cnt) + (xx1/x1_cnt)) / 2, 500, (0, 0, 255), 2))
#         cv2.line(out_img, (x1, y1), (x2, y2), (0, 255, 0), 3)


#lines = cv2.HoughLines(wap, 1, np.pi/180, thr)
#HoughLines로 r, theta값을 구함
# for line in lines:
#     r, theta = line[0]
#     if (r > 0 and (np.pi * 1/10 < theta < np.pi * 4/10)):
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * r
#         y0 = b * r
#         x1 = int(x0 + 1000*(-b))￼
#         y1 = int(y0 + 1000*a)
#         x2 = int(x0 - 1000*(-b))
#         y2 = int(y0 - 1000*a)
#
#         cv2.line(out_img, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imshow('hough', out_img)
cv2.waitKey(0)
#----------------------------------
#x locate
#490