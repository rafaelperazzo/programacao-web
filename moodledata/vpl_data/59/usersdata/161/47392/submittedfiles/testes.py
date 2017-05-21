cv=int(input('cv:'))
ce=int(input('ce:'))
cs=int(input('cs:'))
fv=int(input('fv:'))
fe=int(input('fe:'))
fs=int(input('fs:'))
x1=0
x2=0
x1=cv+ce
x2=fv+fe
if x1>x2:
    print('C')
elif x1<x2:
    print('F')
else:
    if cs>fs:
        print('C')
    elif cs<fs:
        print('F')
    else:
        print('=')