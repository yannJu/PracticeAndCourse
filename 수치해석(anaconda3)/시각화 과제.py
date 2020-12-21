#소감 : 약 20개정도의 예제를 직접 타이핑해보고 실습해 보면서,
#우리가 수기로 ppt등과 같은 프로그램을 통해 그래프를 만들거나
#하는 것 보다, 수치를 정확하게 표현할 수 있고, 공식을 통해
#오차를 최소화 하여 시각화 할 수 있을 것 같습니다.
#조금 더 익숙해지고 손에 익게 되면 편하게 수치를 표현 할 수 있다는
#생각이 들었습니다.

# this code is designed for the difference comparison
# between euler and original method

# import numpy as np
# import matplotlib.pyplot as plt
#
# g=9.8
# cd=0.25
# m=68
#
# v0=0
# v1=(1-0)*(g-cd/m*v0**2)+v0
# v2=(2-1)*(g-cd/m*v1**2)+v1
# v3=(3-2)*(g-cd/m*v2**2)+v2
# v4=(4-3)*(g-cd/m*v3**2)+v3
#
# time=np.arange(0, 5)
# vel=np.array([v0, v1, v2, v3, v4])
#
#
# #  original method
#
# vel_o=np.sqrt(g*m/cd)*np.tanh(np.sqrt(g*cd/m)*time)
#
#
# plt.figure(1)
# plt.plot(time, vel, '-b1', label='euler')
# plt.plot(time,  vel_o, '-ro', label='differential')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.grid(True)
# plt.xlabel('time')
# plt.ylabel('velocity by euler and differential')
# plt.show()

