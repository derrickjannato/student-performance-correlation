import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/moncsv.csv")

def scatter_avec_tendance(ax, x_col, y_col, xlabel, title, xticks_range):
    x = df[x_col]
    y = df[y_col]
    
    ax.scatter(x, y, color="blue", alpha=0.6, s=50)
    
    a, b = np.polyfit(x, y, 1)
    ax.plot(x, a * x + b, linestyle='--', color='red')
    
    corr = np.corrcoef(x, y)[0, 1]
    ax.set_title(f"{title}\n(r = {corr:.2f})")
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Moyenne scolaire sur 20')
    ax.set_xticks(xticks_range)
    ax.set_yticks(np.arange(8, 21, 1))
    ax.grid(True, linestyle='--', alpha=0.4)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

configs = [
    (axes[0, 0], 'heures_revision_par_jour', 'Heures de révision/jour',
     'Révision vs Réussite scolaire', np.arange(1, 7, 1)),
    (axes[0, 1], 'temps_ecran_par_jour_heures', "Heures d'écran/jour",
     "Temps d'écran vs Réussite scolaire", np.arange(1, 9, 1)),
    (axes[1, 0], 'heures_sommeil_par_nuit', 'Heures de sommeil/nuit',
     'Sommeil vs Réussite scolaire', np.arange(1, 10, 1)),
    (axes[1, 1], 'niveau_stress', 'Niveau de stress',
     'Stress vs Réussite scolaire', np.arange(1, 6, 1)),
]

for ax, x_col, xlabel, title, xticks in configs:
    scatter_avec_tendance(ax, x_col, 'moyenne_scolaire_sur_20', xlabel, title, xticks)

plt.tight_layout()
plt.savefig('resultats_correlation.png', dpi=150)
plt.show()