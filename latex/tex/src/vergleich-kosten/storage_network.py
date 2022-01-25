import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science')

#AWS:
#- 10240 GB x 0.09 USD per GB  (first 10TB)
#- 40960 GB x 0.085 USD per GB = 3481.60 USD (next 40TB)
#- 102400 GB x 0.07 USD per GB = 7168.00 USD (next 100TB)
#- 999846400 GB x 0.05 USD per GB = 49992320.00 USD (larger than 150TB)

#Google:
#- 0-1 TB $0.12
#- 1-10 TB	$0.11
#- 10+ TB $0.08

#- 30 GB transfer free

x = [0, 0.03, 1, 10, 50, 150, 200]

plt.plot(x, [0, 2.7, 90, 900, 4300, 11300, 13800], '-', label='Amazon S3', color='#FF9900', alpha=0.8, lw=1)
plt.plot(x, [0, 0, 116.4, 1106.4, 4306.4, 12306.4, 16306.4], '-', label='Google Cloud Storage', color='#4285F4', alpha=0.8, lw=1)

plt.xlabel('Übertragene Daten (TB)', color='#1C2833')
plt.ylabel('Kosten (US-Dollar)', color='#1C2833')

plt.legend(loc='upper left')
plt.tight_layout()
plt.grid()
plt.savefig('../../bilder/7_2_vergleich-cloud-kosten/storage-network.pdf')
plt.show()