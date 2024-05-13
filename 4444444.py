#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
from scipy.signal import lfilter, convolve
import matplotlib.pyplot as plt
from scipy.signal import freqz
a = [1, 0, -0.1, 0, -0.06]
b = [0.2, 0.5, 0.4]
x = np.zeros(16)
x[0] = 1

h = lfilter(b, a, x)
print(h)

x_extended_b = np.append(x, np.zeros(len(b) - 1))
x_extended_a = np.append(np.zeros(len(a) - 1), x)
y_conv = convolve(x_extended_b, b, mode='valid') - convolve(x_extended_a, a, mode='valid')
print(y_conv)

y_conv_valid = convolve(x_extended_b, b, mode='valid') - convolve(x_extended_a, a, mode='valid')
print(y_conv_valid)

w, h_freq = freqz(b, a)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(h_freq)), 'b')
plt.ylabel('enysxish (dB)')
plt.title('apokrish')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h_freq), 'b')
plt.ylabel('fash (rad)')
plt.xlabel('syxnothta (Hz)')
plt.grid()
plt.show()




# In[ ]:




