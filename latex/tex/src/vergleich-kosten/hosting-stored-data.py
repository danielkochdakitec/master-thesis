import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 80, 1000)

plt.plot(x, ((0.023 * x) - (5 * 0.023)).clip(min=0.0), '-', label='Amplify Hosting', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, ((0.026 * x) - (10 * 0.026)).clip(min=0.0), '-', label='Firebase Hosting', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Gespeicherte Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/hosting-stored-data.pdf')
plt.show()