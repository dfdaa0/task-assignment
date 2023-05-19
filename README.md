# Problem Statement
A company has a set T with "n" tasks to be performed and a set A with "m" available agents. Assume that "c[i, j]" is the cost of assigning task "j" ∈ T to agent "i" ∈ A, "a[i, j]" is the amount of resources required by agent "i" ∈ A to perform task "j" ∈ T, and "b[i]" is the total availability of resources for agent "i" ∈ A.  

The variables are as follows:

* m: number of agents = 5;
* n: number of tasks = 50;
* a: matrix where the position a[i, j] contains the amount of resources required by agent i to process task j;
* c: matrix where the position c[i, j] contains the cost of assigning task j to agent i;
* b: vector where the position b[i] contains the total capacity of agent i.

"a", "b", and "c" are matrices/vectors provided in .csv files.

* Propose a variation of Variable Neighborhood Search (VNS) that is suitable for solving the single-objective versions of the problem, i.e., to separately optimize the functions fC() and fE(), considering the defined constraints.
* Explain how a candidate solution will be computationally modeled.
* Propose at least three (03) neighborhood structures.
* Propose an intelligent constructive heuristic to generate the initial solution.
* Consider a refinement strategy (local search).
* Implement and use the proposed algorithm to solve the single-objective versions of the problem.
* Since the method is stochastic, it should be executed five times for each of the functions, and the five final results obtained should be presented: for each optimized function (fC and fE), show the min, std, and max values considering the 05 final solutions found.
* For each optimized function (fC and fE), present the 05 convergence curves of the algorithm overlaid in the same figure, i.e., the evolution of the value of f as a function of the number of evaluations of candidate solutions.
* For each optimized function, present the best solution found, explicitly stating the distribution of tasks among agents.
