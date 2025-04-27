import numpy as np

A = np.array([[2,2,3],[1,2,1],[2,-2,1]])
autovalores, autovetores= np.linalg.eig(A)
print("Autovalores: \n", autovalores)
print("Autovetores: \n", autovetores)