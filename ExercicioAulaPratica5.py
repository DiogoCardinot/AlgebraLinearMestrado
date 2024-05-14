import numpy as np
from plot_helper import *
import matplotlib.pyplot as plt


# QUESTÃO 1 
def ContracaoExpansao(vetor, alpha, Questao):
    baseM = np.array([(alpha,0),(0,alpha)])
    vetores=[vetor, baseM.dot(vetor)]
    plot_vector(vetores)
    plt.title(f"Contração ou expansão de [{str(vetor[0])}, {str(vetor[1])}], alpha= {str(alpha)} \n Questão {Questao}")
    # f'Contração ou expansão de ['+ str(vetor[0])+', "+ str(vetor[1])+"] com $\alpha$= '+ str(alpha)+"\n Questão "+ Questao
    plt.show()

ContracaoExpansao(np.array((1,2)),2, "1- a)")
ContracaoExpansao(np.array((1,2)),-3, "1- b)")


# QUESTAO 2
def ReflexaoEixoX(vetor, Questao):
    baseM = np.array([(1,0),(0,-1)])
    vetores=[vetor, baseM.dot(vetor)]
    plot_vector(vetores)
    plt.title(f"Reflexão em torno do eixo x para [{str(vetor[0])}, {str(vetor[1])}] \n Questão {Questao}")
    plt.show()

ReflexaoEixoX(np.array((-3,-6)), "2")


# QUESTÃO 3
def ReflexaoOrigem(vetor, Questao):
    baseM = np.array([(-1,0),(0,-1)])
    vetores=[vetor, baseM.dot(vetor)]
    plot_vector(vetores)
    plt.title(f"Reflexão em torno da origem para [{str(vetor[0])}, {str(vetor[1])}] \n Questão {Questao}")
    plt.show()

ReflexaoOrigem(np.array((5,3)), "3")


# QUESTÃO 4
def RotacaoAntiHorarioAngulo(vetor, teta, Questao):
    baseM = np.array([(np.cos(teta), - np.sin(teta)), (np.sin(teta), np.cos(teta))])
    vetores = [vetor, baseM.dot(vetor)]
    plot_vector(vetores)
    plt.title(f"Rotação anti horária para o vetor [{str(vetor[0])}, {str(vetor[1])}] \n Questão {Questao}")
    plt.show()

RotacaoAntiHorarioAngulo(np.array((2,3)), np.pi, "4- a)")
RotacaoAntiHorarioAngulo(np.array((-1,-2)), 3*(np.pi)/2, "4- b)")


#QUESTÃO 5
def CisalhamentoHorizontal(vetor, alpha, Questao):
    baseM = np.array([(1, alpha), (0,1)])
    vetores= [vetor, baseM.dot(vetor)]
    plot_vector(vetores)
    plt.title(f"Cisalhamento horizontal para o vetor [{str(vetor[0])}, {str(vetor[1])}] \n Questão {Questao}")
    plt.show()

CisalhamentoHorizontal(np.array((-6,5)), 3, "5")
