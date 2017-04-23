cv=int(input('Digite o número de vitórias do Cormingo:'))
ce=int(input('Digite o número de empates do Cormingo:'))
cs=int(input('Digite o número de saldo de gols do Cormingo:'))
fv=int(input('Digite o número de vitórias do Flaminthians:'))
fe=int(input('Digite o número de empates do Flaminthians:'))
fs=int(input('Digite o npumero de saldo de gols do Flaminthians:'))
if (cv>fv):
    print('C')
elif (fv>cv):
    print('F')
    if (cv==fv) and (ce>fe):
        print('C')
    elif (cv==fv) and (ce<fe):
        print('F')
        if (cv==fv) and (ce==fe) and (cs>fs):
            print('C')
        elif (cv==fv) and (ce==fe) and (cs<fs):
            print('F')
else:
    print('=')
