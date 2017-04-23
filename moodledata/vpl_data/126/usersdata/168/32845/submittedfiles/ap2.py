# -*- coding: utf-8 -*-
n1=float(input('Digite o número: ))
n2=float(input('Digite o número: ))
n3=float(input('Digite o número: ))
n4=float(input('Digite o número: ))
if (n1>n2) and (n1>n3) and (n1>n4):
    print(n1)
    print(n4)
elif (n2>n1) and (n2>n3) and (n2>n4):
    print(n2)
    print(n3)
elif (n3>n1) and (n3>n2) and (n3>n4):
    print(n3)
    print(n4)
else:
    print(n4)
    print(n3)


