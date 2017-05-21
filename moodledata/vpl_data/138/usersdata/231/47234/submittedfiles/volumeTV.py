

v=int(input('digite v:')) 
t=int(input('digite t:'))  
cont=v
for i in range(1,t+1,1):
    a=int(input('digite alteração:'))
    if cont<=100:
        cont=cont+a
    if cont>=0:
        cont=cont+a
print(cont)
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 