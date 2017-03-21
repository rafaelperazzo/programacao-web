from __future__ import division
N=int(input('Digite o valor de N: '))
a=[]
b=[]
ele=0
cont=0
c=[]
for i in range(0,N,1):
    a.append(input('Digite (-1) ou (0): '))
d=a
for i in range(0,N):
    if d[i]==0:
        cont= cont+1
for i in range(0,cont):
    b.append(d.index(0))
    d.remove(0)
print N
for g in range(0,N):
    for j in range(0,cont-1):
        if a[0]!=0:
            c.append(b[0])
        if a[0]==0:
            c.append(0)
        if a[g]!=0 and g!=0:
            if b[j]>a[g]<b[j+1]:
                lim=b[j]-b[j+1]
                if g<lim:
                    ele=0
                    for x in range(0,lim):
                        ele=ele+1
                        c.append(ele)
                if g>lim:
                    ele=lim
                    for x in range(lim,b[j+1]):
                        c.append(ele)
                        ele=ele-1
        if a[g]==0 and g!=0:
            c.append(0)
print c
    
        
            
                    
                
                
                
        
            
        
    
