n=input('digiye o número de elemento:')
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor: '))

for i in range(0,n,1):
    if a[i]  %2 ==0:
        print ( a[i] )