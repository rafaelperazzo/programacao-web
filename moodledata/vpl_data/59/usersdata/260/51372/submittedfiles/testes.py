# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
for n in range(1,10000,1):
    z=n
    d1=z//100
    d2=n-d1*100
    s=d1+d2
    if s==(n)**(1/2):
        print(n)