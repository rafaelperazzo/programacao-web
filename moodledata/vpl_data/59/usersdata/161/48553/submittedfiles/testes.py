n=int(input('numero:'))
atual=int(input('atual'))
cont=0
for i in range(1,n,1):
    proximo=int(input('proximo'))
    if atual!=proximo:
        cont=cont+1
    atual=proximo
print(cont)    
 
   