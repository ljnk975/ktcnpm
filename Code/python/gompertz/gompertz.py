# -*- coding: utf-8 -*-
"""
@author: ljnk975
"""

# In[1]
import numpy as np

## Tham so dau vao [narbaev2014]
alpha = 1.202
gamma = 2.773
beta  = 1.212

# Ham gompertz
#from scipy.stats import gompertz


def gompertz(alpha, gamma, T, t):
    return alpha*np.exp(-np.exp(gamma*(1-t/T)))

def gompertz_dis(alpha, gamma, T, t):
    return alpha*gamma*np.exp(gamma*(1-t/T))*gompertz(alpha, gamma, T, t)


## Sinh du lieu
## p = planned, e = earned, a = actual
t_x   = range(1, 30)
#g_p   = alpha*gompertz.pdf([beta-gamma*t/15 for t in t_x], 1)
g_p   = [gompertz_dis(alpha, gamma, 10, t) for t in t_x]
g_e   = [gp+np.random.normal(loc=0.0, scale=alpha/10) for gp in g_p]
g_a   = [gp+np.random.normal(loc=0.0, scale=alpha/10) for gp in g_p]

# In[2]
import matplotlib.pyplot as plt

# plot gompertz
plt.plot(t_x, g_p, 'b-', t_x, g_e, 'r-', t_x, g_a, 'g-');
plt.title('Gompertz')
plt.xlabel('Weeks')
plt.ylabel('Planned, Earned & Cost Rate')
plt.autoscale(tight='both')
plt.show()

# In[3]
# Two point and regression
def calcTe(alpha, gamma, Tp, t):
    return Tp-1/gamma*np.log(-np.log(g_e[t]/alpha))

_2point = [calcTe(alpha, gamma, 30, t) for t in t_x]

