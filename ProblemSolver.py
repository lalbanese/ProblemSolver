import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import cProfile
import pstats

class Robot:
    def __init__(self,mass,length_leg,coeff_fric):
        self.mass = mass
        self.weight = [x * 9.81 for x in mass]
        self.length = length_leg
        self.coeff_fric = coeff_fric

    def CalcForces(self):
        self.f_norm = [] 
        self.torque_motor = []
        self.f_friction = [x / 4 for x in self.weight]
        for coeff_val in self.coeff_fric:
            norm_list = []
            torque_list = []
            for fric_val in self.f_friction:
                norm_val = fric_val/coeff_val
                torque_val = norm_val * self.length
                norm_list.append(norm_val)
                torque_list.append(torque_val)
            self.f_norm.append(norm_list)
            self.torque_motor.append(torque_list)

    def Plot(self):
        for coeff_val in self.torque_motor:
            plt.plot(self.mass,coeff_val)
            #print("plotting")
        plt.ylim(0,1000)
        plt.show()

def main():
    profiler = cProfile.Profile()
    profiler.enable()
    mass = np.linspace(0.01,1,10000)
    length_leg = 8
    coeff_fric = np.linspace(0.01,5,500)
    myRobot = Robot(mass,length_leg,coeff_fric)
    myRobot.CalcForces()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
    stats.dump_stats('results.prof')
    myRobot.Plot()

main()
