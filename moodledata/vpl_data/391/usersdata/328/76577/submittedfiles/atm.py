______________________________________
cn100 = 0
cn50 = 0
cn20 = 0
cn10 = 0
cn05 = 0
cn02 = 0
cn01 = 0
din = int(input('Digite o valor do dinheiro'))
print ('o valor que será deconposto é', din,'R$')
if (din >= 100):
cn100 = cn100 + 1
din = din - 100
elif (din >= 50):
cn50 = cn50 + 1
din = din - 50
elif (din >= 20):
cn20 = cn20 + 1
din = din - 20
elif (din >= 10):
cn10 = cn10 + 1
din = din - 10
elif (din >= 5):
cn05 = cn05 + 1
din = din - 5
elif (din >= 2):
cn02 = cn02 + 1
din = din - 1
elif (din >= 1):
cn01 = cn01 + 1
din = din - 1
print('A quantidade de notas de 100 é',cn100,'cn50 é',cn50,'cn20 é',cn20,'cn10 é',cn10,'cn5 é',cn05,'cn2 é',cn02,'cn1 é',cn01)
print ('fatorado com sucesso!')