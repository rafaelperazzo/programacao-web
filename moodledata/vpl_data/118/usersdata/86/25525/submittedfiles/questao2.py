import numpy
qf=int(input('digite o numero de quadrados:'))
fita=[]

for i in range(1,qf+1,1):
    fita.append(input('digite se esta colorido:'))
cor+[]
cont=0
while fita[i]!=fita[qf-1]:
    if fita[i]!=0:
        cont=cont+1
        cor.append(fita[i])
        if cont>9:
        cor.append(9)
    else:
        cor.append(fita[i])
        
print(cor)
        
    
    