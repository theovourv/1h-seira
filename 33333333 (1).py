#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

b = [0.3, 0.6, 0.3]
a = [0, 0, -0.9]

x = np.zeros(101)
x[0] = 1
c = np.convolve(x, b)
c = np.append(h, [0, 0])  
c= np.convolve(h, a)

plt.figure(figsize=(10, 5))
plt.stem(c)
plt.title('αποκριση')
plt.xlabel('n')
plt.ylabel('c(n)')
plt.grid(True)
plt.show()


from scipy.signal import lti, impulse
import matplotlib.pyplot as plt

b = [0.3, 0.6, 0.3]
a = [1, 0, -0.9]

system = lti(b, a)

t, c = impulse(system)

plt.figure(figsize=(10, 5))
plt.stem(t, c)
plt.title('αποκριση')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()



# In[ ]:




