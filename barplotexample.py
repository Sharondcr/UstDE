import matplotlib.pyplot as mpl
fig,ax=mpl.subplots()
months = ["Jan","Feb","Mar","Apr","May","June"]
temp = [36,42,40,48,49,36]
bar_labels = ['sunny','hot','warm','warmer','super hot','cool']
bar_colors = ['tab:blue','tab:red','tab:pink','tab:green','tab:orange','tab:blue']
ax.bar(months,temp,label=bar_labels,color=bar_colors)
ax.set_ylabel("Temperature by Month")
ax.set_title("Monthwise Temperature record")
ax.legend(title='Temperature by month')
mpl.show()