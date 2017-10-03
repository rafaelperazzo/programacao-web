# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
cont=0
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
num6=int(input())
num7=int(input())
num8=int(input())
num9=int(input())
num10=int(input())
num11=int(input())
num12=int(input())
list_Y=[num1,num2,num3,num4,num5,num6]
list_MS=[num7,num8,num9,num10,num11,num12]
for y in list_y:
    if y in list_MS:
        cont+=1
if cont==3:
    print("terna")
elif cont==4:
    print("quadra")
elif cont==5:
    print("quina")
elif cont>=6:
    print("sena")
else:
    print("azar")