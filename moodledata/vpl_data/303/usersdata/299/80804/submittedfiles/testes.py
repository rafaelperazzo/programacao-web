x=int(input('Saldo Médio: '))
if x>=0 and x<=500:
    print('Nenhum crédito')
elif x>=501 and x<=1000:
    print('30% do saldo médio')
elif x>=1001 and x<=3000:
    print('40% do saldo médio')  
elif x>3000:
    print('50% do saldo médio')    