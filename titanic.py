import pandas as pd
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
titanic=sns.load_dataset("titanic")
# sns.scatterplot(x='age',y='survived',data=titanic,hue='sex')
# plt.show()

#line plot
# sns.lineplot(x='age',y='survived',data=titanic,hue='sex')
# plt.show()

#bar plot
sns.barplot(x='age',y='survived',data=titanic,width=1.5,hue='sex')
plt.show()