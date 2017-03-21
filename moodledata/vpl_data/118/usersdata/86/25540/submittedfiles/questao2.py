import numpy
qf=int(input('digite o numero de quadrados:'))
fita=[]

for i in range(1,qf+1,1):
    fita.append(input('digite se esta colorido:'))
cor=[]
cont=0
while i<qf:
    if fita[i]!=0:
        cont=cont+1
        cor.append(fita[i])
        
        
    else:
        cor.append(fita[i])
    i=i=1    
print(cor)
        
    
    