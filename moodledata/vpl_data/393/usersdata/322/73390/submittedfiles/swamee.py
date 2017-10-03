# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
#ENTRADA

f= float(input(' digitar valor para f: '))
L= float(input(' digitar valor para L: '))
Q= float(input(' digitar valor para Q: '))
DeltaH= float(input(' digitar valor para DeltaH: '))
v= float(input(' digitar valor para v: '))

#PROCESSAMENTO

D= ((8*f*L*Q)**2)/math.pi*9.81*DeltaH
Rey= (4*Q)/math.pi*D*v
