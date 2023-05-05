# Teoria da Decisão (ELE088) - UFMG
## Enunciado
Uma empresa possui um conjunto T com "n" tarefas a serem realizadas e um conjunto A com "m" agentes disponíveis. Assuma que "c[i, j]" é o custo de atribuir a tarefa "j" ∈ T ao agente "i" ∈ A, "a[i, j]" é a quantidade de recursos necessários ao agente "i" ∈ A para realizar a tarefa "j" ∈ T , e "b[i]" é a disponibilidade total de recursos do agente "i" ∈ A.  

As variáveis são as seguintes: 

* m: número de agentes = 5;
* n: número de tarefas = 50;
* a: matriz onde a posição a[i, j] contém a quantidade de recursos necessários ao agente i para processar a tarefa j;
* c: matriz onde a posição c[i, j] contém o custo de atribuição da tarefa j ao agente i;
* b: vetor onde a posição b[i] contém a capacidade total do agente i.

"a", "b" e "c" são matrizes/vetores oferecidas em arquivos .csv.

## Algoritmo de solução
* Proponha uma variação da VNS (variable neighborhood search) que seja adequada para resolver as versões mono-objetivo do problema, ou seja, para otimizar separadamente as funções fC() e fE(), considerando as restrições definidas.
* Explicite como uma solução candidata será modelada computacionalmente.
* Proponha pelo menos três (03) estruturas de vizinhança.
* Proponha uma heurística construtiva inteligente para gerar a solução inicial.
* Considere alguma estratégia de refinamento (busca local).

## Resultados da otimização mono-objetivo (Utilizando Python)
* Implemente e utilize o algoritmo proposto para resolver as versões mono-objetivo do problema. 
* Como o método é estocástico, ele deve ser executado cinco vezes para cada uma das funçoes e os cinco resultados finais obtidos devem ser apresentados: para cada função otimizada (fC e fE), mostre os valores min, std e max considerando-se as 05 soluções finais encontradas.
* Para cada funçao otimizada (fC e fE), apresente as 05 curvas de convergência do algoritmo sobrepostas em uma mesma figura, ou seja, evolução do valor de f em função do número de avaliações de soluçoes candidatas.
* Para cada função otimizada, apresente a melhor solução encontrada explicitando a distribuição das tarefas aos agentes.
