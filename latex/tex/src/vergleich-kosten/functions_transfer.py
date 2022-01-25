import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 60, 100)

plt.plot(x, 0.09 * x, '-', label='AWS Lambda', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, ((0.12 * x) - (5 * 0.12)).clip(min=0.0), '-', label='Google Cloud Functions', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Übertragene Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_2_vergleich-cloud-kosten/functions-transfer.pdf')
plt.show()