
# Optimization problem

- *"An optimization problem is a problem that seeks to find the best solution from a set of possible solutions."*

- *"The notion of an optimization problem provides a structured way to think about solving lots of computational problems"*

- *"Whenever you set about solving a problem that involves finding the biggest, the smallest, the most, the fewest, the fastest, the least expensive, etc., there is a good chance that you can map the problem onto a classic optimization problem for which there is a known computational solution."*

- An optimization problem has two parts:
  - An `objective function` (or cost function) that is to be maximized or minimized
  - An optional set of constraints

## Greedy 

* => Note from GPT*

A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. In other words, at each step, a greedy algorithm chooses the best available option without considering the consequences of that choice on future steps.

Greedy algorithms are simple and often efficient, but they do not guarantee an optimal solution for all problems. They can find approximate solutions for certain problems and work well when the problem exhibits the greedy-choice property. The greedy-choice property means that a locally optimal choice leads to a globally optimal solution.

Here's a general outline of how a greedy algorithm works:

1. Initialization: Initialize an empty or partial solution.
2. Selection: Select the best available option based on a specific criterion (e.g., maximum value, minimum cost).
3. Feasibility: Check if the selected option is feasible within the problem constraints.
4. Acceptance: Include the selected option in the solution.
5. Termination: Repeat steps 2 to 4 until the solution is complete.

One classic example of a problem that can be solved using a greedy algorithm is the "Coin Change" problem, where the goal is to make change for a given amount using the fewest number of coins. The greedy approach in this case would involve repeatedly selecting the largest coin that is not larger than the remaining amount until the amount becomes zero.
Here are some other examples:

- Dijkstra's algorithm is a greedy algorithm that is used to find the shortest path between two nodes in a graph.
- Prim's algorithm is a greedy algorithm that is used to find the minimum spanning tree of a graph.
- The greedy algorithm for the `knapsack probleme` is a greedy algorithm that is used to find the subset of items that has the maximum value and that fits into a knapsack with a limited capacity.

It's important to note that not all problems can be solved optimally using a greedy algorithm. Sometimes, a problem requires more sophisticated approaches like dynamic programming or backtracking to find the optimal solution.

Greedy algorithms are widely used in various applications, including optimization problems, scheduling, and some graph algorithms. However, it's crucial to carefully analyze the problem and verify that the greedy approach indeed leads to an optimal or acceptable solution before applying it.

## 0/1 Knapsack

The 0/1 knapsack problem can be formalized as follows:

- Each item is represented by a pair, `<value, weight>`.
- The knapsack can accommodate items with a total weight of no more than w.
- A vector, $I$, of length $n$, represents the set of available items. Each element of $I$ is an item.
- A vector, $V$, of length $n$, is used to indicate whether each item is selected. $V[i] = 1$ if item $I[i]$ is selected, $0$ otherwise.

- Find a V that maximizes: $$\sum_{i=0}^{n-1} V[i]*I[i].value $$

- Subject to the constraint that: $$\sum_{i=0}^{n-1} V[i]*I[i].weight \le w $$
