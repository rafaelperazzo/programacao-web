 
 
e=int(input('escreva e:'))
f=int(input('escreva f:'))
cont=e
for i in range(1,f+1,1):
     a=int(input('escreva alteração:'))
     
     if (cont+a)<=100 and cont>=0:
         cont=cont+a
     elif (cont+a)>=100:
         e=cont-100
         cont=cont-e
         
         
         
print(cont)
    