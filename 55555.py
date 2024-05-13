#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

def apokrish(b, a, omega):
    H = np.polyval(b, np.exp(1j * omega)) / np.polyval(a, np.exp(1j * omega))
    return H

b1 = [0.7]
a1 = [1, -0.3]

b2 = [0, 2, -1, 1]
a2 = [1]

omega = np.linspace(0, 2*np.pi, 1000)

c1 = apokrish(b1, a1, omega)
c2 = apokrish(b2, a2, omega)

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(c1))
plt.title('αποκριση συχνοτητας (a)')
plt.xlabel('συχνοτητα (radians/sample)')
plt.ylabel('πλατος')

plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(c1))
plt.title('αποκριση (a)')
plt.xlabel('συχνοτητα (radians/sample)')
plt.ylabel('φαση (radians)')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(c2))
plt.title('αποκριση συχνοτητας (b)')
plt.xlabel('συχνοτητα (radians/sample)')
plt.ylabel('πλατος')

plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(c2))
plt.title('αποκριση φασης (b)')
plt.xlabel('συχνοτητα (radians/sample)')
plt.ylabel('φαση (radians)')

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




