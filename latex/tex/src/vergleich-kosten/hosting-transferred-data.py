import matplotlib.pyplot as plt
import numpy as np

plt.style.use(['science','ieee'])

overlapping = 0.8
xLength = 60
#yLength = 8

x = np.linspace(0, xLength, 1000)

# Amplify
# 0.15 pro GB und ersten 15 GB kostenfrei
amplifyHosting = ((0.15 * x) - (15 * 0.15)).clip(min=0.0)

plt.plot(x, amplifyHosting, '-', label='Amplify Hosting', color='#FF9900', alpha=overlapping, lw=1)

# Firebase
# 0.15 pro GB und ersten 10.8 GB kostenfrei
firebaseHosting = ((0.15 * x) - (10.8 * 0.15)).clip(min=0.0)

plt.plot(x, firebaseHosting, '-', label='Firebase Hosting', color='#4285F4', alpha=overlapping, lw=1)

plt.xlim([0, xLength])
#plt.xlim([0, yLength])

plt.xticks(np.arange(0, 60, 5))

plt.xlabel('Übertragene Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/hosting-transferred-data.pdf')
plt.show()