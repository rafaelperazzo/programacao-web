n=int(input('numero:'))
soma=0
cont1=0
cont2=0
for i in range(1,n+1,1):
    idade=int(input('idade'))
    if idade>60:
        cont1=cont1+1
print(cont1)
    else:
        cont2=cont2+1
print(cont2)
soma=soma+idade
média=soma/n
print(média)        
    

 
   