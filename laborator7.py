import pandas as pd
data=pd.read_csv('data.csv')
pd.set_option('display.max_rows', None)    
pd.set_option('display.max_columns', None)       
#print(data)
# Ex 2
# rezultat = data[data['Age'] > 40].head(10)
# print(rezultat)
# # Ex 3
# jucatori_tineri_top85 = data[(data['Overall'] >= 85) & (data['Age'] < 25)]

# print(jucatori_tineri_top85)
# # Ex 4
# skillmoves = data.sort_values(by='Skill Moves', ascending=False)
# print(data.head())
# #Ex 5
# contracte_2021 = data[data['Contract Valid Until'] == 2021]

# print(contracte_2021)
# # Ex 6
# dimensiuni = data.shape
# print(f"Setul de date are {dimensiuni[0]} rânduri și {dimensiuni[1]} coloane.")

# jucatori_unici = data['Name'].nunique()
# print(f"Avem {jucatori_unici} jucători unici.")
# # Ex 7
# top_nationalitati = data['Nationality'].value_counts()


# print("Top 5 nationalitati:")
# print(top_nationalitati.head(5))


# print(f"\nCea mai frecventă naționalitate este: {top_nationalitati.idxmax()}")
# Ex 8
# import matplotlib.pyplot as plt


# top_5 = data['Nationality'].value_counts().head(5)


# plt.figure(figsize=(10, 7))
# plt.pie(top_5, labels=top_5.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'orange', 'pink', 'lightgrey'])


# plt.title('Proporția jucătorilor pe naționalități (Top 5)')
# plt.show()
# Ex 9
# medii_atribute = data.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()


# print(medii_atribute.head(10))
# Ex 10
# data['Position'] = data['Position'].fillna("Unknown")


# print(f"Valori lipsă rămase în 'Position': {data['Position'].isnull().sum()}")
# Ex 11
# cluburi_top = data.groupby('Club')['Overall'].mean()


# cel_mai_bun_club = cluburi_top.idxmax()
# media_maxima = cluburi_top.max()

# print(f"Clubul cu cea mai mare medie de Overall este: {cel_mai_bun_club}")
# print(f"Media acestuia este: {media_maxima:.2f}")


# print("\nTop 5 cluburi după media Overall:")
# print(cluburi_top.sort_values(ascending=False).head(5))
# Ex 12
# 1. Funcție pentru a converti formatele de tip '€100K' sau '€10M' în numere reale
# def clean_currency(value):
#     if isinstance(value, str):
#         value = value.replace('€', '').replace(',', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return float(value)


# data['Value_Num'] = data['Value'].apply(clean_currency)
# data['Wage_Num'] = data['Wage'].apply(clean_currency)


# numar_jucatori = (data['Value_Num'] > data['Wage_Num']).sum()

# print(f"Numărul de jucători cu valoarea de transfer mai mare decât salariul este: {numar_jucatori}")
# Ex 13

# data['is_underpaid'] = data['Wage_Num'] < (data['Value_Num'] / 100)

# print(data[['Name', 'Wage', 'Value', 'is_underpaid']].head())

# print(f"\nJucători subplătiți: {data['is_underpaid'].sum()}")
# Ex 14

# data['Scor'] = (0.3 * data['Overall']) + \
#              (0.3 * data['Potential']) + \
#              (0.2 * data['SprintSpeed'])


# data_sortat = data[['Name', 'Overall', 'Potential', 'SprintSpeed', 'Scor']].sort_values(by='Scor', ascending=False)


# print(data_sortat.head(10))
# Ex 15


# # Folosim .copy() pentru a evita avertismentele de tip SettingWithCopyWarning
# df_afacere = data[['Name', 'Wage', 'Value']].copy()


# def clean_currency(value):
#     if isinstance(value, str):
#         value = value.replace('€', '').replace(',', '')
#         if 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         elif 'K' in value:
#             return float(value.replace('K', '')) * 1000
#     return float(value)

# df_afacere['Wage_Num'] = df_afacere['Wage'].apply(clean_currency)
# df_afacere['Value_Num'] = df_afacere['Value'].apply(clean_currency)


# # Această diferență arată care jucători sunt o "afacere bună" (valoare mare, salariu mic)
# df_afacere['difference'] = df_afacere['Value_Num'] - df_afacere['Wage_Num']


# df_afacere = df_afacere.sort_values(by='difference', ascending=False)


# print("\n=== JUCĂTORI CU CELE MAI BUNE 'AFACERI' (Top 10) ===")
# print("(Jucători cu cea mai mare diferență: valoare de transfer - salariu)")
# print("\n", df_afacere[['Name', 'Wage', 'Value', 'difference']].head(10))

# Ex 16 
import matplotlib.pyplot as plt
import seaborn as sns


df_afacere = data[['Name', 'Wage', 'Value', 'Overall']].copy()


def clean_currency(value):
    if isinstance(value, str):
        value = value.replace('€', '').replace(',', '')
        if 'M' in value:
            return float(value.replace('M', '')) * 1000000
        elif 'K' in value:
            return float(value.replace('K', '')) * 1000
    return float(value)

df_afacere['Wage_Num'] = df_afacere['Wage'].apply(clean_currency)
df_afacere['Value_Num'] = df_afacere['Value'].apply(clean_currency)


df_afacere['difference'] = df_afacere['Value_Num'] - df_afacere['Wage_Num']


df_afacere = df_afacere.sort_values(by='difference', ascending=False)


print("\n=== JUCĂTORI CU CELE MAI BUNE 'AFACERI' (Top 10) ===")
print(df_afacere[['Name', 'Wage', 'Value', 'difference']].head(10))


plt.figure(figsize=(14, 8))


sns.scatterplot(data=df_afacere, x='Wage_Num', y='Value_Num', 
                hue='difference', size='Overall', 
                palette='viridis', sizes=(50, 300), alpha=0.7)

plt.xlabel('Salariu (€)', fontsize=12)
plt.ylabel('Valoare Transfer (€)', fontsize=12)
plt.title('Analiza Jucătorilor: Salariu vs Valoare de Transfer\n(Culoare = Diferență, Mărime = Overall)', 
          fontsize=14, fontweight='bold')


ax = plt.gca()
ax.ticklabel_format(style='plain', axis='x')
ax.ticklabel_format(style='plain', axis='y')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()
