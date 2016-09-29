# -*- coding: utf-8 -*-
from __future__ import division
p=input('peso em kg:')
a=input('altura em metros:')
i= p/a**2
if i<20:
    print('ABAIXO')
elif 20<=i<=25:
    print('NORMAL')
elif 25<i<=30:
    print('SOBREPESO')
elif 30<i<=40:
    print('OBESIDADE')
elif 40<i:
    print('OBESIDADE GRAVE')
