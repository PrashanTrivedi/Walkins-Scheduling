import matplotlib.pyplot as plt


delta=[5,10,15,20,25]

d_5=[8.448191082531977, 66.03041886101913, 0.241332, 66.49753417928315]
d_10=[8.49936606871148, 65.97271493421651, 0.230326, 66.93794435583092]
d_15=[8.341397047478106, 65.12824839932493,  0.244777, 66.58347421483396]
d_20=[8.585869679113888, 65.33683813407296,  0.232684, 67.27748210671751]
d_25=[8.51434704720434, 64.52657816312794, 0.240228, 66.92523369585446]
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
    plt.title('delta vs time for different performance measures for L_max= 42')
    
plt.show()
    
    

