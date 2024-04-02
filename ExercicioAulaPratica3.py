import numpy as np

# SISTEMA A 
matrizAa = np.array([[2,-1,-2],[3,2,2],[5,4,3]])
matrizBa = np.array([10,1,4])
matrizAaAmpliada = np.array([[2,-1,-2,10],[3,2,2,1],[5,4,3,4]])

# SISTEMA B 
matrizAb = np.array([[1,2,-1],[2,-1,3],[4,3,1]])
matrizBb = np.array([0,0,0])
matrizAbAmpliada =np.array([[1,2,-1,0],[2,-1,3,0],[4,3,1,0]])

# SISTEMA C 
matrizAc = np.array([[1,-1,2,-1],[2,1,-2,-2],[-1,2,-4,1],[3,0,0,-3]])
matrizBc = np.array([-1,-2,1,-3])
matrizAcAmpliada = np.array([[1,-1,2,-1,-1],[2,1,-2,-2,-2],[-1,2,-4,1,1],[3,0,0,-3,-3]])

# SISTEMA D 
matrizAd = np.array([[1,1,1],[2,5,-2],[1,7,-7]])
matrizBd  = np.array([4,3,5])
matrizAdAmpliada = np.array([[1,1,1,4],[2,5,-2,3],[1,7,-7,5]])

# SISTEMA E 
matrizAe = np.array([[1,-2,3],[2,5,6]])
matrizBe  = np.array([0,0])
matrizAeAmpliada = np.array([[1,-2,3,0],[2,5,6,0]])

# SISTEMA F 
matrizAf = np.array([[1,1,1,1],[1,1,1,-1],[1,1,-1,1],[1,-1,1,1]])
matrizBf  = np.array([0,4,-4,2])
matrizAfAmpliada = np.array([[1,1,1,1,0],[1,1,1,-1,4],[1,1,-1,1,-4],[1,-1,1,1,2]])

def CalculaPosto(matrizA, matrizB ,matrizAAmpliada):
    postoA = np.linalg.matrix_rank(matrizA)
    postoAAmpliada = np.linalg.matrix_rank(matrizAAmpliada)
    n= matrizA.shape[1]
    print("Numero de variaveis: ", n)
    if(postoA != postoAAmpliada):
        print("Sistema sem solucao")
    else:
        if(postoA < n):
            print("Sistema possui varias solucoes")
        if(postoA == n):
            print("Sistema com apenas uma solucao.")
            solucao = np.linalg.solve(matrizA, matrizB)
            if(n==2):
                print("Solucao: \n", "x=", solucao[0], ", y=", solucao[1])
            if(n==3):
                print("Solucao: \n", "x=", solucao[0], ", y=", solucao[1], ", z=", solucao[2])
            if(n==4):
                print("Solucao: \n", "x=", solucao[0], ", y=", solucao[1], ", z=", solucao[2], ", t=",solucao[3])



print("Sistema letra a:")
CalculaPosto(matrizAa, matrizBa, matrizAaAmpliada)
print("\nSistema letra b:")
CalculaPosto(matrizAb, matrizBb, matrizAbAmpliada)
print("\nSistema letra c:")
CalculaPosto(matrizAc, matrizBc, matrizAcAmpliada)
print("\nSistema letra d:")
CalculaPosto(matrizAd, matrizBd, matrizAdAmpliada)
print("\nSistema letra e:")
CalculaPosto(matrizAe, matrizBe, matrizAeAmpliada)
print("\nSistema letra f:")
CalculaPosto(matrizAf, matrizBf, matrizAfAmpliada)
