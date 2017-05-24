n=int(input('numero:'))
soma=0
cont=0
for i in range(1,n+1,1):
    idade=int(input('idade'))
    if idade>60:
        cont=cont+1
    print(cont)
    if idade<=60:
        cont=cont+1
    print(cont)
soma=soma+idade
média=soma/n
print(média)        
    

 
   