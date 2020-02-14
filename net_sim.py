import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
import random
import math
import sys

def gen_exp1(M):
    R = random.uniform(0,1)
    t = int((-M)*(np.log(1.0-R)))
    if t< 64:
        return 64
    elif t>1518:
        return 1518
    else:
        return t

def gen_exp2(M):
    R = random.uniform(0,1)
    t = float((-M)*(np.log(1.0-R)))
    return t
   
def main():
    N = int(sys.argv[2])
    file_name = str(sys.argv[1])
    f = open(file_name, "r")
    time =[]
    length = []
    length_2=[]
    t_interval =[]
    t_interval_2 = []
    time_2 = []

#collect data
    for line in f:
        x=line.split()
        time.append(float(x[0]))
        length.append(int(x[1]))


#calculate the list of interval time
    for i in range(len(time)-1):
        t_interval.append(time[i+1]-time[i])
    
#calculate mean
    M = float(math.sqrt(np.var(length)))

#generate list of length in exponential distribution
    for i in range(N):
        length_2.append(gen_exp1(M))

#generate list of time interval in exponential distribution
    M = float(math.sqrt(np.var(t_interval)))

    for i in range(N):
         t_interval_2.append(gen_exp2(M))

    t = 0  
    for i in range(N):
        t = t + t_interval_2[i]
        time_2.append(t)

    f = open("newtrace.tl","w")
    for i in range(N):
        pad = " "*(6-len(str(length_2[i])))
        f.write("    "+str(time_2[i])[:8]+pad+str(length_2[i])+"\n")
    
    print("done")
main()
