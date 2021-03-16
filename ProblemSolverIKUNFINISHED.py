import numpy as np
import time
import sympy as sym
import math

def solve(l1, l2, end_effector):
    x3 = end_effector[0]
    y3 = end_effector[1]
    theta1 = sym.Symbol("theta1", real = True)
    theta2 = sym.Symbol("theta2", real = True)
    x2 = sym.Symbol("x2", real = True)
    y2 = sym.Symbol("y2", real = True)

    eq1 = sym.Eq(x2, l1*sym.cos(theta1))
    eq2 = sym.Eq(y2, l1*sym.sin(theta1))
    eq3 = sym.Eq(x3, l2*sym.cos(theta1+theta2))
    eq4 = sym.Eq(y3, l2*sym.sin(theta1+theta2))
   
    solution = sym.nsolve([eq1,eq2,eq3,eq4],[theta1,theta2,x2,y2],[0,0,x3,y3])
    angle1 = math.degrees(solution[0])
    angle2 = math.degrees(solution[1])
    origin2 = [solution[2], solution[3]]
    
    return angle1, angle2

#def circle(radius, circle_origin):


def main():
    l1 = 5
    l2 = 6
    #radius = 
    #circle_origin = 
    end_effector = [5,7]
    [angle1, angle2] = solve(l1,l2,end_effector)
    print("Angle of Link 1: ")
    print("Angle of Link 2: ")

main()


