import math
def mdc( n1, n2):
    if (n1 !=0 and n2 !=0):
        if (n1>n2):
            dividendo=n1
            divisor=n2
        else:
            dividendo=n2
            divisor=n1
        while (dividendo%divisor!=0):
            resto= dividendo%divisor
            dividendo=divisor
            divisor=resto
        return divisor
    else:
        print('os dois valores não podem ser zero')
n1=int(argv(1))
n2=int(argv(2))
print('o MDC de:' ,n1, 'e', n2, '=', mcd(n1,n2))