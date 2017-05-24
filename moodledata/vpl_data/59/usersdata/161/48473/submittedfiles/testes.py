n=int(input('numero:'))
soma=0
cont1=0
cont2=0
for i in range(1,n+1,1):
    idade=int(input('idade'))
    if idade>60:
        cont1=cont1+1
    else:
        cont2=cont2+1
    soma=soma+idade
p1=(cont1/n)*100
p2=(cont2/n)*100
média=soma/n
print('%.2f' %média)        
print('%.2f' %p1)
print('%.2f' %p2)

 
   