# -*- coding: utf-8 -*-
Cv=int(input('digite Cv:'))
Ce=int(input('digite Ce:'))
Cs=int(input('digite Cs:'))
Fv=int(input('digite Fv:'))
Fe=int(input('digite Fe:'))
Fs=int(input('digite Fs:'))
P1=(3*Cv)+(1*Ce)
P2=(3*Fv)+(1*Fe)
if P1>P2:
    print('C')
elif P2>P1:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
    else:
        print('=')