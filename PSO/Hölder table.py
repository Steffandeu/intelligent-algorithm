import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def Holder_table(X_min = -10, X_max = 10, Y_min = -10, Y_max = 10):
    X, Y = get_X_AND_Y(X_min, X_max, Y_min, Y_max)
    Z = -np.abs(np.sin(X) * np.cos(Y) * np.exp(np.abs(1 - np.sqrt(X**2 + Y**2)/np.pi)))
    return X, Y, Z, 0, "Hölder table function", -20

def get_X_AND_Y(X_min, X_max, Y_min, Y_max):
    X = np.arange(X_min, X_max, 0.1)
    Y = np.arange(Y_min, Y_max, 0.1)
    X, Y = np.meshgrid(X, Y)
    return X, Y

def draw_pic(X, Y, Z, z_max, title, z_min=0):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    # ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(z_min, z_max)
    ax.set_title(title)
    # plt.savefig("./myProject/Algorithm/pic/%s.png" % title) # 保存图片
    plt.show()

X,Y,Z,z_max,title,z_min = Holder_table()
draw_pic(X,Y,Z,z_max,title,z_min)