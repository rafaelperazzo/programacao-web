# -*- coding: utf-8 -*-
from __future__ import division
import math
cv = input ('vitorias C:')
ce = input ('empates C:')
cs = input ('saldo C :')
fv = input ('vitorias f:')
fe = input ('empates f:')
fs = input ('saldo f :')
pc = (3*cv) + ce
pf = (3*fv) + fe
if pc > pf:
    print 'C'
elif pf >pc:
    print 'F'
else:
    print'='