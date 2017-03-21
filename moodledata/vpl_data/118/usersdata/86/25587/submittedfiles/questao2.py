import numpy
qf=int(input('digite o numero de quadrados:'))
fita=[]
cor=[]
for i in range(1,qf+1,1):
    fita.append(input('digite se esta colorido:'))

cont=0
for j in range(0,len(fita),1):
    i=0
    while fita[i]==0:
        if fita[j]!=fita[i]:
            cont=cont+1
        cor.append(input(cont))
        else:
            cor.append(input(0))
        
        i=i=1    

print(cor)
        
    
    