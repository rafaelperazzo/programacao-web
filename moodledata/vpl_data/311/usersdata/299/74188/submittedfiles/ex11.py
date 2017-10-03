dia1=input('Dia: ')
mes1=input('Mes: ')
ano1=input('Ano: ')
dia2=input('Dia: ')
mes2=input('Mes: ')
ano2=input('Ano: ')
Data1=dia1+mes1+ano1
Data2=dia2+mes2+ano2
if Data1>Data2:
    print('DATA1')
elif Data2>Data1:
    print('DATA2')
else:
    print('IGUAIS')