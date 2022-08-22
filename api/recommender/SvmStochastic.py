import pandas as pd
import numpy as np
from sklearn import svm
from .QuadTree import *

CLASSES_SVM = 3
LIMITE_RANDOM_INICIAL = 0
EPS = 0.001


def run_svm(df_teste, df_treino):

    if "Class" in df_teste.columns:
        df_teste = df_teste.drop(["Class"], axis=1)

    # Separa o conjunto de treino em atributos e classe
    x = df_treino[["x", "y"]]
    y = df_treino["Class"]

    # Treina o classificador SVM
    clf = svm.SVC(kernel="rbf", gamma=0.05, C=1)

    clf.fit(x, y)

    predict_list = clf.decision_function(df_teste.drop(["name"], axis=1))

    df_teste["Class"] = predict_list
    df_teste = df_teste.sort_values(by=['Class'], ascending=False)
    # df_teste.to_csv("Anno/teste.txt", encoding='utf-8', index=False, sep=',')
    print(df_teste.head(10))
    print(df_teste.tail(10))
    return df_teste


def select_img_svm_inverse_transf(df_classified, qtd_img):

    q25 = np.percentile(df_classified['Class'], 25)
    q75 = np.percentile(df_classified['Class'], 75)
    
    positive_row_index = df_classified.loc[df_classified['Class'] > q75].index
    df_positive = df_classified.loc[positive_row_index, :]
    df_positive = calcular_prob_nao_zero(df_positive)

    negative_row_index = df_classified.loc[df_classified['Class'] < q25].index
    df_negative = df_classified.loc[negative_row_index, :]
    df_negative = calcular_prob_nao_zero(df_negative)

    zero_row_index = df_classified.loc[(df_classified['Class'] <= q75) & (df_classified['Class'] >= q25)].index
    df_zero = df_classified.loc[zero_row_index, :]
    df_zero = calcular_prob_proximo_zero(df_zero)

    list_positivas = select_img_prob_quadtree(df_positive, int(qtd_img/CLASSES_SVM), LIMITE_RANDOM_INICIAL)
    list_negativas = select_img_prob_quadtree(df_negative, int(qtd_img/CLASSES_SVM), LIMITE_RANDOM_INICIAL)
    list_zero = select_img_prob_quadtree(df_zero, int(qtd_img/CLASSES_SVM), LIMITE_RANDOM_INICIAL)

    list_final = list_positivas + list_zero + list_negativas

    print(list_final)
    return list_final


def calcular_prob_nao_zero(df):
    df['Class'] = df['Class'].abs()
    sum_svm = df["Class"].values.sum()
    df = df.sort_values(by=['Class'], ascending=True)

    list_pj = []
    list_soma_pj = []
    list_class = df["Class"].tolist()
    last = 0

    for c in list_class:
        # probabilidade para classificação do svm
        pj = c / sum_svm
        list_pj.append(pj)
        # soma cumulativa
        soma_pj = pj + last
        list_soma_pj.append(soma_pj)
        last = soma_pj

    df['Pj'] = list_pj
    df['SomaPj'] = list_soma_pj

    return df


def calcular_prob_proximo_zero(df):
    df['Class'] = df['Class'].abs()
    svm_max = df['Class'].max()

    sum_svm = (svm_max - df["Class"]).values.sum()

    df = df.sort_values(by=['Class'], ascending=True)

    list_pj = []
    list_soma_pj = []
    list_class = df["Class"].tolist()
    last = 0

    for c in list_class:
        # probabilidade para classificação do svm
        pj = (svm_max - c) / sum_svm
        list_pj.append(pj)
        # soma cumulativa
        soma_pj = pj + last
        list_soma_pj.append(soma_pj)
        last = soma_pj

    df['Pj'] = list_pj
    df['SomaPj'] = list_soma_pj
    df = df[df.Pj != 0]

    return df


def select_img_prob_quadtree(df, samples, random_min):
    new_rows = pd.DataFrame(columns=df.columns)
    list_soma = df["SomaPj"].tolist()
    qtd_select = samples * 10

    for x in range(0, qtd_select):
        u = random.uniform(random_min, 1)
        for soma in list_soma:  # lista com a soma cumulativa dda probabilidade
            if u < soma:
                df_temp = df.loc[df['SomaPj'] == soma]
                # print(dfTemp)
                # newRows = pd.concat([newRows, dfTemp])
                new_rows = pd.concat([new_rows, df_temp])
                # idx.append(df.loc[df['SomaPj']==soma].index)
                list_soma.remove(soma)
                df = df.drop(df.loc[df['SomaPj'] == soma].index, axis=0)
                break
    if len(new_rows) < samples:
        temp = select_img_prob_quadtree(df, samples - len(new_rows), (df["SomaPj"].min() - EPS))
        new_rows = pd.concat([new_rows, temp])

    if len(new_rows) > 0:
        # print("entrou aqui")
        quadtree = QuadTree()
        print(new_rows.head(10))
        # dfFinal = quadtree.selectImgQuadTreeSVM(dfImages,qtdImg)
        list_imagens = quadtree.select_img_quadtree(new_rows, samples)
        return list_imagens
    else:
        return None
