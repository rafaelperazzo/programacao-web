# -*- coding: utf-8 -*-
def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return media

def dif(a):
    soma = 0
    m = media(a)
    for i in range(0,len(a),1):
        soma = soma + (a[i]-m)**2
    return soma



