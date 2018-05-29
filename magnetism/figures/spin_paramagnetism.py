from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 12})

def M(x):
    return np.tanh(x)

x = np.linspace(0,5,200)

figsize = (4.5,3.5)
plt.figure(figsize=figsize)
plt.plot(x,M(x),linewidth=2)

plt.xlabel('Field strength $(\mu_B B_0/k_B T)$')
plt.ylabel('Magnetization  $(M V/N \mu_B)$')
plt.xlim([0,5])
plt.ylim([0,1.04])

plt.tight_layout()

plt.figure(figsize=figsize)

y = np.linspace(0.001,5,200)

plt.plot(y,M(1/y),linewidth=2)
plt.xlabel('Temperature $(k_B T/\mu_B B_0)$')
plt.ylabel('Magnetization  $(M V/N \mu_B)$')
plt.xlim([0,5])
plt.ylim([0,1.04])
plt.tight_layout()
plt.show()
