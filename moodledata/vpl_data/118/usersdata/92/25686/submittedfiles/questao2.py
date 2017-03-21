from __future__ import division

n= input('Digite o valor de n: ')

l=[]
for i in range(0, n, 1):
    l.append(input('Digite -1 ou 0: '))
    
p=[]
for j in range(1, n+1, 1):
    if l[j]==0:
        p.append(i)
l2=[]
cont=0
for k in range(0, len(p), 1):
    if k<(len(p)-1):
        if l[cont]!=0:
            while l[cont]!=0:
                d1= p[k]-cont
                if d1<0:
                    d1=d1*(-1)
                    d2= (p[k]+1)-cont
                    if d2<0:
                        d2=d2*(-1)
                    if d1<=d2:
                        x=d1
                    else:
                        x=d2
                    if x>=9:
                        x=9
                    
                    l2.append(x)
                    cont=cont+1
                    if l[cont]==p[len(p)-1]:
                        break
        else:
            l2.append(0)
            cont= cont+1
    else:
        while cont<=(n-1):
            if l[p[k]]!=0:
                while l[cont]!=l[n-1]:

                    d3= l[p[k]-cont
                    if d3<0:
                        d3=d3*(-1)
                    if d3>=9:
                        d3=9
                    l2.append(d3)
                    cont= cont+1
                
            else:
                l2.append(0)
                cont= cont+1
                    
print l2 
            
            