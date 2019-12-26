import matplotlib.pyplot as plt

delta=[5,10,15,20,25]

d_5=[6.9999156675364285, 64.11586992871584, 0.353357, 64.59087003719254]
d_10=[7.194434152163474, 63.14215518676848, 0.345405, 64.11434341884056]
d_15=[7.013899650647399, 62.884013799878694,  0.352785, 64.34395330521725]
d_20=[7.10648482469452, 61.26326351448642, 0.351266, 63.190037919420234]
d_25=[7.009018769072627, 62.151201684208964, 0.358769, 64.53379823449481]
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
    plt.title('delta vs time for different performance measures for L_max= 36')
    
plt.show()
    
    
