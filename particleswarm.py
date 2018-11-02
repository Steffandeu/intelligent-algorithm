import random
import  numpy as np
class parti:
    """

    """
    def __init__(self,speed,position):
        self.speed = speed
        self.positon = position
        self.pbest = [0.0 for i in range(dim)]

        # self.fitvalue = fitvalue
        # self.lBestfit = lBestfit
        # self.lBestpositon = lBestposition





class PSO:
    def __init__(self, dim, size, iter_num,interval, max_vel,tab ='min', C1 = 2, C2 = 2, W = 1):
        self.C1 = C1
        self.C2 = C2
        self.W = W
        self.dim = dim  # 粒子的维度
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.internal = interval
        self.max_vel = max_vel  # 粒子最大速度
        self.tab = tab.strip()
        # self.gbest = [0.0 for i in range(dim)]
        # self.best_fitness_value = best_fitness_value
        self.best_position = [0.0 for i in range(dim)]  # 种群最优位置
        self.fitness_val_list = []  # 每次迭代最优适应值
        #对种群进行初始化（包含维度）
        self.Particle_List = [self.Particles(self.internal,self.max_vel,self.dim) for i in range(self.size)]
        self.update()



    def Particles(self,interval, max_vel, dim):
        Particle_List = []
        for i in range(dim):
            parti_speed =random.uniform(-max_vel,max_vel)
            parti_position = random.uniform(*interval)
            Particle_List.append(parti(parti_speed,parti_position))
            # print(parti_speed)
        # print(len(Particle_List))
        # print(type(parti(parti_speed,parti_position)))
        # # print(type(Particle_List))
        return  Particle_List

    def fit_fun(X):  # 适应函数
        return -np.abs(np.sin(X[0]) * np.cos(X[1]) * np.exp(np.abs(1 - np.sqrt(X[0] ** 2 + X[1] ** 2) / np.pi)))


    # def get_vel(self,Particle_List):
    #     vel_value_list1 = []
    #     vel_value_list2 = []
    #     max_vel = []
    #     for parti_c in Particle_List:
    #         print("=====",parti_c)
    #         vel_value_list1.append(parti_c[0].positon)
    #         vel_value_list2.append(parti_c[1].positon)
    #     for i in vel_value_list1:
    #         for j in vel_value_list2:
    #             bestvalue = min(self.fit_fun(i,j))
    #
    #     return vel_value_list1


    def judge(self):
        Particle_List = []
        for i in range(dim):
            parti_speed = random.uniform(-max_vel, max_vel)
            parti_position = random.uniform(*interval)
            Particle_List.append(parti(parti_speed, parti_position))
        temp = 'find' + self.tab
        if hasattr(self,temp):
            # gbest = self.find_max()
            best_position = getattr(self,temp)(Particle_List)
        return best_position

    def find_min(self,Particle_List):
        parti = min(Particle_List,key=lambda parti:self.fit_fun(parti.positon))
        return parti.pbest

    def find_max(self,Particle_List):
        parti = max(Particle_List,key= lambda parti:self.fit_fun(parti.positon))
        return parti.pbest

    def update(self):
        for i in range(dim):
            for parti_c in self.Particle_List:
                position = []
                print(parti_c[1].speed)
                # f1 = self.fit_fun(parti_c[i].positon)
                vel_value = self.W * parti_c[i].speed + self.C1 * random.random()*(parti_c[i].pbest-parti_c[i].positon)+self.C2 *random.random()*(self.best_position[i] - parti_c[i].positon)
                if vel_value > self.max_vel:
                    vel_value = self.max_vel
                elif vel_value < -self.max_vel:
                    vel_value.speed = -self.max_vel
                if self.internal[0] <= parti_c[i].positon + vel_value <=self.internal[1]:
                    parti_c[i].positon = parti_c[i].positon + vel_value
                else:
                    parti_c[i].positon = parti_c[i].positon - vel_value
                f2 = self.fit_fun(parti_c[i].positon)
                # getattr(self,'deal_'+self.tab)(f1,f2,parti_c)

    def deal_min(self,f1,f2,parti):
        if f2<f1:
            parti.pbest = parti.positon
        if f2 < self.fit_fun(self.gbest):
            self.gbest = parti.positon

    def deal_max(self,f1,f2,parti):
        if f2 > f1:
           parti.pbest = parti.positon
        if f2 > self.fit_fun(self.gbest):
            self.gbest == parti.positon



    # def update_pos(self, part):
    #     for i in range(self.dim):
    #         pos_value = part.get_pos()[i] + part.get_vel()[i]
    #         part.set_pos(i, pos_value)
    #     value = self.fit_fun(part.get_pos())
    #     if value < part.get_fitness_value():
    #         part.set_fitness_value(value)
    #         for i in range(self.dim):
    #             part.set_best_pos(i, part.get_pos()[i])
    #     if value < self.get_bestFitnessValue():
    #         self.set_bestFitnessValue(value)
    #         for i in range(self.dim):
    #             self.set_bestPosition(i, part.get_pos()[i])
    #
    #
    # # def deal_min(self):
    # def update(self):
    #     for i in range(self.iter_num):
    #         for part in self.Particle_list:
    #             self.update_vel(part)  # 更新速度
    #             self.update_pos(part)  # 更新位置
    #         self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
    #     return self.fitness_val_list, self.get_bestPosition()


if __name__ == '__main__':
    dim = 2
    size = 20
    iter_num = 1000
    interval = [-10,10]
    max_vel = 0.5
    pso = PSO(dim,size,iter_num,interval,max_vel)

    # print(pso.Particle_List)
    # print(pso.get_vel(pso.Particle_List))
    # print(np.shape(pso.Particle_List))
    # print(len(pso.Particle_List))
    # print(pso.get_vel(pso.Particle_List))


    # fit_var_List ,best_pos = pso.update()
    # print("最优位置："+str(best_pos))
    # print("最优解："+ str(fit_var_List[-1]))
