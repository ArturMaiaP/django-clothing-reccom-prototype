import os
from .Util import *
from .SvmStochastic import *
from .Constantes import TAMANHO_MINIMO_SVM
from .entropy import EntropyCalculator


class SelectImages:
    def __init__(self):
        self.sample = 12
        self.entropy_calculator = EntropyCalculator()
        
    def init_app(self, data):
        self.df_teste = data

    def select_images_distance(self, slots=None):
        qt = QuadTree()
        df = self.df_teste
        
        if slots:
            for key in slots:
                for value in slots[key]:
                    df = df[df[key] == value]
                    
        return qt.select_img_quadtree(df, self.sample)

    def select_images_svm(self, list_rel, list_irrel, slots=None):
        df = self.df_teste
        if slots:
            for key in slots:
                for value in slots[key]:
                    df = df[df[key] == value]

        df_treino = get_df_treino(df, list_rel, list_irrel)
        
        if len(df_treino) < TAMANHO_MINIMO_SVM:
            return self.select_images_distance(slots)
        
        df = update_df_teste(df_treino, df)

        df_classified = run_svm(df, df_treino)

        return select_img_svm_inverse_transf(df_classified, self.sample)

    def select_best_svm(self, list_rel, list_irrel, slots=None):
        df = self.df_teste
        if slots:
            for key in slots:
                for value in slots[key]:
                    df = df[df[key] == value]

        df_treino = get_df_treino(df, list_rel, list_irrel)
        
        if len(df_treino) < TAMANHO_MINIMO_SVM:
            return self.select_images_distance(slots)[0]
        
        df = update_df_teste(df_treino, df)

        df_classified = run_svm(df, df_treino)
        
        return df_classified.iloc[0].to_dict()

    def entropy(self, slots):
        df = self.df_teste
        for key in slots:
            for value in slots[key]:
                df = df[df[key] == value]
        return self.entropy_calculator.entropy(df)
