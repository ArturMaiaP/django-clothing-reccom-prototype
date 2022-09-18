import os
from .Util import *
from .SvmStochastic import *


class SelectImages:
    def __init__(self):
        self.sample = 12
        
    def init_app(self, data):
        self.df_teste = data

    def select_images_distance(self, slots=None):
        qt = QuadTree()
        df = self.df_teste
        
        if slots:
            for key in slots:
                for value in slots[key]:
                    df = df[df[value] == 1]
                    
        return qt.select_img_quadtree(df, self.sample)

    def select_images_svm(self, list_rel, list_irrel, slots=None):
        df = self.df_teste
        if slots:
            for key in slots:
                for value in slots[key]:
                    df = df[df[value] == 1]

        df_treino = get_df_treino(df, list_rel, list_irrel)
        df = update_df_teste(df_treino, df)

        df_classified = run_svm(df, df_treino)

        return select_img_svm_inverse_transf(df_classified, self.sample)

    def select_best_svm(self, list_rel, list_irrel):
        self.df_treino = pd.concat([self.df_treino, get_df_treino(self.df_teste, list_rel, list_irrel)], sort=False)
        self.df_teste = update_df_teste(self.df_treino, self.df_teste)

        df_classified = run_svm(self.df_teste, self.df_treino)
        
        return df_classified.iloc[0].to_dict()
