from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
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
#Ex 7
# X = df[['bmi']]
# y = df['target']


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# model = LinearRegression()
# model.fit(X_train, y_train)


# y_pred = model.predict(X_test)


# mse = mean_squared_error(y_test, y_pred)
# print(f"Eroarea pătratică medie (MSE): {mse:.2f}")


# plt.figure(figsize=(10, 6))


# plt.scatter(X_test, y_test, color='blue', label='Date reale (Test)', alpha=0.7)


# plt.plot(X_test, y_pred, color='red', linewidth=3, label='Linia de regresie')

# plt.title('Regresie liniară: BMI vs Scor Diabet')
# plt.xlabel('BMI (Index de masă corporală - standardizat)')
# plt.ylabel('Scor progresie boală')
# plt.legend()
# plt.grid(True)
# plt.show()
#Ex 8
X = df[['bmi', 'bp']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
print("Coeficienții modelului:")
print(f" - BMI: {model.coef_[0]:.2f}")
print(f" - BP (Tensiune arterială): {model.coef_[1]:.2f}")
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"\nScorul R² pe setul de testare: {r2:.4f}")