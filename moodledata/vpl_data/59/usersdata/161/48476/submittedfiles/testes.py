n=int(input('numero:'))
soma=0
maior=0
menor=150
for i in range(1,n+1,1):
    idade=int(input('idade'))
    if idade>maior:
        maior=idade
    if idade<menor:
        menor=idade
    soma=soma+idade
média=soma/n
print('%.2f' %média)        
print(maior)
print(menor)

 
   