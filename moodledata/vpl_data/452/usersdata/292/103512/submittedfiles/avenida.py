# -*- coding: utf-8 -*-
class Quadras(object):
    def __init__(self, M, N):
        self.norte_sul = M
        self.leste_oeste = N
        self.quadras = []
        
        for i in range(1, M+1):
            linhas = []
            for j in range(1, N+1):
                linhas.append(int(input(