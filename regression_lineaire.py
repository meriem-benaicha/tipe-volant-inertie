import numpy as np
import matplotlib.pyplot as plt

# Données expérimentales extraites du tableau
temps = np.array([0.0, 3.3, 6.6, 9.9, 13.2, 16.5, 19.8, 23.1, 26.4, 29.7])
omega = np.array([1.26e+02, 1.19e+02, 1.10e+02, 1.03e+02, 9.61e+01,
                  9.05e+01, 8.48e+01, 8.04e+01, 7.60e+01, 7.23e+01])

# Calcul du logarithme népérien de la vitesse angulaire
ln_omega = np.log(omega)

# Régression linéaire : ln(omega) = a * t + b
coeffs = np.polyfit(temps, ln_omega, 1)
fit_line = np.poly1d(coeffs)

# Affichage graphique
plt.figure(figsize=(8, 5))
plt.scatter(temps, ln_omega, color='orange', label="Données expérimentales", marker='x')
plt.plot(temps, fit_line(temps), color='red',
         label=f"Régression linéaire\ny = {coeffs[1]:.2f} + {coeffs[0]:.3f} t")
plt.title("Régression de ln(ω) en fonction du temps")
plt.xlabel("Temps (s)")
plt.ylabel("ln(ω) (rad/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
