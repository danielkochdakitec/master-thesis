import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

overlapping = 0.8
xLength = 80
#yLength = 1.2

x = np.linspace(0, xLength, 1000)

# Amplify
# 0.023 pro GB und ersten 5 GB kostenfrei
amplifyHosting = ((0.023 * x) - (5 * 0.023)).clip(min=0.0)

plt.plot(x, amplifyHosting, '-', label='Amplify Hosting', color='#FF9900', alpha=overlapping, lw=1)

# Firebase
# 0.026 pro GB und ersten 10 GB kostenfrei
firebaseHosting = ((0.026 * x) - (10 * 0.026)).clip(min=0.0)

plt.plot(x, firebaseHosting, '-', label='Firebase Hosting', color='#4285F4', alpha=overlapping, lw=1)

plt.xlim([0, xLength])
#plt.ylim([0, yLength])

plt.xlabel('Gespeicherte Daten (GB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/hosting-stored-data.pdf')
plt.show()