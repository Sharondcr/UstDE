import pandas as pd
import matplotlib.pyplot as plt
case=pd.read_csv('Case.csv')
# print(case)
province=case.loc[:'province']
confirmed=case.loc[:'confirmed']
group=case.groupby('province')['confirmed'].sum().reset_index()
print(group)
fig,chart=plt.subplots()
chart.bar(group.province,group.confirmed)
plt.xticks(rotation=75)
chart.set_ylabel("Accumulated nu confirmed")
chart.set_title("No fo corona cases")
plt.show()

