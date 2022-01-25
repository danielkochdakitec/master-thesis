import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

x = np.linspace(0, 600, 1000)

plt.plot(x, 0.017 * x, '-', label='AWS Elemental Media Convert', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, 0.030 * x, '-', label='Google Transcoder API', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Konvertierte Videozeit (min)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_2_vergleich-cloud-kosten/transcoding.pdf')
plt.show()