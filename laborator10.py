from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
# X=np.array([[1],[2],[3],[4]])
# y=np.array([5,6,7,8])
# model=LinearRegression()
# model.fit(X,y)
# print(model.predict([[5]]))
diabetes=load_diabetes()
df=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df['target']=diabetes.target
#print(df.head())
#print(diabetes.feature_names)
df.describe()
#print(df.describe())
#print(df.mean())
plt.figure(figsize=(8,6))
plt.scatter(df['bmi'], df['age'], c=df['target'], cmap='viridis')
plt.title('BMI Si Varsta in functie de target')
plt.xlabel('BMI')
plt.ylabel('Varsta')
plt.colorbar(label='Target')
plt.show()