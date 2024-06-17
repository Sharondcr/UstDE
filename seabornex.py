import numpy as np
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# print(sns.get_dataset_names())
tips=sns.load_dataset('tips')
print(tips.head())
gap=px.data.gapminder()
print(gap)
""""
sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter")
plt.title("Total Bill vs Tip")
plt.show()"""

# g=sns.scatterplot(data=tips,x="total_bill",y="tip")
# g.set_title("Total Bill vs Tip")
# plt.show()
# india=gap[(gap["country"]=="India")]
# sns.relplot(data=india,x="lifeExp",kind="hist")
# plt.title("YoY life Expatancy of india")
# plt.show()
# g=sns.barplot(data=tips,x='day',y='total_bill',estimator=np.median,errorbar=None)
# g.set_title('Daywise total bill')
# plt.show()
# g=sns.pointplot(data=tips, x='day', y='tip',hue='sex')
# plt.show()
sns.catplot(kind="box",data=tips,y='tip')
plt.title('Distribution of tips')
plt.show()