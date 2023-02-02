import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage
df = pd.read_csv (r'Species.csv')
print (df)
df = df.set_index('Species')
Z = hierarchy.linkage(df, 'ward')
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)

dendrogram(Z, color_threshold=250)
plt.axhline(y=250, c='grey', lw=1, linestyle='dashed')
plt.show()
hierarchy.dendrogram(Z, orientation="right", labels=df.index)
plt.show()
# or
hierarchy.dendrogram(Z, orientation="left", labels=df.index)
plt.show()
