# -*- coding: utf-8 -*-
a=int(input('numero escolhido a:'))
b=int(input('numero escolhido b:'))
c=int(input('numero escolhido c:'))
d=int(input('numero escolhido d:'))
e=int(input('numero escolhido e:'))
f=int(input('numero escolhido f:'))
u=int(input('numero sorteado u:'))
v=int(input('numero sorteado v:'))
w=int(input('numero sorteado w:'))
x=int(input('numero sorteado x:'))
y=int(input('numero sorteado y:'))
z=int(input('numero sorteado z:'))
cont=0
if u==a or u==b or u==c or u==d or u==e or u==f:
    cont=cont+1
    if v==a or v==b or v==c or v==d or v==e or v==f:
        cont=cont+1
        if w==a or w==b or w==c or w==d or w==e or w==f:
            cont=cont+1
            if x==a or x==b or x==c or x==d or x==e or x==f:
                cont=cont+1
                if y==a or y==b or y==c or y==d or y==e or y==f:
                    cont=cont+1
                    if z==a or z==b or z==c or z==d or z==e or z==f:
                        cont=cont+1
print(cont)    