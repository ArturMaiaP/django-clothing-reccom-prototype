from .AuxPts import *
from math import ceil
import random


class QuadTree:
    def __init__(self):
        self.limite = 6
        self.limProf = 10
        self.eps = 0.001
        self.aux_qt = AuxQt()

    def select_img_quadtree(self, df_atributos, amostras):
        pontos = self.aux_qt.extrair_pontos_df(df_atributos)

        x_max = df_atributos['x'].max() + self.eps
        x_min = df_atributos['x'].min()

        y_max = df_atributos['y'].max() + self.eps
        y_min = df_atributos['y'].min()
        root = Node(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, points=pontos)

    # Chamar Função Para Quebrar regiões e salvar childrens
        root = self.construir_quadtree(root, 0)

    # Selecionar os pontos no quadtree
        pts_qtree = self.selecionar_quadtree(regiao=root, n=amostras)
        self.aux_qt.imprimir_pts(pts_qtree)

        list_idx = []
        for pt in pts_qtree:
            list_idx.append(pt.idxDf)

        df_imagens = df_atributos.loc[list_idx, :]

        lista_imagens = df_imagens['name'].values.tolist()

        return lista_imagens

    def construir_quadtree(self, regiao, nivel):

        if len(regiao.get_points()) <= self.limite or nivel >= self.limProf:
            # print("Região atingiu o limite mínimo de pontos ou nível maximo de profundidade")
            return
        else:
            list_reg = self.aux_qt.dividir_reg(regiao)
            list_reg_sorted = self.aux_qt.ordenar_reg_cresc(list_reg)

            r1 = list_reg_sorted[0]
            self.construir_quadtree(r1, nivel + 1)

            r2 = list_reg_sorted[1]
            self.construir_quadtree(r2, nivel + 1)

            r3 = list_reg_sorted[2]
            self.construir_quadtree(r3, nivel + 1)

            r4 = list_reg_sorted[3]
            self.construir_quadtree(r4, nivel + 1)

            regiao.childrens = [r1, r2, r3, r4]
            return regiao

    def selecionar_quadtree(self, regiao, n):
        pts_qtree = []

        if len(regiao.get_childrens()) == 0:
            pts_qtree = pts_qtree + random.sample(regiao.get_points(), min(n, len(regiao.get_points())))

        elif len(regiao.get_points()) <= n:
            pts_qtree = pts_qtree + regiao.get_points()

        elif n < 4:
            faltam = n
            while faltam > 0:
                reg = regiao.get_childrens()[random.randint(1, 4) - 1]
                if len(reg.get_points()) > 0:
                    pt_select = random.choice(regiao.get_points())
                    pts_qtree.append(pt_select)
                    # self.selecionarQuadTree(R, 1)
                    regiao.remove_pt(pt_select)
                    faltam = faltam - 1

        else:
            list_reg = regiao.get_childrens()
            list_reg_sorted = self.aux_qt.ordenar_reg_cresc(list_reg)

            faltam = n
            samplesize = ceil(faltam / 4)

            r1 = list_reg_sorted[0]
            pts_qtree = pts_qtree + self.selecionar_quadtree(r1, min(samplesize, len(r1.get_points())))
            faltam = faltam - min(samplesize, len(r1.get_points()))

            if faltam <= 0:
                return

            samplesize = ceil(faltam / 3)
            r2 = list_reg_sorted[1]
            pts_qtree = pts_qtree + self.selecionar_quadtree(r2, min(samplesize, len(r2.get_points())))
            faltam = faltam - min(samplesize, len(r2.get_points()))

            if faltam <= 0:
                return

            samplesize = ceil(faltam / 2)
            r3 = list_reg_sorted[2]
            pts_qtree = pts_qtree + self.selecionar_quadtree(r3, min(samplesize, len(r3.get_points())))
            faltam = faltam - min(samplesize, len(r3.get_points()))

            if faltam <= 0:
                return
            r4 = list_reg_sorted[3]
            pts_qtree = pts_qtree + self.selecionar_quadtree(r4, faltam)
            faltam = faltam - min(samplesize, len(r4.get_points()))

            if faltam > 0:
                pts = self.selecionar_quadtree(regiao, faltam)
                pts_qtree = pts_qtree + pts

        # print(len(ptsQTree))

        return pts_qtree
