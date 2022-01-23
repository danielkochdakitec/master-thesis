import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

overlapping = 0.8
xLength = 80
#yLength = 1.2

x = np.linspace(0, xLength, 1000)

# Amazon S3
# 0.0245000000 pro GB und ersten 5 GB kostenfrei
amplifyHosting = ((0.0245000000 * x) - (5 * 0.0245000000)).clip(min=0.0)

plt.plot(x, amplifyHosting, '-', label='Amazon S3', color='#FF9900', alpha=overlapping, lw=1)

# Google Cloud Storage
# 0.023 pro GB und ersten 5 GB kostenfrei
firebaseHosting = ((0.023 * x) - (5 * 0.023)).clip(min=0.0)

plt.plot(x, firebaseHosting, '-', label='Google Cloud Storage', color='#4285F4', alpha=overlapping, lw=1)

plt.xlim([0, xLength])
#plt.ylim([0, yLength])

plt.xlabel('Gespeicherte Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/storage-amount.pdf')
plt.show()