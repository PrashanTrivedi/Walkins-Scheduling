import matplotlib.pyplot as plt


delta=[5,10,15,20,25]

d_5=[8.521705231696759, 65.76296569456518, 0.241415, 66.23017958052226]
d_10=[8.341438355911276, 65.64181962802533, 0.249631, 66.60679552162222]
d_15=[8.460930412655252, 65.76656581826511,  0.239958, 67.22396614421929]
d_20=[8.329961982416615, 64.51033888666439,  0.245727, 66.44657266771338]
d_25=[8.351956115315955, 64.59700483657711,0.243125 , 66.99900572878795]
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
    
    

