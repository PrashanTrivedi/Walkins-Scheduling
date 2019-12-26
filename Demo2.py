import random
import matplotlib.pyplot as plt
import numpy as np
import random

#N=int(input('Enter the number if walkins you can handle'))

t_s=float(input('Enter the time at which hospital opens reception desk:='))
t_e=float(input('Enter the time at which hospital close reception desk:='))
t_c=float(input('Enter the time at which doctor starts consultation:= '))
t_max=float(input('Enter the time at which doctor ends the consultation:= '))
m=int(input('Enter the number of blocks in a day:='))
L_max=float(input('Enter the maximum load in blocks, L_max:='))
Delta=float(t_max-t_c)/m
print('Delta, the length of each  block :=', Delta)
delta=float(input('Enter delta, the difference of the start time of the walkins and t_c = '))
print('delta := ',delta)

patients_in_block=[]
for i in range(m):
    a=int(input('Enter the number of scheduled patients in each blocks = '))
    patients_in_block.append(a)
print('Number of scheduled patients block wise', patients_in_block)

t_u=[]
for i in range(m):
    t_u.append(t_c+i*Delta)
print('Start time of blocks ',t_u)

p_s=float(input('Enter the mean consultation time for a scheduled patient:='))
p_w=float(input('Enter the mean consultation time for a walk-ins:='))

#Generate the consultation time of the scheduled patients with given mean
consultation_time=[]
for i in range(len(patients_in_block)):
    a=np.random.exponential(float(p_s),size=patients_in_block[i])
    consultation_time.append(a)
print('consultation_time of scheduled patient block wise',consultation_time)

#Number of walkin in each block
def num_walkin(u):
    for i in range(m):
        if i==u:
            z=np.random.randint(1,high=10)
    return z
#print('num_walkin(2) := ',num_walkin(2))


# Load calculation
def Load_block_u(u,n_w):
    for i in range(m):
        if i==u:
            L_u=sum(consultation_time[i])+n_w*p_w
    return L_u
#print('Load_block_u(3)',Load_block_u(3))

#WBS
def WBS(u):
    if Load_block_u(u,num_walkin(u)) + p_w <=L_max:
        print('Schedule the patient in block ',u)
    else:
        if u==m:
            print('Schedule patient at ',t_max)
        else:
            u=u+1
            z=Load_block_u(u,num_walkin(u))
            z=z+Load_block_u(u-1,num_walkin(u-1)) - Delta
            print('condition true')
    return u
#print('WBS(3) := ',WBS(3))

def WBSA(u):
    if u==m:
        print('Schedule patient at ',t_max)
    else:
        u=u+1
        z=Load_block_u(u,num_walkin(u))
        z=z+Load_block_u(u-1,num_walkin(u-1)) - Delta
        #print('condition true')
    return u

#def waiting():

            
def Scheduling(t):
    Load_block=0
    if t<t_c:
       y=WBS(1)
       if y==1:
           return t_c+delta
       else:
           return t_u[y]+delta
    else:
        for u in range(1,m+1):
            if sum(Load_block_u(u-1,num_walkin(u-1)))+sum(consultation_time[u]) < t_u[u]+delta:
                print('Send the walkin for consultation, no wait consultaion case')
                break
            else:
                a=[]
                
                for i in range(len(t_u)):
                    w=t_u[i]-t
                    if w<0:
                        a.append(1)
                    else:
                        a.append(0)
                u=np.argmax(a)
                if t_u[u]<=t and t< t_u[u]+delta:
                    Load_block=Load_block_u(u,num_walkin(u))+ 0.5
                    #Load_block_u(u,num_walkin(u))=Load_block
                if t_u[u]+delta <= t and t< t_u[u+1]:
                    Load_block= 1.5
                    #Load_block_u(u,num_walkin(u))=Load_block
        if float((Load_block+p_w) / (t_u[u]-t)) <=float(L_max/Delta):
            r=max(t,t_u[u]+delta)
            print('Schedule time of patient is := ', r)
        else:
            WBSA(u)
    
    return t




t=float(input('Enter the time of walkin patient'))
print('Schedule the walkin at time',Scheduling(t))

#start time of consultation

a=[]
for i in range(len(consultation_time)):
    s=[]
    s.append(t_u[i])
    for j in range(len(consultation_time[i])):
        s.append(t_u[i]+sum(consultation_time[i][:j+1]))
    a.append(s)
print('Start time of consultation of scheduke patient',a)


d=[]
for i in range(m):
    f=[]
    for j in range(patients_in_block[i]):
        f.append(t_u[i])
print(d)
            
                
                
            
            


