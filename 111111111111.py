#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[10]:


import numpy as np
import matplotlib.pyplot as plt

n1 = np.arange(-10, 11)
x1 = np.zeros_like(n1)
x1[n1 == 2] = 2

n2 = np.arange(-10, 11)
x2 = np.sqrt(np.pi) * (np.where(n2 == -10, 1, 0) - 3 * np.where(n2 == 7, 1, 0))

n3 = np.arange(-10, 11)
x3 = np.where(n3 >= 2, 1, 0)

n4 = np.arange(-10, 11)
x4= np.where((n4 >= 0) & (n4 <= 10), 1, 0)

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.stem(n1, x1)
plt.title('x(n) = 2δ(n-2)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

plt.subplot(222)
plt.stem(n2, x2)
plt.title('x(n) = √π * (δ(n+10) - 3δ(n-7))')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

plt.subplot(223)
plt.stem(n3, x3)
plt.title('x(n) = u(-n+2)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

plt.subplot(224)
plt.stem(n4, x4)
plt.title('x(n) = u(n) - u(n-10)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




