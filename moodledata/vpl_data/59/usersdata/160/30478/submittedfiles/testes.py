investimento=float(input('Digite o valor do investimento inicial:' ))
taxa=float(input('Digite a taxa de crescimento percentual: '))

r1=investimento+(taxa*investimento)
r2=r1+(taxa*investimento)
r3=r2+(taxa*investimento)

print ('%.2f' %r1)
print ('%.2f' %r2)
print ('%.2f' %r3)