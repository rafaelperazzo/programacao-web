n=int(input('Informe um valor:'))
s=0
for i in range (1,n+1,1):
    if (i%2==1):
        s=s+(i/(i**2))
    else:
        s=s-(i/(i**2))
print('%.5f'%s)