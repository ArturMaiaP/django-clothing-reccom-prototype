import pandas as pd


def get_df_treino(df_teste, list_rel, list_irrel):
    list_rel = [item.replace("/static/","") for item in list_rel]
    relevante_idx = df_teste.loc[df_teste['name'].isin(list_rel)].index
    df_relevante = df_teste.loc[relevante_idx, :]
    df_relevante['Class'] = 1.0

    list_irrel = [item.replace("/static/","") for item in list_irrel]
    irrelevante_idx = df_teste.loc[df_teste['name'].isin(list_irrel)].index
    df_irrelevante = df_teste.loc[irrelevante_idx, :]
    df_irrelevante['Class'] = -1.0

    frames = [df_relevante, df_irrelevante]
    return pd.concat(frames)


def update_df_teste(df_treino, df_teste):
    for name in df_treino.name:
        df_teste = df_teste[df_teste.name != name]

    return df_teste
