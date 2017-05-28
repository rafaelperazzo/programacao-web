# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n"))
i=int(input("i"))
j=int(input("j"))
if contador==n:
    break
else:
    for num in range(0,n+1,1):
        if numero % i == 0 or numero % j == 0:
            print(num)
            contador=contador+1
   