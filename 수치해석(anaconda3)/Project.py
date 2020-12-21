import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

#-----------데이터 생성
np.random.seed(seed = 1)
X_min = 4
X_max = 30 #상한 하한
X_n = 16 #표본 개수?
X = 5 + 25 * np.random.rand(X_n)
Prm_c = [170, 108, 0.2]
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)
np.savez('project.npz', X = X, X_min = X_min, X_max = X_max, X_n = X_n, T = T)

#list
#print(X)
#print(np.round(X, 2))
#print(np.round(T, 2))

#data graph------------
plt.figure(figsize= (4, 4))
plt.plot(X, T, marker = 'o', linestyle = 'None', markeredgecolor = 'black', color = 'cornflowerblue')
plt.xlim(X_min, X_max)
plt.grid(True)
plt.show()

#평균 오차함수--------
def mse_line(x, t, w):
    y = w[0] * x + w[1]
    mse = np.mean((y - t)**2)
    return mse

#cal-----------------
xn = 100
w0_range = [-25, 25]
w1_range = [120, 170]
x0 = np.linspace(w0_range[0], w0_range[1], xn)
x1 = np.linspace(w1_range[0], w1_range[1], xn)
xx0, xx1 = np.meshgrid(x0, x1)
J = np.zeros((len(x0), len(x1)))
for i in range(xn):
    for j in range(xn):
        J[j, i] = mse_line(X, T, (x0[i], x1[j]))

#표시 ---------------

plt.figure(figsize = (9.5, 4))
plt.subplots_adjust(wspace = 0.5)
ax = plt.subplot(1, 2, 1, projection = '3d')
ax.plot_surface(xx0, xx1, J, rstride = 10, cstride = 10, alpha = 0.3, color = 'blue', edgecolor = 'black')
ax.set_xticks([-20, 0, 20])
ax.set_yticks([120, 140, 160])
ax.view_init(20, -60)

plt.subplot(1, 2, 2)
cont = plt.contour(xx0, xx1, J, 30, colors = 'black', levels = [100, 1000, 10000, 100000])
cont.clabel(fmt = '%1.0f', fontsize = 8)
plt.grid(True)
plt.show()

#-------------평균제곱오차의 기울기
def dmse_line(x, t, w):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y - t) * x)
    d_w1 = 2 * np.mean(y - t)
    return d_w0, d_w1

d_w = dmse_line(X, T, [10, 165])
#print(np.round(d_w, 1))

#------------SGD

def fit_line_num(x, t):
    w_init = [10.0, 165.0]
    alpha = 0.0038 #학습률
    #alpha = 0.001
    #alpha = 0.002
    #alpha = 0.003
    #alpha = 0.004
    #alpha = 0.005
    #alpha = 0.0035
    i_max = 100000 #최대 반복수
    eps = 0.1
    w_i = np.zeros([i_max, 2])
    # print("#1")
    # print(w_i)
    w_i[0, :] = w_init
    # print("#2")
    # print(w_i)
    rj = 1
    cnt = 0
    for i in range(1, i_max):
        cnt +=1
        tmp = rj
        rj = random.randint(1, len(x))
        dmse = dmse_line(x, t, w_i[tmp]) #샘플링?
        print(w_i[tmp])
        w_i[rj, 0] = w_i[tmp, 0] - alpha * dmse[0]
        w_i[rj, 1] = w_i[tmp, 1] - alpha * dmse[1] #81-82 다음 기울기 등 구하는것
        # print("#{}".format(i + 2))
        # print(w_i)
        if max(np.absolute(dmse)) < eps:
            break
    w0 = w_i[rj, 0]
    w1 = w_i[rj, 1]
    w_i = w_i[:rj, :]
    return w0, w1, dmse, w_i, cnt

#main

plt.figure(figsize = (4, 4))
xn = 100
w0_range = [-25, 25]
w1_range = [120, 170]
x0 = np.linspace(w0_range[0], w0_range[1], xn)
#print(x0)
x1 = np.linspace(w1_range[0], w1_range[1], xn)
#print(x1)
xx0, xx1 = np.meshgrid(x0, x1)
#print(xx0)
#print(xx1)
J = np.zeros((len(x0), len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        J[i1, i0] = mse_line(X, T, (x0[i0], x1[i1]))
cont = plt.contour(xx0, xx1, J, 30, colors = 'black', levels = (100, 1000, 10000, 100000))
cont.clabel(fmt = '%1.0f', fontsize = 8)
plt.grid(True)

W0, W1, dMSE, W_history, cnt = fit_line_num(X, T)

print('반복횟수 {0}'.format(cnt))
print('W = [{0:.6f}, {1:.6f}]'.format(W0, W1))
print('dMSE = [{0:.6f}, {1:.6f}]'.format(dMSE[0], dMSE[1]))
print('MSE = {0:.6f}'.format(mse_line(X, T, [W0, W1])))
plt.plot(W_history[:, 0], W_history[:, 1], '.-', color = 'gray', markersize = 10, markeredgecolor = 'cornflowerblue')
plt.show()

#line + main

def show_line(w):
    xb = np.linspace(X_min, X_max, 100)
    y = w[0] * xb + w[1]
    plt.plot(xb, y, color = (.5, .5, .5), linewidth = 4)

plt.figure(figsize = (4, 4))
W = np.array([W0, W1])
mse = mse_line(X, T, W)
print("w0 = {0:.3f}, w1 = {1:.3f}".format(W0, W1))
print("SD = {0:.3f} cm".format(np.sqrt(mse)))
show_line(W)
plt.plot(X, T, marker = 'o', linestyle = "None", color = 'cornflowerblue', markeredgecolor = 'black')
plt.xlim(X_min, X_max)
plt.grid(True)
plt.show()