import math
a=int(input('digite a:'))
b=int(input('digite b:'))
    if a!=0 and b!=0:
        if (a>b):
            dividendo=a
            divisor=b
        else:
            dividendo=b
            divisor=a
        while (dividendo%divisor!=0):
            resto=dividendo%divisor!=0
            dividenod=divisor
            divisor=resto

print(mdc)
