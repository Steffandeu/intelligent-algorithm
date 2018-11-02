import  random
import numpy as np 


def fit_fun(X):  # 适应函数
    return -np.abs(np.sin(X[0]) * np.cos(X[1]) * np.exp(np.abs(1 - np.sqrt(X[0] ** 2 + X[1] ** 2) / np.pi)))

class Particle(object):
    def __init__(self,x_Max,max_vel,dim):
        self.x_Max = x_Max
        self.max_vel = max_vel
        self.pos = [random.uniform(-x_Max,x_Max) for i in range(dim)]
        self.vel = [random.uniform(-max_vel,max_vel) for i in range(dim)]
        self.pbest = [0.0 for i in range(dim)]
        self.pfit_value =fit_fun(self.pos)

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def set_pos(self,i,value):
        self.pos[i] = value
    def set_vel(self,i,value):
        self.vel[i] = value
    def get_pbest(self):
        return self.pbest
    def set_pbest(self,i,value):
        self.pbest[i] = value
    def get_pfit_value(self):
        return self.pfit_value
    def set_pfit_value(self,value):
        self.pfit_value = value

class PSO():
    def __init__(self,dim,partisnum,itermax,max_vel,x_Max,gbest_fitness_value=float('Inf'),c1=2,c2=2,w=1):
        self.dim = dim
        self.partisnum = partisnum
        self.itermax = itermax
        self.x_Max = x_Max
        self.max_vel = max_vel
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.gbest_fitness_value_list  =[ ]
        self.gbest_fitness_value = gbest_fitness_value
        self.gbest = [0.0 for i in range(dim)]

        self.Paticle_List = [Particle(x_Max,max_vel,dim) for i in range(partisnum)]

    def set_bestFitnessValue(self, value):
        self.gbest_fitness_value = value

    def get_bestFitnessValue(self):
        return self.gbest_fitness_value

    def set_bestPosition(self, i, value):
        self.gbest[i] = value

    def get_bestPosition(self):
        return self.gbest

    def update_vel(self):
        for i in range(self.dim):
            for pati_c in self.Paticle_List:
                vel_value = self.w * pati_c.vel[i] + self.c1 * random.random() *(pati_c.get_pbest()[i]-pati_c.get_pos()[i])+self.c2*random.random()*(self.get_bestPosition()[i]-pati_c.get_pos()[i])
                if vel_value > self.max_vel:
                    vel_value = self.max_vel
                elif vel_value < -self.max_vel:
                    vel_value = -self.max_vel
    #
    #             pati_c.set_vel(i,vel_value)
    # def update_vel(self,part):
    #     for i in range(self.dim):
    #         vel_value = self.w * part.get_vel()[i] + self.c1 * random.random() *(part.get_pbest()[i]-part.get_pos()[i])+self.c2*random.random()*(self.get_bestPosition()[i]-part.get_pos()[i])
    #         if vel_value > self.max_vel:
    #             vel_value = self.max_vel
    #         elif vel_value < -self.max_vel:
    #             vel_value = -self.max_vel
    #             # for i in range(self.dim):
    #         part.set_vel(i,vel_value)

    def update_pos(self, part):
        for i in range(self.dim):
            if -self.x_Max <= part.get_pos()[i] + part.get_vel()[i] <= self.x_Max:
                pos_value = part.get_pos()[i] + part.get_vel()[i]
                part.set_pos(i, pos_value)
        value = fit_fun(part.get_pos())
        # print(part.get_pos())
        print(value)

        if value < part.get_pfit_value():
            part.set_pfit_value(value)
            for i in range(self.dim):
                part.set_pbest(i, part.get_pos()[i])
        if value < self.get_bestFitnessValue():
            self.set_bestFitnessValue(value)
            for i in range(self.dim):
                self.set_bestPosition(i, part.get_pos()[i])

    def update(self):
        for i in range(self.partisnum):
            for part in self.Paticle_List:
                self.update_pos(part)
                self.update_vel()
                self.gbest_fitness_value_list.append(self.get_bestFitnessValue())
        return self.gbest_fitness_value_list,self.get_bestPosition()

if __name__ == '__main__':
    dim = 2
    partisnum = 100
    itermax= 10000
    x_Max = 10
    max_vel = 0.5
    pso = PSO(dim,partisnum,itermax,max_vel,x_Max)
    gbest_fitness_value_list, best_pos = pso.update()
    print("最优位置:" + str(best_pos))
    print("最优解:" + str(gbest_fitness_value_list[-1]))





