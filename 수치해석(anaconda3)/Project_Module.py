import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

class Opty:
    def __init__(self):
        self.X_min = 0
        self.X_max = 0
        self.alpha = 0.0038
    #-----------데이터 생성
    def createData(self):
        # print("Min : ", self.X_min)
        # print("Max : ", self.X_max)
        np.random.seed(seed = 1)
        self.X_min = 4
        self.X_max = 30 #상한 하한
        # print("Min : ", self.X_min)
        # print("Max : ", self.X_max)
        X_n = 16 #표본 개수?
        X = 5 + 25 * np.random.rand(X_n)
        Prm_c = [170, 108, 0.2]
        T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)

        # print(X)
        # print(np.round(X, 2))
        # print(np.round(T, 2))

        #data graph------------
        plt.figure(figsize= (4, 4))
        plt.plot(X, T, marker = 'o', linestyle = 'None', markeredgecolor = 'black', color = 'cornflowerblue')
        plt.xlim(self.X_min, self.X_max)
        plt.grid(True)
        plt.show()

        return X, T

    # 평균 오차함수--------
    def mse_line(self, x, t, w):
        y = w[0] * x + w[1]
        mse = np.mean((y - t) ** 2)
        #print(mse)
        return mse

    # 표시 ---------------
    def graphLine(self, xx0, xx1, J):

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
        #plt.show()

    # -------------평균제곱오차의 기울기
    def dmse_line(self, x, t, w):
        y = w[0] * x + w[1]
        d_w0 = 2 * np.mean((y - t) * x)
        d_w1 = 2 * np.mean(y - t)
        #print("W0 : ", type(d_w0))
        # print("W1 : ", d_w1)
        return d_w0, d_w1

    # ------------SGD
    def fit_line_num(self, x, t):
        w_init = [10.0, 165.0]
        #alpha = 0.0038  # 학습률
        # alpha = 0.001
        # alpha = 0.002
        # alpha = 0.003
        # alpha = 0.004
        # alpha = 0.005
        # alpha = 0.0035
        i_max = 100000  # 최대 반복수
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
            cnt += 1
            tmp = rj
            rj = random.randint(1, len(x))
            dmse = self.dmse_line(x, t, w_i[tmp])  # 샘플링?
            #print(dmse)
            #print(w_i[tmp])
            w_i[rj, 0] = w_i[tmp, 0] - self.alpha * dmse[0]
            w_i[rj, 1] = w_i[tmp, 1] - self.alpha * dmse[1]  # 81-82 다음 기울기 등 구하는것
            # print("#{}".format(i + 2))
            # print(w_i)
            if max(np.absolute(dmse)) < eps:
                break
        w0 = w_i[rj, 0]
        w1 = w_i[rj, 1]
        w_i = w_i[:rj, :]
        return w0, w1, dmse, w_i, cnt

    def show_line(self, w):
        xb = np.linspace(self.X_min, self.X_max, 100)
        y = w[0] * xb + w[1]
        plt.plot(xb, y, color=(.5, .5, .5), linewidth=4)
        #plt.show()

    def f2(self, x, y):
        return (1 - x) ** 2 + 100.0 * (y - x ** 2) ** 2

    def f2g(self, w):
        g_w0 = np.mean(2.0 * (w[0] - 1) - 400.0 * w[0] * (w[1] - w[0]**2))
        g_w1 = np.mean(200.0 * (w[1] - w[0]**2))
        return g_w0, g_w1

    def graphF2(self, x, y, z):
        self.alpha = 0.00017896325

        level = np.logspace(-1, 3, 10)
        plt.contourf(x, y, z, alpha = 0.2, levels=level)
        plt.contour(x, y, z, colors="green",levels = level)
        plt.plot(1, 1, 'ro', markersize=10)
        plt.xlim(-4, 4)
        plt.ylim(-3, 3)
        plt.xticks(np.linspace(-4, 4, 9))
        plt.yticks(np.linspace(-3, 3, 7))

        s = 0.95

        i_max = 100000
        w_init = [-1, -1]
        w_i = np.zeros([i_max, 2])
        # print("#1")
        # print(w_i)
        w_i[0, :] = w_init
        # print("#2")
        # print(w_i)
        rj = 0
        cnt = 0
        for i in range(0, i_max):
            cnt += 1
            tmp = rj
            rj = random.randint(1, len(x))
            #print(w_i[tmp])
            g = self.f2g(w_i[tmp])
            #dmse = self.dmse_line(x, y, w_i[tmp])  # 샘플링?
            print(w_i[tmp])
            # print("w_i type : ", type(w_i))
            # print("g type : ", type(g))
            if (i == 0) :
                w_i[rj, 0] = self.alpha * g[0]
                w_i[rj, 1] = self.alpha * g[1]
            else :
                w_i[rj, 0] = w_i[tmp, 0] - self.alpha * g[0]
                w_i[rj, 1] = w_i[tmp, 1] - self.alpha * g[1] # 81-82 다음 기울기 등 구하는것
            # print("#{}".format(i + 2))
            # print(w_i)
            print(w_i[tmp, 0], w_i[tmp, 1])

        # w0 = w_i[rj, 0]
        # w1 = w_i[rj, 1]
        # w_i = w_i[:rj, :]
        #return w0, w1, dmse, w_i, cnt

            if (0.99 <= w_i[tmp, 0] <= 1.1 and 0.99 <= w_i[tmp, 1] <= 1.1):
                break
        print(w_i)
        for i in range(1, cnt):
            plt.arrow(w_i[i - 1, 0], w_i[i - 1, 1], w_i[i, 0] - w_i[i - 1, 0], w_i[i, 1] - w_i[i - 1, 1], head_width=0.04,
                      head_length=0.04, fc='k', ec='k', lw=2)

        plt.ylabel("$y$")
        plt.xlabel("$x$")
        plt.title("2차원 로젠브록 함수 $f(x,y)$")
        plt.show()


