# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a,x,y):
    lv=[]
    lh=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==