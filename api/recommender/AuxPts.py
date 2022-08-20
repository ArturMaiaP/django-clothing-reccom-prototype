from .Point import *
from .Node import *
from operator import itemgetter


class AuxQt:

    @staticmethod
    def extrair_pontos_df(df):
        # df = self.dfQuadtree.drop(['name'],axis=1)
        obj_pts = []

        for index, row in df.iterrows():
            pt = Point(row['x'], row['y'], index)
            obj_pts.append(pt)

        return obj_pts

    @staticmethod
    def ordenar_reg_cresc(list_reg):
        dic_regioes = {}
        for reg in list_reg:
            qtd_pts_reg = len(reg.get_points())
            dic_regioes[reg] = qtd_pts_reg

        dic_regioes = dict(sorted(dic_regioes.items(), key=itemgetter(1)))
        # print("Regiões ordenadas:", dicRegioes)
        list_nodes_sorted = list(dic_regioes.keys())
        return list_nodes_sorted

    def dividir_reg(self, pai=Node):
        pm_x = (pai.get_x_max() + pai.get_x_min())/2
        pm_y = (pai.get_y_max() + pai.get_y_min())/2

        # 3ºQuadrante
        # print("3ºQuadrante")
        pts_reg1 = self.contem(pai.get_points(), pai.get_x_min(), pai.get_y_min(), pm_x, pm_y)
        r1 = Node(pai.get_x_min(), pai.get_y_min(), pm_x, pm_y, pts_reg1)

        # 2ºQuadrante
        # print("2ºQuadrante")
        pts_reg2 = self.contem(pai.get_points(), pai.get_x_min(), pm_y, pm_x, pai.get_y_max())
        r2 = Node(pai.get_x_min(), pm_y, pm_x, pai.get_y_max(), pts_reg2)

        # 4ºQuadrante
        # print("4ºQuadrante")
        pts_reg3 = self.contem(pai.get_points(), pm_x, pai.get_y_min(), pai.get_x_max(), pm_y)
        r3 = Node(pm_x, pai.get_y_min(), pai.get_x_max(), pm_y, pts_reg3)

        # 1ºQuadrante
        # print("1ºQuadrante")
        pts_reg4 = self.contem(pai.get_points(), pm_x, pm_y, pai.get_x_max(), pai.get_y_max())
        r4 = Node(pm_x, pm_y, pai.get_x_max(), pai.get_y_max(), pts_reg4)

        return [r1, r2, r3, r4]

    @staticmethod
    def contem(points, xmin, ymin, xmax, ymax):
        # print(xmin,ymin,xmax,ymax)
        pts = []
        for point in points:
            if xmin <= point.x < xmax and ymin <= point.y < ymax:
                pts.append(point)
        return pts

    def imprimir_pts(self,pts):
        for pt in pts:
            print("### PTX: ",pt.get_x(), " ### PTY: ", pt.get_y(), ".\n" )


