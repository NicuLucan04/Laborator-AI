# if nr_ghicite == 6:
#     print("INCREDIBIL! Ai câștigat MARELE PREMIU!")
# elif nr_ghicite >= 4:
#     print("Felicitări! Ai câștigat un premiu substanțial!")
# elif nr_ghicite >= 3:
#     print("Felicitări! Ai câștigat un premiu mic!")
# else:
#     print("Din păcate, nu ai câștigat de data aceasta. Mai încearcă!")
#Ex 6
# import time

# def joc_aventura():
#     inventar = []
#     print("  AVENTURĂ ÎN PĂDUREA MAGICĂ  ")
#     print("Te trezești la marginea unei păduri dese. Ceața se risipește...")
#     time.sleep(1)

    
#     alegere1 = input("\nÎn fața ta sunt două poteci. Unde mergi? (stânga/dreapta): ").lower()

#     if alegere1 == "stânga":
#         print("\nAi ajuns la un râu argintiu. Pe mal strălucește ceva.")
#         actiune = input("Vrei să cercetezi sau să mergi mai departe? (cercetează/mergi): ").lower()
        
#         if actiune == "cercetează":
#             print("Ai găsit o 'Amuleta de Smarald'! A fost adăugată în inventar.")
#             inventar.append("Amuleta de Smarald")
#         else:
#             print("Ai ignorat obiectul și ai mers mai departe.")

#     elif alegere1 == "dreapta":
#         print("\nTe întâlnești cu un spiriduș bătrân care stă pe o ciupercă.")
#         print("Spiridușul: 'Dacă îmi răspunzi la o ghicitoare, îți dau un cadou!'")
#         raspuns = input("Cât fac 7 + 5? ")
        
#         if raspuns == "12":
#             print("Spiridușul chicotește: 'Corect!' Ți-a dat o 'Papiotă Magică'.")
#             inventar.append("Papiotă Magică")
#         else:
#             print("Spiridușul a dispărut într-un nor de fum. N-ai primit nimic.")
    
#     else:
#         print("\nTe-ai rătăcit prin mărăcini pentru că n-ai ales o direcție clară.")

    
#     print("\n--- Momentul Adevărului ---")
#     print("O poartă uriașă de piatră îți blochează calea. Are o adâncitură rotundă.")
    
#     if "Amuleta de Smarald" in inventar:
#         print("Amuleta ta începe să lumineze! Poarta se deschide spre un oraș de aur.")
#         print("FELICITĂRI! Ai câștigat jocul!")
#     else:
#         print("Nu ai obiectul necesar pentru a deschide poarta. Rămâi captiv în pădure...")
#         print("SFÂRȘITUL JOCULUI.")

#     print(f"\nInventarul tău final: {inventar}")


# joc_aventura()
# Ex 7
# def analizeaza_sentimentul(text):
#     text = text.lower()
#     cuvinte_pozitive=["bine", "frumos", "super", "excelent", "minunat"]
#     cuvinte_negative=["urat", "prost", "groaznic", "dezamagitor"]
#     este_pozitiv = any(cuvant in text for cuvant in cuvinte_pozitive)
#     este_negativ = any(cuvant in text for cuvant in cuvinte_negative)
#     if este_pozitiv:
#         return "Comentariu pozitiv!"
#     elif este_negativ:
#         return "Comentariu negativ!"
#     else:
#         return "Comentariu neutru."
# comentariu_utilizator = input("Introdu un comentariu: ")
# rezultat = analizeaza_sentimentul(comentariu_utilizator)

# print(rezultat)
# Ex8

import time

def proceseaza_tranzactii():
    tari_risc = ["Coreea de Nord", "Siria", "Iran"]
    tranzactii_suspecte_count = 0
    utilizator_blocat = False
    
    print("Sistem de Monitorizare Bancară ")
    
    while not utilizator_blocat:
        print(f"\n[Status: {tranzactii_suspecte_count}/3 alerte detectate]")
        
        try:
            suma = float(input("Introduceți suma tranzacției (RON): "))
            tara = input("Introduceți țara de origine: ").strip()
        except ValueError:
            print("Eroare: Vă rugăm să introduceți o sumă validă.")
            continue

        
        status = "Sigură"
        motiv = ""

        if tara.title() in [t.title() for t in tari_risc]:
            status = "Frauduloasă"
            motiv = "(țară cu risc ridicat)"
            tranzactii_suspecte_count += 1
        elif suma > 10000:
            status = "Suspicioasă"
            motiv = "(sumă mare)"
            tranzactii_suspecte_count += 1
        
        
        print(f"Tranzacție: {suma} RON din {tara} → {status} {motiv}")

        
        if tranzactii_suspecte_count >= 3:
            utilizator_blocat = True
            print("\n" + "!"*40)
            print("ALERTA: 3 tranzacții suspecte detectate!")
            print("CONT BLOCAT PENTRU SECURITATE.")
            print("!"*40)


proceseaza_tranzactii()