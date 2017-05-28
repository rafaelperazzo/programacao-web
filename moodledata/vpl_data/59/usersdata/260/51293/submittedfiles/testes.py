# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
i=int(input("i"))
j=int(input("j"))
if j>i:
    for numero in range(2,j+1,1):
        if i%numero==0 and j%numero==0:
            a=numero
            break
        else:
            a=1
print(a)
else:
    for numero in range(2,j+1,1):
        if i%numero==0 and j%numero==0:
            a=numero
            break
        else:
            a=1
print(a)