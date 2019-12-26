import matplotlib.pyplot as plt


delta=[5,10,15,20,25]


d_5=[8.475938782046942, 66.46728338654077, 0.240003, 66.93407136425927]
d_10=[8.313550234909906, 65.90341303227194, 0.248232, 66.86850264925909]
d_15=[8.432134000332004, 65.49932229886774, 0.240958, 66.95650659715025]
d_20=[8.389053732851218, 64.42044713263776, 0.246248, 66.35660265744765]
d_25=[8.477697955170536, 63.90463116004261, 0.243512, 66.29874104762207]

k=[d_5,d_10,d_15,d_20,d_25]
#print(k)
q=[]

for i in range(4):
    d=[]
    for j in range(5):
        d.append(k[j][i])
    q.append(d)
#print(q)

a=['Mean_waiting_time_scheduled','Mean_waiting_time_walk-ins','mean_idle_time _physician','Mean_preference_waiting']

for i in range(len(q)):
    plt.plot(delta,q[i],label=a[i])
    plt.legend(loc='best')
    plt.xlabel('delta')
    plt.ylabel('Time')
    plt.title('delta vs time for different performance measures for L_max= 54')
    
plt.show()
    
    
