from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
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
#ex 6
# y_pred=knn.predict(X_test_scaled)
# matrice=confusion_matrix(y_test,y_pred)
# print("\nMatricea de confuzie:")
# print(matrice)
# report=classification_report(y_test,y_pred)
# target_names=iris.target_names
# print(report)
#Ex 5
# k_values = range(1, 16)
# accuracies = []
# for k in k_values:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train, y_train)
#     y_pred = knn.predict(X_test)
#     acc = accuracy_score(y_test, y_pred)
#     accuracies.append(acc)
# plt.figure(figsize=(10, 6))
# plt.plot(k_values, accuracies, marker='o', linestyle='dashed', color='b')
# plt.title('Acuratețea modelului KNN în funcție de k')
# plt.xlabel('Valoarea lui k')
# plt.ylabel('Acuratețe (Accuracy)')
# plt.xticks(k_values)
# plt.grid(True)
# plt.show()
#Ex 7
X_2d = iris.data[:, 2:4] 
y = iris.target
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_2d, y)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap='viridis', edgecolor='k', s=60)
plt.title('Distribuția claselor de Iris (Lungime vs. Lățime petală)')
plt.xlabel('Lungime petală (cm)')
plt.ylabel('Lățime petală (cm)')
cbar = plt.colorbar(scatter)
cbar.set_ticks([0, 1, 2])
cbar.set_ticklabels(iris.target_names)
print("--- Introduceți datele pentru floarea nouă ---")
try:
    # Preluarea datelor de la utilizator din terminal
    lungime_noua = float(input("Introduceți lungimea petalei (în cm, ex: 4.5): "))
    latime_noua = float(input("Introduceți lățimea petalei (în cm, ex: 1.5): "))
    
    # Formatarea datelor pentru model (un array 2D cu o singură linie)
    floare_noua = np.array([[lungime_noua, latime_noua]])
    
    # Rularea predicției
    predictie = knn.predict(floare_noua)
    nume_clasa_prezisa = iris.target_names[predictie[0]]
    
    print(f"\n=> Rezultat: Modelul KNN a clasificat floarea ca fiind: {nume_clasa_prezisa.upper()}")
    
    # Adăugarea florii noi pe grafic sub forma unei stele roșii mari
    plt.scatter(lungime_noua, latime_noua, c='red', marker='*', s=300, edgecolor='black', label='Floarea introdusă')
    plt.legend()
    
except ValueError:
    print("Eroare: Vă rugăm să introduceți doar valori numerice (folosiți punctul pentru zecimale, ex: 2.5).")

# Afișarea graficului cu toate punctele
plt.grid(True)
plt.show()
