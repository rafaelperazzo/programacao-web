investimento=float(input('Digite o valor de investimento:'))
taxa=float(input('Digite a taxa de crescimento:'))
investimento=0
for i in range(1,11,1):
    investimento=investimento+taxa*investimento
print('O valor é %.2f' %investimento)  




