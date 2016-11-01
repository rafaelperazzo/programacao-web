# -*- coding: utf-8 -*-
from __future__ import division

def main():
    a=int(input("digite o valor de uma moeda:"))
    b=int(input("digite o valor de outra moeda:"))
    c=int(input("digite o valor da cedula:"))
    
    possivel=false
    na=0
    while na <= c//a and not possivel:
        nb=0
        while nb <= c//b and not possivel:
            if na*a + nb*b == c:
                possivel=true
            nb = nb+1
        na=na+1
    if possivel:
        print("%d moeda(s) de %d e %d moeda(s) de %d" %(na-1,a,nb-1,b))
    else:
        print("nao e possivel trocar a cedula")
    