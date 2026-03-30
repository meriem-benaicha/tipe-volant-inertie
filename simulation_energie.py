import numpy as np
import matplotlib.pyplot as plt

# Données physiques ajustées
J = 574.7  # moment d'inertie (kg·m²) pour Ec_max = 38.6 MJ
omega_max = 3500 * 2 * np.pi / 60  # vitesse angulaire max en rad/s

# Paramètres du cycle
tau_recharge = 20   # durée du freinage (s)
tau_decharge = 10   # durée du démarrage (s)
dt = 0.1
t_cycle = tau_recharge + tau_decharge
n_cycles = 3
t_total = t_cycle * n_cycles

# Simulation
time = np.arange(0, t_total, dt)
omega = np.zeros_like(time)

for i, t in enumerate(time):
    cycle_pos = t % t_cycle
    if cycle_pos < tau_recharge:
        omega[i] = omega_max * (1 - np.exp(-cycle_pos / tau_recharge))
    else:
        omega[i] = omega_max * np.exp(-(cycle_pos - tau_recharge) / tau_decharge)

E_c = 0.5 * J * omega**2

plt.figure(figsize=(10, 5))
plt.plot(time, E_c / 1e6)
plt.title("Énergie cinétique du volant (ajusté à 38,6 MJ max)")
plt.xlabel("Temps (s)")
plt.ylabel("Énergie cinétique (MJ)")
plt.grid(True)
plt.tight_layout()
plt.show()
