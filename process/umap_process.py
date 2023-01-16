
from sklearn.preprocessing import StandardScaler
import pandas as pd
import umap
import matplotlib.pyplot as plt

df = pd.read_csv("product.seed.csv")
encoded_df = pd.get_dummies(df[[
    "type",
    "size",
    "color",
    "pattern",
    "fabric",
]])


# print("Scaling")
# scaled = StandardScaler().fit_transform(data)

print("Umap")
reducer = umap.UMAP()
embedding = reducer.fit_transform(encoded_df.values)
embedding.shape


df['x'] = embedding[:, 0]
df['y'] = embedding[:, 1]

plt.scatter(
    embedding[:, 0],
    embedding[:, 1])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection', fontsize=24)
plt.savefig("mygraph.png")

df.to_csv("product.seed.csv")