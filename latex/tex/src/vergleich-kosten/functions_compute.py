import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 100000, 1000)

plt.plot(x, 60 * ((0.0000166667 * x) - (1600000/60 * 0.0000166667)).clip(min=0.0), '-', label='AWS Lambda', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, 60 * ((0.0000035 * x) - (1600000/60 * 0.0000035)).clip(min=0.0), '-', label='Google Cloud Functions', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Ausführungszeit (min)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/functions-compute.pdf')
plt.show()