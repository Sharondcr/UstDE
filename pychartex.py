import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots(figsize=(6,3),subplot_kw=dict(aspect='equal'))
recipe = [
    "375 g Flour",
    "75 g Sugar",
    "250 g butter",
    "300 g berries"
]
data = [float(x.split()[0]) for x in recipe]
incredients = [(x.split()[-1]) for x in recipe]
print(data,incredients)
def func(pct,allvals):
    absolute=int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d}g)"
wedges,texts,autotexts=ax.pie(data,
                              autopct = lambda pct:func(pct,data)
                              ,textprops=dict(color="w"))
ax.legend(wedges,incredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1,0,0.5,1))
plt.setp(autotexts,size=8,weight="bold")
ax.set_title("Bakery a pie")
plt.show()