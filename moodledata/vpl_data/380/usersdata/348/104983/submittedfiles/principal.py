# -*- coding: utf-8 -*-
a = int(input( ' a '))
b = int(input( ' b '))

da = 0 
db = 0

while a >= 1:
    da = da +1
    a = a//10
while b > 0:
    db = db +1 
    b = b//10
    
print( '%.d' %da)
print('%.d' %db)



