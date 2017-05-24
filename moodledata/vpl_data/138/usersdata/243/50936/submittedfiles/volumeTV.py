 -*- coding: utf-8 -*-

e=int(input('digite e:'))
f=int(input('digite f:'))
 
cont=e
for i in range(1,f+1,1):
    a=int(input('digite alteração:'))
    
    if (cont+a)<=100 and cont>=0:
        cont=cont+a
    elif (cont+a)>=100:
        e=cont-100
        cont=cont-e
print(cont)        