n=int(input('numero:'))
x=n
cont=0
reverso=0
while x>0:
    x=x//10
    cont=cont+1
while n>0:
    ultimo=n%10
    reverso=reverso+ultimo*(10**(cont-1))
    n=n//10
    cont=cont-1
print(reverso)    
   