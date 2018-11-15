import matplotlib.pyplot as plt
import  numpy as np

def inputfun(x):
    return (x-2)*(x+3)*(x+8)*(x-9)

initT = 1000#模拟退火的初始的温度
minT =1#迭代最小的温度
iterL = 1000#迭代的次数
delat =0.95#温度衰减的洗漱
k=1

initX = 10*(2*np.random.rand()-1)
nowT = initT
print("初始解：",initX)

xx = np.linspace(-10,10,300)
yy = inputfun(xx)
plt.figure()
plt.plot(xx,yy)
plt.plot(initX,inputfun(initX),'o')
#SA算法寻优
while nowT > minT:
    for i in np.arange(1,iterL,1):
        funVal = inputfun(initX)
        xnew = initX + (2*np.random.rand()-1)#以一定预设领域来产生一个扰动得到一个新的状态初始量
        # xnew = initX + np.random.uniform(low=-0.055,high=0.005)*initT
        if xnew >= -10 and xnew<=10:
            funnew = inputfun(xnew)
            res = funnew - funVal
            if res<0:
                initX = xnew
            else:
                p= np.exp(-(res)/(k*nowT))
                if np.random.rand() <p:
                    initX = xnew
    nowT = nowT * delat

print("最优解：",initX)
print("最优值：",inputfun(initX))
plt.plot(initX,inputfun(initX),'*r')
plt.show()

