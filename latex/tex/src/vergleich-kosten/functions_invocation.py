import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 10, 10)

plt.plot(x, ((0.2 * x) - (1 * 0.2)).clip(min=0.0), '-', label='AWS Lambda', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, ((0.4 * x) - (2 * 0.4)).clip(min=0.0), '-', label='Google Cloud Functions', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Funktionsaufrufe (Anzahl in Millionen)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_2_vergleich-cloud-kosten/functions-invocation.pdf')
plt.show()