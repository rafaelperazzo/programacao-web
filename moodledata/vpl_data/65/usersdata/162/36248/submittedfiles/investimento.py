investimento=float(input('Digite o valor do investimento inicial:'))
taxa=float(input('Digite o valor do crescimento percentual:'))
for i in range(1,11,1):
    investimento=investimento + (investimento * taxa)
    print('R$%.2f' %investimento)




