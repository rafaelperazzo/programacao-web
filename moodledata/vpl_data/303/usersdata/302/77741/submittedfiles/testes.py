n = float(input('Digite um número: '))

if n >= 0:
    n = n**(1/2)
    print(n)
else:
    n = n**2
    print('%f.2',n)