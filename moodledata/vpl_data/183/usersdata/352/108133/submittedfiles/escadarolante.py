# -*- coding: utf-8 -*-

def intervalo (p):
    periodo=10
    for i in range(1,len(p),1):
        periodo=periodo+(p[i]-p[i-1])
    return(periodo)