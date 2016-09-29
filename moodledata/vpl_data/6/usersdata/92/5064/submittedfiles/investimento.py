# -*- coding: utf-8 -*-
from __future__ import division

inv= input( )
taxa= input( )

inv1= inv + inv*taxa
inv2= inv2 + inv1*taxa
inv3= inv2 + inv2*taxa
inv4= inv3 + inv3*taxa
inv5= inv4 + inv4*taxa
inv6= inv5 + inv5*taxa
inv7= inv6 + inv6*taxa
inv8= inv7 + inv7*taxa
inv9= inv8 + inv8*taxa
inv10= inv9 + inv9*taxa

print('%.2f' %inv1)
print('%.2f' %inv2)
print('%.2f' %inv3)
print('%.2f' %inv4)
print('%.2f' %inv5)
print('%.2f' %inv6)
print('%.2f' %inv7)
print('%.2f' %inv8)
print('%.2f' %inv9)
print('%.2f' %inv10)