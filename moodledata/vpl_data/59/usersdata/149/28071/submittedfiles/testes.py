# -*- coding: utf-8 -*-
import math
e=float(0.000002)
D=float(5.6098)
rey=float(12.8932)
K=(0.25)/((math.log10(e/(3.7*D))*((5.74)/rey**0.9)))**2
print('%.4f'%K) 
