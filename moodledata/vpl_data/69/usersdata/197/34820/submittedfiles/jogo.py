# -*- coding: utf-8 -*-
import math
Cv=int(input('Digite o número de vitórias de C:'))
Ce=int(input('Digite o número de empatess de C:'))
Cs=int(input('Digite o número do saldo de gols de C:'))
Fv=int(input('Digite o número de vitórias de F:'))
Fe=int(input('Digite o número de empates de F:'))
Fs=int(input('Digite o número do saldo de gols de F:'))
if (Cv*3)+(Ce)>(Fv*3+Fe):
    print('C')
elif (Cv*3)+(Ce)==(Fv*3+Fe) and Cs>Fs:
    print('C')
elif (Cv*3)+(Ce)>(Fv*3+Fe):
    print('C')
elif (Cv*3)+(Ce)==(Fv*3+Fe) and Cs>Fs:
    print('C')
elif (Cv*3)+(Ce)==(Fv*3+Fe) and Cs==Fs:
    print('=')
else:
    print('=')