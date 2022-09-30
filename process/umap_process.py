
from sklearn.preprocessing import StandardScaler
import pandas as pd
import umap

df = pd.read_csv("product.seed.csv")

data = df[[
    "a_line",
    "denim",
    "dots",
    "faux",
    "faux_leather",
    "Floral",
    "knit",
    "Lacy",
    "leather",
    "maxi",
    "midi",
    "mini",
    "pencil",
    "Pleated",
    "Printed",
    "skater",
    "Stripes"
]].values

# print("Scaling")
# scaled = StandardScaler().fit_transform(data)

print("Umap")
reducer = umap.UMAP()
embedding = reducer.fit_transform(data)
embedding.shape


df['x'] = embedding[:, 0]
df['y'] = embedding[:, 1]

df.to_csv("product.seed.csv")