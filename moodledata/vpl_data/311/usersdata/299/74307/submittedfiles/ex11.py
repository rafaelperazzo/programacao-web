dia1=input('Dia: ')
while dia1>31:
    print('Dia invalido')
    dia1=input('Dia: ')
mes1=input('Mes: ')
while mes1>12:
    print('Mes invalido')
    mes1=input('Mes: ')
ano1=input('Ano: ')
dia2=input('Dia: ')
while dia2>31:
    print('Dia invalido')
    dia2=input('Dia: ')
mes2=input('Mes: ')
while mes2>12:
    print('Mes invalido')
    mes2=input('Mes: ')
ano2=input('Ano: ')
Data1=dia1+mes1+ano1
Data2=dia2+mes2+ano2
if Data1>Data2:
    print('DATA 1')
elif Data2>Data1:
    print('DATA 2')
else:
    print('IGUAIS')