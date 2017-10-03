# -*- coding: utf-8 -*-
a=int(input("Digite um valor a: "))
b=int(input("Digite um valor b: "))
c=int(input("Digite um valor c: "))
d=int(input("Digite um valor d: "))
if a==b+c+d:
    print ("S")
elif b+c==d:
    print ("S")
elif b==c:
    print ("S")
else:
    print ("N")



