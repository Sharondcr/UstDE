import matplotlib.pyplot as mpl
import numpy as np

species = ("Adelle\n $\\mu=$3700.66g",
           "Chinstrap\n $\\mu=$3733.09g",
           "Gentoo\n $\\mu=5076.02g$",)
weight_counts = {
    "Below" : np.array([70,31,58]),
    "Above" : np.array([70,31,58])
}
bottom=np.zeros(3)
width = 0.5
fig,ax = mpl.subplots()

for boolean,weight_counts in weight_counts.items():
    p=ax.bar(species,weight_counts,width,label=boolean,bottom=bottom)
    bottom += weight_counts
ax.set_title("number of penguins with above average body mass")
ax.legend(loc="upper right")
mpl.show()