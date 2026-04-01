# from functools import reduce
# n=3
# fib=lambda n:n if n<=1 else fib(n-1)+fib(n-2)
# result= fib(10)
# print(result)
# import functools
# lis=[1,3,5,6,2]
# print("The sum of the list elements is: ",end="")
# print(functools.reduce(lambda a, b:a+b,lis))
# print("The maximum element of the list is : ",end="")
# print(functools.reduce(lambda a,b:a if a>b else b, lis))

# Exercitiul 1 
# while True:
#     j1 = input("\nJucător 1 (piatra/hartie/foarfeca): ")
#     j2 = input("Jucător 2 (piatra/hartie/foarfeca): ")

#     if j1 == j2:
#         print("Egalitate!")
#     elif (j1 == "piatra" and j2 == "foarfeca") or \
#          (j1 == "foarfeca" and j2 == "hartie") or \
#          (j1 == "hartie" and j2 == "piatra"):
#         print("Felicitări Jucător 1, ai câștigat!")
#     else:
#         print("Felicitări Jucător 2, ai câștigat!")

#     if input("Mai jucați? (da/nu): ") != "da":
#         break

# Exercitiul 2
# def generare_factura(client, **produse):
#     print(f" FACTURA PENTRU: {client}  ")
#     total=0
#     for produs, pret in produse.items():
#         print( f" {produs.capitalize()}: {pret} RON")
#         total +=pret
#     print ("-"*30)
#     print(f"Total de plata: {total} RON")
# generare_factura("Andrei Vasile", paine=5, lapte=9, telemea=35, banane=4)
# generare_factura("Adelina Cebuc", paine_neagra=10, lapte_de_ovaz=9, Covrigi=35, banane=4, piersici=15)
# Exercitiul 3
# import random
# def normalize_data(lista_numere):
#     minim=min(lista_numere)
#     maxim=max(lista_numere)
#     if  maxim == minim:
#         return[0.0]*len(lista_numere)
#     return[(x-minim)/(maxim-minim)for x in lista_numere]
# data=[10, 20, 30, 40, 50]
# normalize_data=normalize_data(data)
# print(f"Date originale: {data}")
# print(f"Date normalizate {normalize_data}")

