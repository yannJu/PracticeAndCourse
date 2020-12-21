import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

# # 2차원 로젠브록 함수



import matplotlib.pyplot as plt



plt.figure(10)

ax = plt.axes()

ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

plt.show()





x, y = -1, -1

for i in range(5): # 5000

    g = f2g(x, y)

    plt.arrow(x, y, -s * mu * g[0], -s * mu * g[1],

              head_width=0.04, head_length=0.04, fc='k', ec='k', lw=2)

    x = x - mu * g[0]

    y = y - mu * g[1]



plt.xlim(-3, 3)

plt.ylim(-2, 2)

plt.xticks(np.linspace(-3, 3, 7))

plt.yticks(np.linspace(-2, 2, 5))

plt.xlabel("x")

plt.ylabel("y")

plt.title("최대경사법을 사용한 2차함수의 최적화" )

plt.show()



xx = np.linspace(0, 4, 800)

yy = np.linspace(0, 3, 600)

X, Y = np.meshgrid(xx, yy)

Z = f2(X, Y)



levels = np.logspace(-1, 4, 20)



plt.contourf(X, Y, Z, alpha=0.2, levels=levels)

plt.contour(X, Y, Z, colors="green", levels=levels, zorder=0)

plt.plot(1, 1, 'ro', markersize=10)



mu = 1.8e-3  # 스텝 사이즈

s = 0.95  # 화살표 크기



x, y = 1.5, 1.5

for i in range(15):

    g = f2g(x, y)

    plt.arrow(x, y, -s * mu * g[0], -s * mu * g[1],

              head_width=0.04, head_length=0.04, fc='k', ec='k', lw=2)

    x = x - mu * g[0]

    y = y - mu * g[1]



plt.xlim(0, 3)

plt.ylim(0, 2)

plt.xticks(np.linspace(0, 3, 4))

plt.yticks(np.linspace(0, 2, 3))

plt.xlabel("x")

plt.ylabel("y")

plt.title("최대경사법을 사용한 2차함수의 최적화 (진동 현상)" )

plt.show()