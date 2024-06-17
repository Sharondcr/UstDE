import matplotlib.pyplot as mpl
weight = [90,100,110,120,130,140,150]
height = [1.5,2,2.5,3,3.5,4,4.5]
fig,ax=mpl.subplots()
ax.bar(weight,height)
mpl.show()