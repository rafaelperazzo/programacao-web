deposito = float(input("digite o valor do deposito=  "))
taxa = float(input("digite o valor da taxa=  "))
ano = 1
saldo = 0
while ano <=0:
    saldo = deposito + (deposito*(taxa/100))
    print = ("%.2f" % saldo)
    ano = ano + 1