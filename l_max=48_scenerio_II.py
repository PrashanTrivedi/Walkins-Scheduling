import matplotlib.pyplot as plt

delta=[5,10,15,20,25]

d_5=[7.035709969625145, 63.382654642260945, 0.356828 , 63.85790358435509]
d_10=[7.028020125668056, 63.16252956296099, 0.356562, 64.13465964066594]
d_15=[7.04034807950666, 64.10109062762407, 0.354015, 65.56262133361787]
d_20=[7.051495360111918, 62.698454116515414, 0.353438, 64.62886691305549]
d_25=[7.073726085073906, 61.86312752460618, 0.354028, 64.24534387418295]
k=[d_5,d_10,d_15,d_20,d_25]
#print(k)
q=[]

for i in range(4):
    d=[]
    for j in range(5):
        d.append(k[j][i])
    q.append(d)
print(q)

a=['Mean_waiting_time_scheduled','Mean_waiting_time_walk-ins','mean_idle_time _physician','Mean_preference_waiting']


for i in range(len(q)):
    plt.plot(delta,q[i],label=a[i])
    plt.legend(loc='best')
    plt.xlabel('delta')
    plt.ylabel('Time')
    plt.title('delta vs time for different performance measures for L_max= 48')
    
plt.show()
    
    
