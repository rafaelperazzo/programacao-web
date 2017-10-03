# -*- coding: utf-8 -*-
num=int(input("Número: "))
d1=int(num/(10**8))
d2=int(num/(10**7) - d1)
print d2 + d1