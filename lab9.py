from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
X=iris.data
y=iris.target

print(" Forma setului de date:", X.shape)
print("\n Denumirile atributelor:")
print(iris.feature_names)
print("\nClasele:")
print(iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("\nDimensiunea setului de antrenare:", X_train.shape)
print("\nDimensiunea setului de testare:", X_test.shape)
print(y_test.shape)
print(y_train.shape)
print(X)
#EX 3
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
print(X_train_scaled[:5])
print(X_test_scaled[:5])
#EX 4
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled,y_train)
acuratete=knn.score(X_test_scaled,y_test)
print("\nAcuratetea modelului KNN:", acuratete)