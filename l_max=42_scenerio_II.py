import matplotlib.pyplot as plt

delta=[5,10,15,20,25]

d_5=[7.088088620024875, 63.930414560932036, 0.354130, 64.40535508312296]
d_10=[7.048952989887769, 63.70198491471972,  0.354333, 64.674118618493]
d_15=[7.060423769372805, 63.11718091223522,  0.357935, 64.57679293012447]
d_20=[7.151922685187012, 62.542728267005614,  0.351185, 64.47488962822538]
d_25=[7.018218244823537, 61.70826999925399, 0.359189, 64.09262674447359]
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
    plt.title('delta vs time for different performance measures for L_max= 42')
    
plt.show()
    
    
