import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
#reading image
img = mpimg.imread('mix.jpg')
plt.imshow(img)
plt.show()

#list

r = []
g = []
b = []
for line in img:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

print(r)

fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(r,g,b)
plt.show()


df=pd.DataFrame({"red":r,"green":g,"blue":b})
df["red"]=whiten(df["red"])
df["green"]=whiten(df["green"])
df["blue"]=whiten(df["blue"])

cluster_centers, distortion = kmeans(df[['red', 'green', 'blue']], 2)
print(cluster_centers)

for i in range(0,len(cluster_centers)):
    for j in range(0,3):
        cluster_centers[i][j]=(cluster_centers[i][j]*(df.iloc[j].std()))%255

plt.imshow([cluster_centers])
plt.show()