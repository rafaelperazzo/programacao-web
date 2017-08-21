valor=int(input('valor: '))
taxa=float(input('taxa: '))
taxa=taxa/100
meses=int(input('meses: '))
soma=0
for i in range(0,meses,1):
    soma=soma+valor*taxa
    valor=valor+soma
print(soma)