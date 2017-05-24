investimento=float(input('Digite o valor do investimento inicial:'))
taxa=float(input('Digite o valor da taxa de crescimento percentual:'))
for i in range(1,11,1):
    investimento=investimento+taxa*investimento
print('%.2f' %investimento)    
