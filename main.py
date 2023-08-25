
#%%
import numpy as np
import matplotlib.pyplot as plt
import random 

#%%
M = 1000
vmax = 5
N = 100
p = 1/3

# %%
X = np.array(sorted(random.sample(range(0, M-1), N)), dtype=np.int64)
V = np.zeros(100, dtype=np.int64)
dX = np.zeros(X.size, dtype=np.int64)

# %%
def update(X, V):
    for i in range(N): 
        d=0
        if i == N-1:
            d = M - X[i] + X[0]
        else:
            d = X[i+1] - X[i]

        V[i] = min(V[i]+1, vmax)
        V[i] = min(V[i], d-1)
        if (random.random() < p):
            V[i] = max(0, V[i]-1) 

    X = X + V 
    for i in range(N):
        if X[i] >= M:
            X[i] = X[i] - M 
            
    while (X[-1] < X[0]):
        X = np.concatenate((X[[-1]], X[0:-1]))
    return X, V
# %%
T = 2000
Xt = np.zeros((T,N), dtype=np.int64)
Vt = np.zeros((T,N), dtype=np.int64)
for t in range(T):
    X, V =update(X, V)
    Xt[t, :] = X
    Vt[t, :] = V
Xt
# %%
Ft = np.zeros((T, M), dtype=np.int64)
for t in range(T):
    Ft[t, Xt[t, :]] = 1

plt.imshow(Ft, cmap="Greys")
# %%
