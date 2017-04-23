# -*- coding: utf-8 -*-
Cv=int(input('digite Cv:'))
Ce=int(input('digite Ce:'))
Cs=int(input('digite Cs:'))
Fv=int(input('digite Fv:'))
Fe=int(input('digite Fe:'))
Fs=int(input('digite Fs:'))
if Cv>Fv:
    print('C')
elif Fv>Cv:
    print('F')
else:
    if Ce>Fe:
        print('C')
    elif Fe>Ce:
        print('F')
    else:
        if Cs>Fs:
            print('C')
        elif Fs>Cs:
            print('F')
        else:
            print('=')