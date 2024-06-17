#Univariate,Bivariate and Multivariate
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

card_approval_data=pd.read_csv("creditcarddataset.csv")
# print(card_approval_data)

#Univariate

# #Histogram for continous data
#
# sns.histplot(data=card_approval_data,x="Age",hue="Gender",kde=True)
# plt.legend(labels=["male","female"])
# plt.show()
# sns.histplot(data=card_approval_data,x="YearsEmployed",hue="Gender",kde=True)
# plt.legend(labels=["male","female"])
# plt.show()
#
# #Histogram for Categorical data
#
# sns.countplot(data=card_approval_data,x="Gender")
# plt.show()
# sns.countplot(data=card_approval_data,x="BankCustomer")
# plt.show()

#Bivariate

#continous

# print(card_approval_data[["Age","Debt","YearsEmployed","CreditScore","Income"]].corr())
# sns.scatterplot(data=card_approval_data,x="YearsEmployed",y="Income")
# plt.ylim(0,20000)
# plt.show()

# data = card_approval_data.groupby(by="Approved").agg("mean")[['Age','Debt','YearsEmployed']]
# print(data)


#categorical data
sns.countplot(data=card_approval_data,x='Approved',hue='Gender')
plt.show()

# Multivariate - It is used for more complex form of statistical analysis.it is used when there are more than two variables in the dataset
sns.pairplot(data=card_approval_data[["Age","Debt","YearsEmployed","CreditScore","Income","Approved"]],hue="Approved")
plt.show()