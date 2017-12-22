# -*- coding: utf-8 -*-
import math
n1=int(input('Digite n1: '))
n2=int(input('Digite n2: '))
n3=int(input('Digite n3: '))
n4=int(input('Digite n4: '))
while n1>=0 :
    if n1>n2 or n2>n3 or n3>n4 or n4>n3:
        print('''S''')
        break
    elif n4>n3 or n1>n4 :
        print('''S''')
        break
    elif n1==n2==n3>n4:
        print('''N''')
        break
    elif n1==n2==n3<n4:
        print('''S''')
    else :
        print('''N''')
        break