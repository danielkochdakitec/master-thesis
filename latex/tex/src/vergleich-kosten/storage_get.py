import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 100000, 1000)

plt.plot(x, ((0.00000043 * x) - (20000 * 0.00000043)).clip(min=0.0), '-', label='Amazon S3', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, ((0.0000004 * x) - (50000 * 0.0000004)).clip(min=0.0), '-', label='Google Cloud Storage', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Anzahl an Anfragen', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/storage-get.pdf')
plt.show()