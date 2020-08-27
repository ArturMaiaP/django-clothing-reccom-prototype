import pandas as pd
from .Node import *
from .AuxPts import *
from math import ceil
import random

class QuadTree():
    def __init__(self):
        # self.ptsQTree = []
        #self.contador = 0
        self.limite = 6
        self.limProf = 10
        self.eps = 0.001
        self.auxQt = AuxQt()

    def selectImgQuadTree(self, dfAtributos, amostras):
        pontos = self.auxQt.extrairPontosDf(dfAtributos)

        xmax = dfAtributos['X'].max() + self.eps
        xmin = dfAtributos['X'].min()

        ymax =  dfAtributos['Y'].max() + self.eps
        ymin =  dfAtributos['Y'].min()
        root = Node(xMin=xmin, yMin=ymin, xMax=xmax, yMax=ymax, points=pontos)

    # Chamar Função Para Quebrar regiões e salvar childrens
        root = self.construirQuadTree(root, 0)

    #Selecionar os pontos no quadtree
        ptsQTree = self.selecionarQuadTree(regiao=root, n=amostras)

        listIdx = []
        for pt in ptsQTree:
            listIdx.append(pt.idxDf)

        dfImagens = dfAtributos.loc[listIdx, :]
        #print(dfImagens)

        listaImagens = dfImagens['image_name'].values.tolist()

        return listaImagens

    def construirQuadTree(self, regiao, nivel):

        if len(regiao.getPoints()) <= self.limite or nivel >= self.limProf:
            # print("Região atingiu o limite mínimo de pontos ou nível maximo de profundidade")
            return
        else:
            listReg = self.auxQt.dividirReg(regiao)
            listRegSorted = self.auxQt.ordenarRegCresc(listReg)

            R1 = listRegSorted[0]
            self.construirQuadTree(R1, nivel + 1)

            R2 = listRegSorted[1]
            self.construirQuadTree(R2, nivel + 1)

            R3 = listRegSorted[2]
            self.construirQuadTree(R3, nivel + 1)

            R4 = listRegSorted[3]
            self.construirQuadTree(R4, nivel + 1)

            regiao.childrens = [R1, R2, R3, R4]
            return regiao

    def selecionarQuadTree(self, regiao, n):
        ptsQTree = []

        if len(regiao.getChildrens()) == 0:
            ptsQTree = ptsQTree + random.sample(regiao.getPoints(), min(n, len(regiao.getPoints())))

        elif len(regiao.getPoints()) <= n:
            ptsQTree = ptsQTree + regiao.getPoints()

        elif n < 4:
            faltam = n
            while faltam > 0:
                R = regiao.getChildrens()[random.randint(1, 4) - 1]
                if len(R.getPoints()) > 0:
                    ptSelect = random.choice(regiao.getPoints())
                    ptsQTree.append(ptSelect)
                    # self.selecionarQuadTree(R, 1)
                    regiao.removePt(ptSelect)
                    faltam = faltam - 1

        else:
            listReg = regiao.getChildrens()
            listRegSorted = self.auxQt.ordenarRegCresc(listReg)

            faltam = n
            samplesize = ceil(faltam / 4)

            R1 = listRegSorted[0]
            ptsQTree = ptsQTree + self.selecionarQuadTree(R1, min(samplesize, len(R1.getPoints())))
            faltam = faltam - min(samplesize, len(R1.getPoints()))

            if faltam <= 0:
                return

            samplesize = ceil(faltam / 3)
            R2 = listRegSorted[1]
            ptsQTree = ptsQTree + self.selecionarQuadTree(R2, min(samplesize, len(R2.getPoints())))
            faltam = faltam - min(samplesize, len(R2.getPoints()))

            if faltam <= 0:
                return

            samplesize = ceil(faltam / 2)
            R3 = listRegSorted[2]
            ptsQTree = ptsQTree + self.selecionarQuadTree(R3, min(samplesize, len(R3.getPoints())))
            faltam = faltam - min(samplesize, len(R3.getPoints()))

            if faltam <= 0:
                return
            R4 = listRegSorted[3]
            ptsQTree = ptsQTree + self.selecionarQuadTree(R4, faltam)
            faltam = faltam - min(samplesize, len(R4.getPoints()))

            if faltam > 0:
                pts = self.selecionarQuadTree(regiao, faltam)
                ptsQTree = ptsQTree + pts

        # print(len(ptsQTree))

        return ptsQTree


