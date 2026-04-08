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
# Ex 4
# from functools import reduce
# lista=[3,4,5]
# listalapatrat=list(map(lambda x:x**2, lista))
# print(listalapatrat)
# EX 5
# a= [(0,2),(4,3),(9,9),(10,-1)]
# sorted_a=sorted(a,key=lambda x: x[1])
# print(sorted_a)
# Ex 6
# lista=[1,2,3,4,5,6,7,8,9,10]
# lista_pare=list(filter(lambda x: x%2==0, lista))
# lista_impare=list(filter(lambda x: x%2!=0, lista))
# print(f"Lista Originala: {lista}")
# print(f"Lista numere pare: {lista_pare}")
# print(f"Lista numere impare: {lista_impare}")
# Ex 7
# preturi=[100,250,None,400,50,None,111]
# preturi_filtrate=filter(lambda x: x is not None, preturi)
# preturi_reduse=list(map(lambda x:x*0.9, preturi_filtrate))
# print(f"Preturi originale: {preturi}")
# print(f"Preturi dupa filtrare si reducere: {preturi_reduse}")
# Ex 8
# import datetime
# timp=datetime.datetime.now()
# an=lambda d:d.year
# luna=lambda d:d.month
# ziua=lambda d:d.day
# ora=lambda d:d.time()
# print(f"Data completa: {timp}")
# print(f"Anul:     {an(timp)}")
# print(f"Luna:      {luna(timp)}")
# print(f"Ziua:      {ziua(timp)} ")
# print(f"Ora:    {ora(timp)}")
# Ex 9
# list1 = [1, 2, 3, 4, 5] 
# list2 = [10, 20, 30, 40, 50] 

# def sum_lists(l1, l2):
   
#     return list(map(lambda x: x[0] + x[1], zip(l1, l2)))

# result = sum_lists(list1, list2) 
# print(result) 
# Ex10
# pare = [x for x in range(101) if x % 2 == 0]
# pare_v2 = [x for x in range(0, 101, 2)]
# print(pare)
# cuburi = [x**3 for x in range(10)]
# print(cuburi)
# lista_a = [1, 2, 3, 4, 5, 9]
# lista_b = [3, 4, 5, 6, 7, 8, 9]
# comune = [x for x in lista_a if x in lista_b]
# print(comune)
# Ex11
# primele_pare = {x for x in range(0, 20, 2)}
# print(primele_pare)
# text = "programare in python"
# litere_distincte = {char for char in text if char.isalpha()}
# print(litere_distincte)
# fraza = "Invatarea limbajului Python este o experienta fascinanta"
# cuvinte_lungi = {cuvant for cuvant in fraza.split() if len(cuvant) >= 5}
# print(cuvinte_lungi)
# Ex 12
# patrate = {x: x**2 for x in range(1, 11)}
# print(patrate)
# text = "python programming"
# frecventa_litere = {char: text.count(char) for char in text if char.isalpha()}
# print(frecventa_litere)
# divizori_dict = {
#     n: [d for d in range(1, n + 1) if n % d == 0] 
#     for n in range(1, 11)
# }
# for numar, divizori in divizori_dict.items():
#     print(f"{numar}: {divizori}")