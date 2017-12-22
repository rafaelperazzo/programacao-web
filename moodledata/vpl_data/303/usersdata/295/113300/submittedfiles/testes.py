s = str(input('Informe seu sexo :'))
while s not in 'MmFf':
    s = str(input("Dados invalido. Digite novamente ")).strip().upper()[0] 
print(s)