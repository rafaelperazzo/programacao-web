for __future__ import division

n= input('Digite o valor de n: ')

l=[]
for i in range(0, n, 1):
    l.append(input('Digite -1 ou 0: '))
    
p=[]
for i in range(1, n+1, 1):
    if l[i]==0:
        p.append(i)
l2=[]
cont=0
for i in range(0, len(p), 1):
    if i<(len(p)-1):
        if l[cont]!=0:
            while l[cont]!=0:
                d1= l[p[i]]-cont
                if d1<0:
                    d1=d1*(-1)
                    d2= l[p[i]+1]-cont
                    if d2<0:
                        d2=d2*(-1)
                    if d1<=d2:
                        x=d1
                    else:
                        x=d2
                    
                    l2.append(x)
                    cont=cont+1
                    if l[cont]==p[len(p)-1]:
                        break
        else:
            cont= cont+1
    else:
        while l[cont]!=l[n-1]:
            d1= l[p[i]]-cont
                if d1<0:
                    d1=d1*(-1)
            l2.append(d1)
            cont= cont=1
                    
print l2    
            
            