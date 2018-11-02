import numpy as np
import matplotlib.pyplot as plt
import  random

class parti:
    def __init__(self,v,x):
        self.v = v #粒子当前速度
        self.x = x #粒子当前位置
        self.pbest = x #粒子历史最优位置

class PSO:
    def __init__(self,interval,tab = 'min',patisNum=10,iterMax=100,w=1,c1=2,c2=2,):
        self.interval = interval #给定状态空间即待求解空间
        self.tab = tab.strip()  #求解最大值还是最小值标签
        self.iterMax = iterMax  #迭代求解次数

        self.w = w  #惯性因字
        self.c1 = c1  #学习因子
        self.c2 = c2  #学习银子
        self.v_max = (interval[1]-interval[0]) * 0.1 #设置最大迁移速度
        ############################################################################
        self.partis_list,self.gbest = self.initPartis(patisNum)  #完成粒子全初始化，并提取群体历史最优位置
        self.x_seed = np.array(list(parti_.x for parti_ in self.partis_list))  #提取粒子群种子get position on x axis
        # print(self.x_seed)
        self.solve() ##求解
        self.display()
        # print(interval)



    def initPartis(self,partisNum):
        partis_list = list()
        # for j in range(dim):
        for i in range(partisNum):
            v_seed = random.uniform(-self.v_max,self.v_max)
            x_seed = random.uniform(*self.interval)#[-9,5]
            # print(x_seed)
            # print("-----",v_seed)
            partis_list.append(parti(v_seed,x_seed))#存放例子
        print(partis_list)
        temp= 'find_' + self.tab
        # print(temp)
        if hasattr(self,temp):
            gbest = self.find_max(partis_list)
            # gbest = getattr(self,temp)(partis_list)  # 采用反射方法提取对应的函数------>equal find+_min/max
        else:
            exit('>>>tab标签传参有误："min"|"max"<<<')
        # print(partis_list)
        return partis_list,gbest

    def solve(self):
        # for j in range(self.dim):
        for i in range(self.iterMax):
            for parti_c in self.partis_list:
                f1 = self.func(parti_c.x)
                parti_c.v = self.w * parti_c.v + self.c1 * random.random() * (parti_c.pbest - parti_c.x) + self.c2 * random.random() * (self.gbest - parti_c.x)#粒子群速度更新速公式
                if parti_c.v > self.v_max:#更新粒子的速度，并限制在最大迁移速度之内
                    parti_c.v = self.v_max
                elif parti_c.v < -self.v_max:
                    parti_c.v = -self.v_max
                if self.interval[0] <= parti_c.x +parti_c.v<=self.interval[1]:#更新粒子的位置，并限制在解空间之内
                    parti_c.x = parti_c.x+parti_c.v
                else:
                    parti_c.x = parti_c.x - parti_c.v
                f2 = self.func(parti_c.x)
                getattr(self,'deal_'+self.tab)(f1,f2,parti_c)####------> EQUAL TO  deal_max/min(f1,f2,parti_c)

    def func(self,x):
        value = np.sin(x**2)*(x**2-5*x)
        return value

    def find_min(self,partis_list):
        parti = min(partis_list, key=lambda parti: self.func(parti.pbest))
        return parti.pbest#粒子历史最优位置

    def find_max(self,partis_list):
        parti = max(partis_list, key=lambda parti: self.func(parti.pbest))
        return parti.pbest

    def deal_min(self,f1,f2,parti_):
        if f2 < f1:
            parti_.pbest = parti_.x
        if f2 < self.func(self.gbest):
            self.gbest = parti_.x

    def deal_max(self,f1,f2,parti_):
        if f2 >f1:
            parti_.pbest = parti_.x
        if f2 > self.func(self.gbest):
            self.gbest = parti_.x

    def display(self):
        print('solution:{}'.format(self.gbest))
        plt.figure(figsize=(8,4))
        x = np.linspace(self.interval[0],self.interval[1],300)
        y = self.func(x)
        plt.plot(x, y, 'g-', label='function')
        plt.plot(self.x_seed, self.func(self.x_seed), 'b.', label='seeds')
        plt.plot(self.gbest, self.func(self.gbest), 'r*', label='solution')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('solution = {}'.format(self.gbest))
        plt.legend()
        plt.savefig('PSO.png', dpi=500)
        plt.show()
        plt.close()


if __name__ == '__main__':
    PSO([-9,10],'max')







