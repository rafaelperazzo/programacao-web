investimento=float(input('Digite o valor do investimento inicial:' ))
taxa=float(input('Digite a taxa de crescimento percentual: '))

r1=investimento+(taxa*investimento)
r2=investimento+(taxa*r1)

print ('%.2f' %r1)
print ('%.2f' %r2)