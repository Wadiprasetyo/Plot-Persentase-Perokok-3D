import csv
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d
import numpy as np


data = []
with open('PersentasePerokokRI.csv', 'r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))
print(data)

provinsi = []
t15 = []
t16 = []
for item in data:
    provinsi.append(item['Provinsi'])
    t15.append(float(item['2015']))
    t16.append(float(item['2016']))
# print(provinsi)
# print(t15)
# print(t16)

ax = plt.subplot(111, projection='3d')
x = np.arange(34)
x1 = x
y = [1]*34
y1 = [3]*34
z = [0]*34
dx = np.repeat(0.5,34)
dy = np.repeat(0.5,34)
dz = t15
dz1 = t16
ax.bar3d(x,y,z,dx,dy,dz)
ax.bar3d(x1,y1,z,dx,dy,dz1)

ax.set_ylabel('Y')
ax.set_zlabel('z')
plt.xticks(x,provinsi,rotation=90)
plt.yticks([1,3],['2015','2016'])
plt.show()