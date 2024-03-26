import numpy as np

# EXERCÍCIO 1
print("Exercicio 1: \n")

A = np.array([[1,2,2],[-2,0,4],[0,3,1]])
B = np.array([[2,3,4],[0,1,1],[-1,-2,4]])
C = np.array([[0,5,-4],[3,5,1],[0,2,2]])

# A+B 
D = np.add(A,B)
print("A+B= \n", D)

# B-A
E= np.subtract(B,A)
print("B-A= \n", E)

# Ct 
F = np.transpose(C)
print("C_transposta: \n", F)

#AB
G = np.dot(A,B)
print("AB: \n", G)

#BA 
H = np.dot(B,A)
print("BA: \n", H)

# 3C
I = 3*C
print("3C: \n", I)

#C3(cada elemento ao cubo)
J = C**3
print("aij^3: \n", J)

Identidade = np.eye(3)

#CI
K= np.dot(C,Identidade)
print("C*Identidade: \n", K)

#C**4
L = np.linalg.matrix_power(C,4)
print("C^4: \n", L)

# EXERCÍCIO 2
print("\nExercicio 2: ")
A1 = np.array([[1,-2],[3,0]])
B1= np.array([[2,1],[-1,4]])

# 2A
M=2*A1

# Bt 
N= np.transpose(B1)

# print(M,"\n\n",N)
C1 = M+N
print("2A + Bt: \n", C1)

# EXERCÍCIO 3
A2 = np.array([[1,-2,3,4]])
B2 = np.array([[8],[3],[-5],[2]])

#AB
O = np.dot(A2,B2)
print("\nExercicio 3: ")
print("AB: \n", O)
