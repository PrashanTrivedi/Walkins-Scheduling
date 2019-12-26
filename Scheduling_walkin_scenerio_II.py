import random
import matplotlib.pyplot as plt
import numpy as np
import random

#N=int(input('Enter the number of times the simulation you want'))
#np.random.seed(100)
N=1000
Wait_schedule=[]
Wait_walkin=[]
Wait_pref=[]
Idle=[]
Number=[]
print('Scenario II')


for g in range(N):

    t_s=8*60
    t_e=11*60
    t_c=9*60
    t_max=12*60
    m=6
    L_max=float(54)
    Delta=float(t_max-t_c)/m
    #print('Delta the length of each  block :=', Delta)
    delta=float(5)
    #print('delta := ',delta)

    patients_in_block=[4,4,4,4,4,2]
    '''
    for i in range(m):
        a=int(input('Enter the number of scheduled patients in each blocks = '))
        patients_in_block.append(a)
    print('Number of scheduled patients block wise', patients_in_block)
    '''
    t_u=[]
    for i in range(m):
        t_u.append(t_c+i*Delta)
    #print('Start time of blocks ',t_u)

    p_s=5
    p_w=8

    #Generate the consultation time of the scheduled patients with given mean
    consultation_time=[]
    for i in range(len(patients_in_block)):
        a=np.random.exponential(float(p_s),size=patients_in_block[i])
        consultation_time.append(a)
    #print('consultation_time of scheduled patient block wise',consultation_time)

    #Number of walkin in each block
    def num_walkin(u):
        a=np.random.randint(1,10)
        return a
    #print('num_walkin(2) := ',num_walkin(2))
    def cum_consultation(u):
        #print consultation_time[1]
        s=0
        for i in range(len(consultation_time[u])):
            s=s+consultation_time[u][i]
            #w.append(d)
        a=s+t_u[u]
        return a
    #print (cum_consultation(1))

    # Load calculation
    def Load_block_u(u,n_w):
        for i in range(m):
            if i==u:
                L_u=sum(consultation_time[i])+n_w
                #print(L_u)
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
                h=Load_block_u(u,num_walkin(u))
                h=h+Load_block_u(u-1,num_walkin(u-1)) - Delta
                #print('condition true')
        return u
    #print('WBS(3) := ',WBS(3))

    def WBSA(u):
        if u==m:
            print('Schedule patient at ',t_max)
        else:
            u=u+1
            t=Load_block_u(u,num_walkin(u))
            t=t+Load_block_u(u-1,num_walkin(u-1)) - Delta
            #print('condition true')
        return u

    #def waiting():
    def cum_consultation(u):
        #print consultation_time[1]
        s=t_u[u]
        for i in range(len(consultation_time[u])):
            s=s+consultation_time[u][i]
            #w.append(d)
        a=s
        return a
    def numberofwaiting(u):
        s=t_u[u]
        for i in range(len(consultation_time[u])):
            s=s+consultation_time[u][i]
            if s>arrival_walkin[i]:
                z=patients_in_block[u]-i
            else:
                z=0
        return z

                
    def Scheduling(t):
        if t<t_c:
           y=WBS(1)
           if y==1:
               return t_c+delta
           else:
               return t_u[y]+delta
        else:
            if t>t_e:
                print('Cannot accept the walkin')
            else:
                for u in range(m):
                    #x=Load_block_u(u,num_walkin(u))+Load_block_u(u-1,num_walkin(u-1))
                    #print('x',x)
                    c=cum_consultation(u)
                    #print 'c',c
                    if c < t and t not in t_u:
                        #print "True"
                        #print('Send the walkin for consultation, no wait consultaion case')
                        return t
                    else:
                        a=[]
                        for i in range(len(t_u)):
                            w=t_u[i]-t
                        if w<0:
                            a.append(1)
                        else:
                            a.append(0)
                        u=np.argmax(a)
                        Load_block=0
                        if t_u[u]<=t and t< t_u[u]+delta:
                            #print 'true1'
                            Load_block=numberofwaiting(u)*p_s+num_walkin(u)*p_w
                        else:
                        #Load_block_u(u,num_walkin(u))=Load_block
                            if t_u[u]+delta <= t and t< t_u[u+1]:
                                #print 'true2'
                                Load_block=numberofwaiting(u)*p_s
                        #Load_block_u(u,num_walkin(u))=Load_block
                        #if (t_u[u]-t)!=0:
                        if float(Load_block+p_w)/(t_u[u+1]-t) <=float(L_max)/Delta and  (t_u[u]-t)!=0:
                            #print 'true3'
                            r=max(t,t_u[u]+delta)
                            return r
                #print('Schedule time of patient is := ', r)
                        else:
                            g=WBSA(u)
                            if g==1:
                               return t_c+delta
                            else:
                               return t_u[y]+delta
                       
                            
        if t>t_e:
            return 'Cannot Schedule'
            
    a=[]
    for i in range(len(consultation_time)):
        s1=[]
        #s.append(t_u[i])
        for j in range(len(consultation_time[i])):
            s1.append(t_u[i]+sum(consultation_time[i][:j]))
        a.append(s1)
    #print('Start time of consultation of scheduke patient',a)


    d=[]
    for i in range(m):
        f=[]
        #f.append(t_u[i])
        for j in range(patients_in_block[i]):
            f.append(t_u[i])
        d.append(f)
    #print(d)

    u=[]
    for i in range(len(d)):
        w_s_i=[]
        for j in range(len(d[i])):
            if a[i][j]-d[i][j]>=0:
                w_s_i.append(a[i][j]-d[i][j])
            else:
                w_s_i.append(0)
        u.append(w_s_i)
    #print("waiting time of schedule patient",u)

    sum_waiting_schedule=[]
    for i in range(m):
        sum_waiting_schedule.append(sum(u[i]))
    #print ("sum of waiting time of schedule patients",sum_waiting_schedule)

    Mean_waiting_time_schedule_patients = float(sum(sum_waiting_schedule)/sum( patients_in_block))
    Wait_schedule.append(Mean_waiting_time_schedule_patients)
    #print('Mean_waiting_time_schedule_patients := ',Mean_waiting_time_schedule_patients)

    total_walkin=0
    for i in range(m):
        total_walkin=total_walkin+num_walkin(i)
    #print (total_walkin)
    arrival_walkin=[]

    for i in range(total_walkin):
        q= t_c+np.random.exponential(0.33)
        if q<=t_e:
            arrival_walkin.append(q)
    arrival_walkin.sort()
    #print ("Walkin arrival time:",arrival_walkin)

    stime_walkin=[]
    for i in arrival_walkin:
        stime_walkin.append(Scheduling(i))
    #print ("scheduled time of walkins:",stime_walkin )

    ctime_walkin=[]
    for i in range(total_walkin):
        ctime_walkin.append(np.random.exponential())
    #print ('consultation time of walkin:',ctime_walkin)

    g=[]
    for i in range(len(consultation_time)):
        t1=[]
        t1.append(t_u[i])
        for j in range(len(consultation_time[i])):
            t1.append(t_u[i]+sum(consultation_time[i][:j+1]))
        g.append(t1)
    #print('Required',g)
    #print type(g)
    start_consultation_walkin=[]
    j=0
    while j<m-1:
        z=g[0][-1]
        for i in range(total_walkin):
            if z<g[j+1][0]:
                z=z+sum(ctime_walkin[:i])
                start_consultation_walkin.append(z)
            else:
                start_consultation_walkin.append(z+g[j+1][-1])
                z=z+sum(ctime_walkin[:i])
        j=j+1
        break

    #print ('start consultation time',start_consultation_walkin)

    waiting_time_walkin=[]
    for i in range(total_walkin):
        if float(start_consultation_walkin[i])-float(stime_walkin[i])>=0:
            waiting_time_walkin.append(start_consultation_walkin[i]-stime_walkin[i])
        else:
            waiting_time_walkin.append(0)
    #print ("waiting time for walkin:",waiting_time_walkin)
    average_waiting_time_walkin=float(sum(waiting_time_walkin)/total_walkin)
    Wait_walkin.append(average_waiting_time_walkin*0.1)
    #print ("average waiting time for walkin:",average_waiting_time_walkin)

    number_no_wait=0
    for i in range(total_walkin):
        for j in range(total_walkin):
            if arrival_walkin[i]==stime_walkin[j]:
                number_no_wait=number_no_wait+1
    #print ("number of no wait consultation time",number_no_wait)

    mean_number_no_wait=float(number_no_wait)/total_walkin
    Number.append( mean_number_no_wait)
    #print('Mean number of total no wait consultation',mean_number_no_wait)

    #physician idle
    h=[]
    for j in range(m):
        h.append(sum(consultation_time[j]))
    #print('h=',h)

    s=0
    for i in range(m):
        s=s+h[i]+ctime_walkin[i]
    #print('Total time doctor is busy=',s)

    idle_time=t_max- t_c - s
    if idle_time>=0:
    #print('Total time doctor is idle:=',idle_time)
        avg_idle_time=float(idle_time)/(t_max-t_c)
        Idle.append(avg_idle_time)
    else:
        Idle.append(0)
    #print('Average idle time of doctor:=',avg_idle_time)


    maximum_term=[]
    for i in range(total_walkin):
        maximum_term.append(max(arrival_walkin[i],t_c))
    #print('maximum_term',maximum_term)

    v_j=[]
    for i in range(len(maximum_term)):
        if start_consultation_walkin[i]-maximum_term[i] >0:
            v_j.append(start_consultation_walkin[i]-maximum_term[i])
        else:
            v_j.append(0)
    #print('v_j=',v_j)

    avg_vj=np.mean(v_j)
    Wait_pref.append(avg_vj*0.1)
    #print('Average v_j=',avg_vj)
print('L_max=',L_max)
print('delta=',delta)
print('Mean waiting time of scheduled patients',np.mean(Wait_schedule))
print('Mean waiting time of walkin patients',np.mean(Wait_walkin))
print('Mean idle time of physician',np.mean(Idle))
print('Mean number of no wait consultation patients',np.mean(Number))
print('Mean waiting time based on arrival time',np.mean(Wait_pref))

#lk=[np.mean(Wait_schedule),np.mean(Wait_walkin),np.mean(Idle),np.mean(Number),np.mean(Wait_pref)]
#print(lk)
