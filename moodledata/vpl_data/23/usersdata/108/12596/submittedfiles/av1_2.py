# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int( input('Digite n:'))
x1 = int (input ('x1:'))
y1 = int (input ('y1:'))
x2 = int (input ('x2:'))
y2 = int (input ('y2:'))

if (x1<=n/2):
    if (x2<=n/2):
        if (y1<=n/2):
            if(y2<=n/2):
                print ('N')
            else:
                print ('S')
        else:
            if(y2>=2):
                print ('N')
            else:
                print ('S')
    else:
        if (y1<=n/2):
            if(y2<n/2):
                print ('N')
            else:
                print ('S')
        else:
            print ('N')
else:
        if (x2>=n/2):
            if (y1>=n/2):
                if(y2>=n/2):
                    print ('N')
                else:
                    print ('S')
            else:
                if(y2>=2):
                    print ('N')
                else:
                    print ('S')
        else:
            if (y1>=n/2):
                if(y2>=n/2):
                    print ('N')
                else:
                    print ('S')
            else:
                print ('N')
    