deposito = float(input("digite o valor do deposito=  "))
taxa = float(input("digite o valor da taxa=  "))
ano = 1
saldo = deposito
while ano <=0:
    saldo = saldo + (saldo*(taxa/100))
    print = ('%.2f' % saldo)
    ano = ano+1