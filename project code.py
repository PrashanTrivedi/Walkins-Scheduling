import random
import matplotlib.pyplot as plt
import numpy as np
import random

N=int(input('Enter the number if walkins you can handle'))

t_s=float(input('Enter the time at which hospital opens reception desk:='))
t_e=float(input('Enter the time at which hospital close reception desk:='))
t_c=float(input('Enter the time at which doctor starts consultation:= '))
t_max=float(input('Enter the time at which doctor ends the consultation:= '))
B=int(input('Enter the number of blocks in a day:='))
L_max=float(input('Enter the maximum load in blocks, L_max:='))
Delta=float(t_max-t_c)/B
print('Delta, the length of each  block :=', Delta)

patients_in_block=[]
for i in range(1,B+1):
    a=int(input('Enter the number of scheduled patients in each blocks = '))
    patients_in_block.append(a)
print('Number of scheduled patients block wise', patients_in_block)

p_s=float(input('Enter the mean consultation time for a scheduled patient:='))
p_w=float(input('Enter the mean consultation time for a walk-ins:='))

delta=float(input('Enter delta, the difference of the start time of the walkins and t_c = '))

t_u=[]
for i in range(B):
    t_u.append(t_c+i*Delta)
print('Start time of blocks ',t_u)




#Generating the arrival times of walkins

walkins_time=[]
for i in range(N-1):
    walkins_time.append(random.uniform(8,11))

walkins_time.sort()

print('Arrival time of the walkins',walkins_time)


t=float(input('Enter the arrival time of walkin'))

def Load_block_u(u,n_s,n_w,p_s,p_w):
    L_u=n_s*p_s+n_w*p_w
    return L_u

def WBS(u,n_s,n_w,p_s,p_w,L_max):
    if Load_block_u(u,n_s,n_w,p_s,p_w) + p_w <=L_max:
        print('Schedule the patient in block ',u)
    else:
        if u==B:
            print('Schedule patient at ',t_max)
        else:
            u=u+1
            z=Load_block_u(u,n_s,n_w,p_s,p_w)
            z=z+Load_block_u(u-1,n_s,n_w,p_s,p_w) - Delta
    return u
print(WBS(1,20,5,p_s,p_w,L_max))




'''


Waiting_s_i=s-a
Waiting_w_j=w-a
def L(u,n_1,n_2):
    return n_1*p_s+n_2*p_w
def WBS(u,Lu(),L_max):
    start=u
    if L(u)+p_w<=L_max:
        return 'patient', j, 'in', u
    else:
        Temp(u,L(u),L_max)

def Temp(j,u,L(u),L_max):
    if u=m:
        return 'patient',j,'in',t_max
    else:
        u=u+1
        L(u)=L(u)+(L(u-1)-Delta)
        WBS(u,L(u),L_max)


def algo(t,t_c,n_1,n_2):
    if t<t_c:
        WBS(1,L(1),L_max) # Call WBS with u=1
    else:
        if p_idle:  # write condition for idle ness of physician, physician will be idle iff the sum of all
            #the consultation times of schedule patients and the walkins till that time is < the current time
            #and the schedule time of regular patient is more than the current time.
            return 'scheduled time=',t
        else:
            temp=[]
            for i in range(1,B+1):
                if t_u[i]<=t:
                    i=i+1
                    temp.append(u)
            u=max(temp)
            if (t**u)<=t<(t**u)+delta:
                print L(u,n_1,n_2)
            else:
                if (t**u)+delta<=t<t**(u+1):
                    print L(u)-n_1*p_w
            if (L(u)+p_w)/(t**(u+1)-t)<=L_max/Delta:
                print 'schedule time of patient',j, 'is',max(t,t**(u)+delta)
            else:
                Temp(u,L(u),L_max)
N=len(t)#'Number of walkins'
for j in range(1,N):
    print algo(j,t[j],n_1,n_2)


    
'p_idle=condition for physician is idle'
 '''              
    
