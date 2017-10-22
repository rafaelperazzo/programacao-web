# -*- coding: utf-8 -*-
import math
n1=int(input("Digite um numero n1: "))
n2=int(input("Digite um numero n2: "))
n3=int(input("Digite um numero n3: "))
n4=int(input("Digite um numero n4: "))
while (True):
    if n1>n2>=n3>n4 or n1>n2<=n3<n4 or n1>n2>=n3<n4<=n1 or n1<n2>n3>=n4  or n1<n2>n3>=n4>=n1 or n1<n2>n3>=n4<=n1 or n1<n2>n3<=n4 or  n1<=n2<n3>n4 or n1<=n2<n3>n4<=n1 or n1<=n2<n3>n4>=n1 or n1<=n2<=n3<n4:
        print ("S")
        break
    else:
        print ("N")
        break