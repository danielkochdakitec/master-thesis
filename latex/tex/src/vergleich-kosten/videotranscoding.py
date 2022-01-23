import matplotlib.pyplot as plt
import numpy as np

plt.style.use(['science','ieee'])

overlapping = 0.8
xLength = 600
#yLength = 8

x = np.linspace(0, xLength, 1000)

# Amplify
# 0.017 pro Minute
mediaConvert = 0.017 * x

plt.plot(x, mediaConvert, '-', label='AWS Elemental Media Convert', color='#FF9900', alpha=overlapping, lw=1)

# Firebase
# 0.030 pro Minute
transcoderApi = 0.030 * x

plt.plot(x, transcoderApi, '-', label='Google Transcoder API', color='#4285F4', alpha=overlapping, lw=1)

plt.xlim([0, xLength])
#plt.xlim([0, yLength])

plt.xlabel('Konvertierte Videozeit (min)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()
plt.savefig('../../bilder/7_1_vergleich-cloud-kosten/transcoding.pdf')
plt.show()