if __name__ == '__main__':
    op = Opty()
    X ,T = op.createData()
    # cal-----------------
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
    for i in range(xn):
        for j in range(xn):
            J[j, i] = op.mse_line(X, T, (x0[i], x1[j])) #평균 오차함수 구하기
    # 그래프 그리기
    op.graphLine(xx0, xx1, J)
    #d_w = dmse_line(X, T, [10, 165])
    # print(np.round(d_w, 1))
    #등고선 그리기
    cont = plt.contour(xx0, xx1, J, 30, colors = 'black', levels = (100, 1000, 10000, 100000))
    cont.clabel(fmt = '%1.0f', fontsize = 8)
    plt.grid(True)
    W0, W1, dMSE, W_history, cnt = op.fit_line_num(X, T)

    print('반복횟수 {0}'.format(cnt))
    print('W = [{0:.6f}, {1:.6f}]'.format(W0, W1))
    print('dMSE = [{0:.6f}, {1:.6f}]'.format(dMSE[0], dMSE[1]))
    print('MSE = {0:.6f}'.format(op.mse_line(X, T, [W0, W1])))
    plt.plot(W_history[:, 0], W_history[:, 1], '.-', color = 'gray', markersize = 10, markeredgecolor = 'cornflowerblue')
    plt.show()

    #line + main

    plt.figure(figsize = (4, 4))
    W = np.array([W0, W1])
    mse = op.mse_line(X, T, W)
    print("w0 = {0:.3f}, w1 = {1:.3f}".format(W0, W1))
    print("SD = {0:.3f} cm".format(np.sqrt(mse)))
    op.show_line(W)
    plt.plot(X, T, marker = 'o', linestyle = "None", color = 'cornflowerblue', markeredgecolor = 'black')
    plt.xlim(op.X_min, op.X_max)
    plt.grid(True)
    plt.show()

    #Rosenbrock
    L_x = np.linspace(-4, 4, 800)
    L_y = np.linspace(-3, 3, 600)
    LXX, LYY = np.meshgrid(L_x, L_y)
    Z = op.f2(LXX,LYY)
    op.graphF2(LXX,LYY, Z)