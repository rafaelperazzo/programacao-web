n = float(input('Digite um número: '))

if n >= 0:
    n = n**(1/2)
    print("%.2f" %n)
else:
    n = n**2
    print('%.2f' %n)