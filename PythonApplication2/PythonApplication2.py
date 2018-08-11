import matplotlib.pyplot as plt

x1=[1,2,3,4,5,6,7]
y1=[4,5,6,6,8,7,9]

plt.bar(x1,y1,label='Bars 1')


plt.xlabel('x')   
plt.ylabel('y')
plt.title('Kora\n Check it out' )
plt.legend()
plt.show()