# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ct-XatJt3lhPDBx44jENvFuTzaoVCRno

Matplotlib
"""

import matplotlib.pyplot as plt

import numpy as np

x=np.linspace(0,10,100)

x

y=np.sin(x)

z=np.cos(x)

plt.plot(x,y,'r-')
plt.plot(x,z,'g+')
plt.xlabel('Angle')
plt.ylabel('Value')
plt.title('trignometric ratios')
plt.show

#parabola
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()

plt.plot(x,y,'r+')
plt.show()

"""Bar plot"""

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
languages=['English','Spanish','Sanskrit','Hindi','Urdu']
speakers=[100,120,23,200,150]
ax.bar(languages,speakers)
plt.xlabel('languages')
plt.ylabel('Person')
plt.title('Speakers')
plt.show()

"""pie chart"""

fig1=plt.figure()
ax=fig1.add_axes([0,0,1,1])
languages=['English','Spanish','Sanskrit','Hindi','Urdu']
speakers=[100,120,23,200,150]
ax.pie(speakers,labels=languages,autopct='%1.1f%%')

plt.title('Speakers')
plt.show()

"""Scatter plot"""

x=np.linspace(0,10,20)
y=np.sin(x)
plt.scatter(x,y,color='g')
plt.show()

#taught by sidhardhan
x=np.linspace(0,10,20)
y=np.sin(x)
fig2=plt.figure()
ax=fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='g')
plt.show()

"""3D scatter plot"""

fig3=plt.figure()
ax=plt.axes(projection='3d')
z=20*np.random.random(100)
x=np.sin(z)
y=np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()
