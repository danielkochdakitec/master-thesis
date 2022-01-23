import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

overlapping = 0.8
xLength = 100000
#yLength = 1.2

x = np.linspace(0, xLength, 1000)

# Amazon S3
# 0.00000043 pro Request und ersten 20k Requests kostenfrei
amplifyHosting = ((0.00000043 * x) - (20000 * 0.00000043)).clip(min=0.0)

plt.plot(x, amplifyHosting, '-', label='Amazon S3', color='#FF9900', alpha=overlapping, lw=1)

# Google Cloud Storage
# 0.0000004 pro Request und ersten 50k Requests kostenfrei
firebaseHosting = ((0.0000004 * x) - (50000 * 0.0000004)).clip(min=0.0)

plt.plot(x, firebaseHosting, '-', label='Google Cloud Storage', color='#4285F4', alpha=overlapping, lw=1)

plt.xlim([0, xLength])
#plt.ylim([0, yLength])

plt.xlabel('Anzahl an Anfragen', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/storage-get.pdf')
#plt.show()