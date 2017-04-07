investimento=float(input('Digite o valor do investimento inicial:' ))
taxa=float(input('Digite a taxa de crescimento percentual: '))

r1=investimento+(taxa*investimento)

print ('%.2f' %r1)
