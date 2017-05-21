n=int(input('número de criança:'))
for i in range(1,n+1,1):
    peso=int(input('Informe o peso da criança:'))
    altura=float(input('Informe a altura da criança:'))
    imc=(peso)/(altura**2)
if imc<20:
    print('abaixo')
if imc >=20 and imc<=25:
    print('normal')
if imc >25 and imc <=30:
    print('sobrepeso')
