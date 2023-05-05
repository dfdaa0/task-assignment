import numpy as np
import matplotlib.pyplot as plt
import csv


m = 5 # não é necessário importar o valor em csv, já que é unitário
n = 50

# Atribuição dos valores dos arquivos csv para as respectivas variáveis
with open('data_5x50_a.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    a = [row for row in csv_reader]

with open('data_5x50_b.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    b = [row for row in csv_reader]

with open('data_5x50_c.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    c = [row for row in csv_reader]

class Struct():
    pass

"""
a[5,50] -> contém a quantidade de recursos necessários ao agente i para processar a tarefa j;
b[5,1] -> vetor onde a posição b(i) contém a capacidade total do agente i;
c[5,50] -> matriz onde a posição c(i, j) contém o custo de atribuição da tarefa j ao agente i;
"""


def solucaoInicial(custo, recursosNecessarios, capacidadeAgente):
  # Utilizando a heurística e alocação de menor custo por recurso
  # inicializa a lista de alocações
  alocacoes = [] 
  for j in range(len(recursosNecessarios[0])): 
    
    # lista de agentes que conseguem fazer a tarefa
    agentesPossiveis = [] 
    
    for i in range(len(recursosNecessarios)):

      # se a capacidade do agente for maior que o gasto
      if all(recursosNecessarios[i][j] <= capacidadeAgente[i]):  

          # o agente entra na lista de agentes disponíveis
          agentesPossiveis.append(i)     

    # ordena a lista de agentes pelo custo de atribuição da tarefa j
    agentesPossiveis.sort(key=lambda i: custo[i][j]) 

    # atribui a tarefa j ao agente com menor custo de atribuição
    alocacoes.append((j, agentesPossiveis[0])) 
    
    for k in range(len(recursosNecessarios[agentesPossiveis[0]])):

      # retira os recursos que o agente utilizou para execução da tarefa
      capacidadeAgente[agentesPossiveis[0]][k] -= recursosNecessarios[agentesPossiveis[0]][k] 

  return alocacoes

