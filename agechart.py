import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('PatientInfo.csv')
print(df.head())
df = df.dropna(subset=['age'])
tp_age=df['age'].value_counts().rename_axis('age').reset_index(name='patients_count')
print((tp_age))
plt.figure(figsize=(10,10))
plt.pie(tp_age.patients_count,labels=tp_age.age,startangle=90,autopct='%.if%%')
plt.title("Age of patients")
plt.show()