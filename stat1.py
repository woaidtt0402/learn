# encoding=utf-8

import numpy as np
from scipy import stats
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn


def calc_statistics(x):
    n = x.shape[0]

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0

    for i in x:
        m1 += i
        m2 += i ** 2
        m3 += i ** 3
        m4 += i ** 4

    m1 = m1 / n
    m2 = m2 / n
    m3 = m3 / n
    m4 = m4 / n

    sigma = math.sqrt(m2 - m1 * m1)
    skew = (m3 + 2 * m1 ** 3 - 3 * m2 * m1) / sigma ** 3
    kurtosis = (m4 - 4 * m1 * m3 + 6 * m1 * m1 * m2 - 4 * m1 ** 3 * m1 + m1 ** 4) / sigma ** 4 - 3

    print('手动计算均值、标准差、偏度、峰度: ', m1, sigma, skew, kurtosis)

    m1 = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    skew = stats.skew(x)
    kurtosis = stats.kurtosis(x)

    print('库函数计算均值、标准差、偏度、峰度: ', m1, sigma, skew, kurtosis)

    return m1, sigma, skew, kurtosis


if __name__ == '__main__':
    d = np.random.randn(10000)
    print('d = ', d)
    mu, sigma, skew, kurtosis = calc_statistics(d)

    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(num=1, facecolor='w')
    y1, x1, dummy = plt.hist(d, bins=50, normed=True, color='g', alpha=0.75)
    print('y1 = ', y1)
    print('x1 = ', x1)
    print('dummy = ', dummy)
    t = np.arange(x1.min(), x1.max(), 0.05)
    y = np.exp(-t ** 2 / 2) / math.sqrt(2 * math.pi)
    plt.plot(t, y, 'r-', lw=2)
    plt.title('高斯分布，样本个数：%d' % d.shape[0])
    plt.grid(True)
    plt.show()

    d = np.random.randn(100000, 2)
    # mu, sigma, skew, kurtosis = calc_statistics(d)

    # 二维图像
    N = 30
    density, edges = np.histogramdd(d, bins=[N, N])
    print('density = ', density)
    print('edges = ', edges)
    density /= density.max()
    x = y = np.arange(N)

    t = np.meshgrid(x, y)
    print(t)

    fig = plt.figure(facecolor='w')
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(t[0], t[1], density, c='r', s=50*density, marker='o', depthshade=True)
    ax.plot_surface(t[0], t[1], density, cmap=cm.Accent, rstride=1, cstride=1, alpha=0.9, lw=0.75)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('二元高斯分布，样本个数：%d' % d.shape[0], fontsize=15)
    plt.tight_layout(0, 1)
    plt.show()

