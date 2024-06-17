import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Original Data Set")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
'oldpeak', 'slope', 'ca', 'thal', 'target']
data = pd.read_csv(url, names=columns,na_values='?')
print(data)
print("-"*80)

#Data Cleaning

# row_missing=data[data.isnull().any(axis=1)]
print("Data After Cleaning")
data.fillna(data.mean(),inplace=True)
print(data)
print("-"*80)

#Descriptive Statistics

print("Descriptive Statistics")
descriptive_stats=data.describe()
print(descriptive_stats)

# TASK1:Age Distribution

plt.hist(x=data['age'],bins='auto',edgecolor='k',alpha=0.7)
plt.xlabel('age')
plt.ylabel('frequency')
plt.title('Distribution of Ages ')
plt.show()

#Task2:Gender Distribution

group=data.groupby('sex').size().reset_index(name="count")
sns.barplot(data=group,x='sex',y='count',palette='Set2')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title("Distribution of Gender")
plt.show()

#Task3:Chest Pain Type vs Heart Disease

data['target'].replace((2,3,4),(1),inplace=True)
cp_values = [1.0,2.0,3.0]
data=data[data['cp'].isin(cp_values)]
sns.countplot(x='cp',hue='target',data=data,palette='Set2')
plt.title("Relationship between Chest Pain and Heart Disease")
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

#Task4:Cholestrol

sns.boxplot(x='chol',hue='target',data=data)
plt.ylabel("Cholestrol Levels")
plt.xlabel("Distribution of Cholestrol levels")
plt.show()

#Task5:Pair Plot

sns.pairplot(data,vars=['age','trestbps','chol','thalach'],hue='target',palette='husl')
plt.title("Pair plot of Variables with Target Differentiation")
plt.show()

#Task6:Correlation HeatMap

Correlation = data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(data=Correlation,annot=True,cmap='coolwarm',vmin=-1,vmax=1,linewidths=.5)
plt.title("Heatmap of Attribute Correlations")
plt.show()

#Task7:Exercise Induced Angina vs Maximum Heart Rate
plt.scatter(x=data['exang'].where(data['target']==1),y=data['thalach'].where(data['target']==1))
plt.scatter(x=data['exang'].where(data['target']==0),y=data['thalach'].where(data['target']==0),marker="^")
plt.legend(["Heart Disease Present","Heart Disease Not Present"])
plt.xlabel("Exercise-Induced angina")
plt.ylabel("Heart rate")
plt.title("Relationship Between Exercise Induced Angina and Maximum Heart Rate")
plt.show()




