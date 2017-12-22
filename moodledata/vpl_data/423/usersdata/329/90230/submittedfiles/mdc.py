# -*- coding: utf-8 -*-
import math
n = int(input("digite o valor de n"))
m = int(input("digite o valor de m"))
MDC = n
while n % MDC != 0 or m % MDC != 0:
    MDC = MDC - 1
    print(MDC)
