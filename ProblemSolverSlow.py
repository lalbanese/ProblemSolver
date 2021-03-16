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
        self.f_norm = np.zeros((len(self.coeff_fric),len(self.mass)))
        self.torque_motor = np.zeros((len(self.coeff_fric),len(self.mass)))
        self.f_friction = [x/4 for x in self.weight]
        for coeff_index in range(0,len(self.coeff_fric)):
            for fric_index in range(0,len(self.f_friction)):
                self.f_norm[coeff_index,fric_index] = self.f_friction[fric_index]/self.coeff_fric[coeff_index]
                self.torque_motor[coeff_index,fric_index] = self.f_norm[coeff_index,fric_index] * self.length

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
