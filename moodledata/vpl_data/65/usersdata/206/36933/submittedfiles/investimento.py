# -*- coding: utf-8 -*-
from __future__ import division

inv= float(input('Digite o valor:'))
taxa= float(input('Digite a taxa:'))

inv= inv + taxa*inv
inv2= inv + taxa*inv
inv3= inv2 + taxa*inv2
inv4= inv3 + taxa*inv3
inv5= inv4 + taxa*inv4
inv6= inv5 + taxa*inv5
inv7= inv6 + taxa*inv6
inv8= inv7 + taxa*inv7
inv9= inv8 + taxa*inv8
inv10= inv9 + taxa*inv9

print('%.2f' % inv)
print('%.2f' % inv2)
print('%.2f' % inv3)
print('%.2f' % inv4)
print('%.2f' % inv5)
print('%.2f' % inv6)
print('%.2f' % inv7)
print('%.2f' % inv8)
print('%.2f' % inv9)
print('%.2f' % inv10)

