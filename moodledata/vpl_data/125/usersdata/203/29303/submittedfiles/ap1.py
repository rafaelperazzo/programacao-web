# -*- coding: utf-8 -*-
a1=int(input('Digite o primeiro valor: '))
a2=int(input('Digite o primeiro valor: '))
a3=int(input('Digite o primeiro valor: '))
if a1>a2 and a1>a3:
    print(a1)
elif a2>=a3:
    print(a2)
    print(a3)
else:
    print(a3)
    print(a2)
if a2>a1 and a2>a3:
    print(a2)
elif a3>=a1:
    print(a3)
    print(a1)
else:
    print(a1)
    print(a3)
if a3>a2 and a3>a1:
    print(a3)
elif a2>=a1:
    print(a2)
    print(a1)
else:
    print(a1)
    print(a2)