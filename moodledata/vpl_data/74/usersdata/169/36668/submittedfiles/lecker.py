# -*- coding: utf-8 -*-
import math
V1=float(input('Digite V1:'))
V2=float(input('Digite V2:'))
V3=float(input('Digite V3:'))
V4=float(input('Digite V4:'))
if (V1>V2) and (V2>=V3) and (V3>=V4):
    print('S')
elif (V2>V1) and (V2>V3) and (V3>=V4):
    print('S')
elif (V3>V2) and (V3>V4) and (V2>=V1)
    print('S')
elif (V4>V3) and (V3>V2) and (V2>=V1)
    print('S')
else:
    print('N')
    