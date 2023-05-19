"""
Dados do Problema:
m -> quantidade de agentes;
n -> quantidade de tarefas;
a[5,50] -> contém a quantidade de recursos necessários ao agente i para processar a tarefa j;
b[5,1] -> vetor onde a posição b(i) contém a capacidade total do agente i;
c[5,50] -> matriz onde a posição c(i, j) contém o custo de atribuição da tarefa j ao agente i;
"""

import numpy as np
import random

def geraSolucaoInicial(m, n, a, b, c):
    x = np.zeros((m, n))  # Matriz de atribuições inicialmente vazia
    disponibilidade = np.copy(b)  # Vetor de capacidade disponível dos agentes
    
    indices_tarefas = list(range(n))  # Lista de índices das tarefas
    random.shuffle(indices_tarefas)  # Embaralhar os índices aleatoriamente
    
    for j in indices_tarefas:
        tarefa_atribuida = False
        menor_custo = float('inf')
        agente_escolhido = -1
        
        for i in np.argsort(disponibilidade):
            if disponibilidade[i] >= a[i, j] and c[i, j] < menor_custo:
                menor_custo = c[i, j]
                agente_escolhido = i
                tarefa_atribuida = True
        
        if tarefa_atribuida:
            x[agente_escolhido, j] = 1  # Atribui a tarefa j ao agente agente_escolhido
            disponibilidade[agente_escolhido] -= a[agente_escolhido, j] + c[agente_escolhido,j]  # Atualiza a capacidade disponível do agente
            
        if not tarefa_atribuida:
            print(f"A tarefa {j} não pode ser atribuída a nenhum agente.")
            # Trate aqui o caso em que uma tarefa não pode ser atribuída a nenhum agente
    
    return x


# Recebe uma tupla de agentes, e uma tupla de tarefas
def trocaTarefas(agentes, tarefas, m, n, a, b, c):
    agente_a, agente_b = agentes
    tarefa_a, tarefa_b = tarefas
    
    # Verificar se a troca é benéfica para o sistema
    custo_atual = np.sum(c * a)  # Custo total atual
    
    # Cálculo do custo total considerando a troca de tarefas
    custo_tarefa_a = c[agente_a, tarefa_b] + a[agente_b, tarefa_a]
    custo_tarefa_b = c[agente_b, tarefa_a] + a[agente_a, tarefa_b]
    novo_custo = custo_atual - (c[agente_a, tarefa_a] + c[agente_b, tarefa_b]) + custo_tarefa_a + custo_tarefa_b
    
    # Verificar se a troca não ultrapassa a capacidade de recursos dos agentes
    recursos_disponiveis_a = np.copy(b)
    recursos_disponiveis_a[agente_a] += a[agente_a, tarefa_a] - a[agente_a, tarefa_b]
    recursos_disponiveis_b = np.copy(b)
    recursos_disponiveis_b[agente_b] += a[agente_b, tarefa_b] - a[agente_b, tarefa_a]
    
    # Verificar se a troca é possível e benéfica
    if novo_custo < custo_atual and np.all(recursos_disponiveis_a >= 0) and np.all(recursos_disponiveis_b >= 0):
        # Efetuar a troca de tarefas
        a[agente_a, tarefa_a] = 0
        a[agente_a, tarefa_b] = 1
        a[agente_b, tarefa_b] = 0
        a[agente_b, tarefa_a] = 1
        
        return 1  # Troca realizada com sucesso
    else:
        return 0  # Troca não realizada


def buscaLocal(m, n, a, b, c, max_iter):
    melhor_solucao = geraSolucaoInicial(m, n, a, b, c)  # Inicializa a melhor solução com uma solução inicial
    melhor_diferenca_recursos = calcularDiferencaRecursos(melhor_solucao, a)  # Calcula a diferença no consumo de recursos da melhor solução

    iteracao = 0
    melhoria = True

    while iteracao < max_iter and melhoria:
        melhoria = False

        for i in range(m):
            for j in range(n):
                if melhor_solucao[i, j] == 1:  # Tarefa atribuída ao agente i
                    for k in range(m):
                        if melhor_solucao[k, j] == 0:  # Tarefa não atribuída ao agente k
                            if trocaTarefas((i, k), (j, j), m, n, a, b, c) == 1:
                                diferenca_recursos_atual = calcularDiferencaRecursos(a, a)  # Diferença no consumo de recursos da solução atualizada

                                if diferenca_recursos_atual < melhor_diferenca_recursos:
                                    melhor_solucao = np.copy(a)
                                    melhor_diferenca_recursos = diferenca_recursos_atual
                                    melhoria = True

                                # Desfaz a troca para explorar outras possibilidades
                                trocaTarefas((i, k), (j, j), m, n, a, b, c)

        iteracao += 1

    return melhor_solucao, melhor_diferenca_recursos


def calcularDiferencaRecursos(solucao, a):
    m, n = a.shape
    custo_agentes = np.zeros(m)

    for i in range(m):
        for j in range(n):
            if solucao[i, j] == 1:  # Tarefa atribuída ao agente i
                custo_agentes[i] += a[i, j]

    menor_consumo = np.min(custo_agentes)
    maior_consumo = np.max(custo_agentes)
    diferenca_recursos = maior_consumo - menor_consumo

    return diferenca_recursos




def main():
    m = 5
    n = 50
    aa = np.genfromtxt('data_5x50_a.csv', delimiter=',')
    bb = np.genfromtxt('data_5x50_b.csv', delimiter=',')
    cc = np.genfromtxt('data_5x50_c.csv', delimiter=',')
    maxIter = 50

    solucaoEncontrada, diferencaRecursosEncontrada = buscaLocal(m, n, aa, bb, cc, maxIter)
    print(f"Solucao: {solucaoEncontrada}")
    print(f"Diferenca no consumo de recursos: {diferencaRecursosEncontrada}")

main()