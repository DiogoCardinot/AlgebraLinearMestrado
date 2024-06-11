import numpy as np

#QUESTÃO 1
print("----------------- QUESTAO 1 -----------------------")
#a)
A=np.array([[-1,6],[0,5]])
autovalorA,autovetorA = np.linalg.eig(A)

print("Autovalores A:\n", autovalorA)
print("Autovetores A:\n", autovetorA)

#b)
B=np.array([[-2,7],[4,8]])
autovalorB,autovetorB = np.linalg.eig(B)

print("Autovalores B:\n", autovalorB)
print("Autovetores B:\n", autovetorB)


#QUESTAO 2
print("----------------- QUESTAO 2 -----------------------")

A2 = np.array([[7,0,5],[0,5,0],[-4,0,-2]])
autovalorA2, autovetorA2 = np.linalg.eig(A2)
print("Autovalores A\n", autovalorA2)
print("Autovetores A\n", autovetorA2)


B2 = np.array([[7,4,-16],[2,5,-8],[2,2,-5]])
autovalorB2, autovetorB2 = np.linalg.eig(B2)
print("Autovalores B\n", autovalorB2)
print("Autovetores B\n", autovetorB2)


#QUESTAO 3
print("----------------- QUESTAO 3 -----------------------")
A3 = np.array([[1,1],[1,-1]])
autovalorA3, autovetorA3 = np.linalg.eig(A3)
print("Autovalor A\n", autovalorA3)
print("Autovetor A\n", autovetorA3)


B3 = np.array([[-1,0],[0,-1]])
autovalorB3, autovetorB3 = np.linalg.eig(B3)
print("Autovalor B\n", autovalorB3)
print("Autovetor B\n", autovetorB3)



C3 = np.array([[0,2],[1,0]])
autovalorC3, autovetorC3 = np.linalg.eig(C3)
print("Autovalor C\n", autovalorC3)
print("Autovetor C\n", autovetorC3)