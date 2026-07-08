import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv('c:\\Users\\derrick\\Downloads\\projet_reussite_scolaire_stress_correlation_forte.csv')

# Relation entre les heures de révision par jour et la moyenne scolaire sur 20

plt.figure(figsize=(10, 8))


plt.subplot(2,2,1)
plt.scatter(df['heures_revision_par_jour'],df['moyenne_scolaire_sur_20'],color="blue" ,alpha=0.6, s=50)
plt.title('Rapport entre les heures de révision et la moyenne scolaire')
plt.xlabel('Heures de révision par jour')
plt.ylabel('Moyenne scolaire sur 20')
plt.xticks(np.arange(1, 7, 1))
plt.yticks(np.arange(8, 21, 1))
plt.grid(True, linestyle='--', alpha=0.4)

x = df['heures_revision_par_jour']
y = df['moyenne_scolaire_sur_20']
a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, linestyle='--', color='red')

# Relation entre les heures d'utilisation du smartphone par jour et la moyenne scolaire sur 20
plt.subplot(2,2,2)
plt.scatter(df['temps_ecran_par_jour_heures'],df['moyenne_scolaire_sur_20'],color="blue" ,alpha=0.6, s=50)
plt.title('Rapport entre les heures d\'utilisation du smartphone et la moyenne scolaire')
plt.xlabel('Heures d\'utilisation du smartphone par jour')
plt.ylabel('Moyenne scolaire sur 20')
plt.xticks(np.arange(1, 9, 1))
plt.yticks(np.arange(8, 21, 1))
plt.grid(True, linestyle='--', alpha=0.4)

x = df['temps_ecran_par_jour_heures']
y = df['moyenne_scolaire_sur_20']
a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, linestyle='--', color='red')





# Relation entre les heures d'utilisation du smartphone par jour et la moyenne scolaire sur 20
plt.subplot(2,2,3)
plt.scatter(df['heures_sommeil_par_nuit'],df['moyenne_scolaire_sur_20'],color="blue" ,alpha=0.6, s=50)
plt.title('Rapport entre les heures de sommeil et la réussite scolaire')
plt.xlabel('Heures de sommeil par nuit')
plt.ylabel('Moyenne scolaire sur 20')
plt.xticks(np.arange(1, 10, 1))
plt.yticks(np.arange(8, 21, 1))
plt.grid(True, linestyle='--', alpha=0.4)

x = df['heures_sommeil_par_nuit']
y = df['moyenne_scolaire_sur_20']
a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, linestyle='--', color='red')



# Relation entre les heures d'utilisation du smartphone par jour et la moyenne scolaire sur 20
plt.subplot(2,2,4)
df[df["niveau_stress"] == 1]["moyenne_scolaire_sur_20"].mean()
df[df["niveau_stress"] == 2]["moyenne_scolaire_sur_20"].mean()
df[df["niveau_stress"] == 3]["moyenne_scolaire_sur_20"].mean()
df[df["niveau_stress"] == 4]["moyenne_scolaire_sur_20"].mean()
df[df["niveau_stress"] == 5]["moyenne_scolaire_sur_20"].mean()

plt.scatter(df['niveau_stress'],df['moyenne_scolaire_sur_20'],color="blue" ,alpha=0.6, s=50)
plt.title('Rapport entre le niveau de stress et la réussite scolaire')
plt.xlabel('Niveau de stress')
plt.ylabel('Moyenne scolaire sur 20')
plt.xticks(np.arange(1, 6, 1))
plt.yticks(np.arange(8, 21, 1))
plt.grid(True, linestyle='--', alpha=0.4)

x = df['niveau_stress']
y = df['moyenne_scolaire_sur_20']
a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, linestyle='--', color='red')





plt.tight_layout()


plt.show()
