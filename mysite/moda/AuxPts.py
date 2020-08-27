from .Point import *
from .Node import *
from operator import itemgetter

class AuxQt():

    def extrairPontosDf(self, df):
        # df = self.dfQuadtree.drop(['image_name'],axis=1)
        objPts = []

        for index, row in df.iterrows():
            pt = Point(row['X'], row['Y'], index)
            objPts.append(pt)

        return objPts

    def ordenarRegCresc(self, listReg):
        dicRegioes = {}
        for reg in listReg:
            qtdPtsReg = len(reg.getPoints())
            dicRegioes[reg] = qtdPtsReg

        dicRegioes = dict(sorted(dicRegioes.items(), key=itemgetter(1)))
        #print("Regiões ordenadas:", dicRegioes)
        listNodesSorted = list(dicRegioes.keys())
        return listNodesSorted

    def dividirReg(self,pai=Node):
        PmX = (pai.getxMax() + pai.getxMin())/2
        PmY = (pai.getyMax() + pai.getyMin())/2

        #3ºQuadrante
        #print("3ºQuadrante")
        ptsReg1 = self.contem(pai.getPoints(), pai.getxMin(), pai.getyMin(), PmX, PmY)
        R1 = Node(pai.getxMin(), pai.getyMin(), PmX, PmY,ptsReg1)

        #2ºQuadrante
        #print("2ºQuadrante")
        ptsReg2 = self.contem(pai.getPoints(), pai.getxMin(), PmY, PmX, pai.getyMax())
        R2 = Node(pai.getxMin(), PmY, PmX, pai.getyMax(),ptsReg2)

        #4ºQuadrante
        #print("4ºQuadrante")
        ptsReg3 = self.contem(pai.getPoints(), PmX, pai.getyMin(), pai.getxMax(), PmY)
        R3 = Node(PmX, pai.getyMin(), pai.getxMax(), PmY,ptsReg3)

        #1ºQuadrante
        #print("1ºQuadrante")
        ptsReg4 = self.contem(pai.getPoints(), PmX, PmY, pai.getxMax(), pai.getyMax())
        R4 = Node(PmX, PmY, pai.getxMax(), pai.getyMax(),ptsReg4)

        return [R1,R2,R3,R4]

    def contem(self,points,xmin,ymin,xmax,ymax):
        #print(xmin,ymin,xmax,ymax)
        pts = []
        for point in points:
            if point.x >= xmin and point.x < xmax and point.y >= ymin and point.y < ymax:
                pts.append(point)
        return pts
