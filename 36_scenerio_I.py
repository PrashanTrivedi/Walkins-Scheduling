import matplotlib.pyplot as plt

delta=[5,10,15,20,25]

d_5=[8.578248386552254, 66.74840951653526,0.244844, 67.2152078178161]
d_10=[8.515256511640368, 65.23949113921523, 0.236855, 66.20534988170772]
d_15=[8.409394903226445, 64.86799407833536, 0.236689 , 66.32394927124928]
d_20=[8.582285624209181, 64.90976672857092, 0.236710, 66.84985147992361]
d_25=[8.384720170924723, 64.38570327003643, 0.242577, 66.78835995265833]
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
    plt.title('delta vs time for different performance measures for L_max= 36')
    
plt.show()
    
    

