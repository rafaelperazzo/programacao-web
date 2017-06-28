import numpy as np
x=int(input('d: '))
y=int(input('f: '))
a=np.zeros((x,y))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('s: '))
        
    
