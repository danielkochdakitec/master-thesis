import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 80, 1000)

plt.plot(x, ((0.0245000000 * x) - (5 * 0.0245000000)).clip(min=0.0), '-', label='Amazon S3', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, ((0.023 * x) - (5 * 0.023)).clip(min=0.0), '-', label='Google Cloud Storage', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Gespeicherte Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_2_vergleich-cloud-kosten/storage-amount.pdf')
plt.show()