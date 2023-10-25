# Dynamic programming

- Invented by Richard Bellman in the 1950s
- *"Dynamic programming is a method for efficiently solving problems that exhibit the characteristics of overlapping subproblems and optimal substructure."*

  - *"A problem has **optimal substructure** if a globally optimal solution can be found by combining optimal solutions to local subproblems. We’ve already looked at a number of such problems. Merge sort, for example, exploits the fact that a list can be sorted by first sorting sublists and then merging the solutions."*

  - *"A problem has **overlapping subproblems** if an optimal solution involves solving the same problem multiple times. Merge sort does not exhibit this property. Even though we are performing a merge many times, we are merging different lists each time."*

*From GPT*

- Dynamic programming is a method used in computer science and mathematics to solve problems by breaking them down into overlapping subproblems and solving each subproblem only once, storing the results in a table or memoization array to avoid redundant computations. This technique is particularly useful when a problem can be divided into smaller subproblems, and the solution to the overall problem depends on the optimal solutions to the subproblems.

- The key idea behind dynamic programming is to store the solutions of the subproblems in memory so that they can be reused when needed. This way, the time complexity of the algorithm is significantly reduced compared to naive recursive approaches that might recompute the same subproblems multiple times.

- Dynamic programming is commonly used to solve optimization problems and is frequently applied in problems involving finding the maximum or minimum value, counting the number of ways to do something, or determining the optimal sequence of choices to reach a certain goal.

- There are two main approaches in dynamic programming:

  1. Top-Down (Memoization): This approach involves breaking the problem into smaller subproblems and solving them recursively while storing the results of each subproblem in a memoization table to avoid redundant computations.

  2. Bottom-Up (Tabulation): In this approach, the problem is solved by iteratively building solutions for all subproblems, starting from the smallest subproblem and moving towards the main problem. The results are stored in a table, and each solution depends only on previously computed solutions.

- Dynamic programming can be applied to various problems such as the Fibonacci sequence, shortest path problems (e.g., Dijkstra's algorithm), knapsack problems, and many more.

- The key to using dynamic programming effectively is recognizing the overlapping subproblems and the optimal substructure property of the problem at hand. By applying dynamic programming techniques, you can often obtain significant speed improvements and efficient solutions to complex problems.
  
  - Optimal Substructure:
  Optimal substructure is a property where the optimal solution to the main problem can be constructed from the optimal solutions of its subproblems. In other words, if we know the optimal solutions to all the subproblems, we can efficiently find the optimal solution to the main problem.
  In problems with optimal substructure, breaking the main problem into smaller subproblems and solving them independently often leads to the overall optimal solution. The main problem's solution can be expressed as a combination of the solutions to its subproblems.

    - Example: Shortest Path Problem
    The shortest path problem, such as finding the shortest path from a source node to a target node in a graph, exhibits optimal substructure. If we know the shortest path from the source node to a specific intermediate node and the shortest path from that intermediate node to the target node, we can combine them to find the shortest path from the source node to the target node.

  - Overlapping Subproblems:
  Overlapping subproblems is a property where the same subproblems are solved multiple times in the process of solving the main problem. Dynamic programming optimizes solutions by storing the results of these subproblems and reusing them whenever needed.
  In problems with overlapping subproblems, there are redundant computations of the same subproblems, leading to inefficiencies if solved independently. By using techniques like memoization or tabulation, dynamic programming avoids re-computation and optimizes the overall algorithm.

    - Example: Fibonacci Numbers
   The Fibonacci sequence is a classic example of a problem with overlapping subproblems. Calculating the nth Fibonacci number using a naive recursive approach results in a lot of redundant computations for the same Fibonacci numbers. By using dynamic programming and memoization, the Fibonacci numbers can be computed efficiently by storing the results of previously calculated Fibonacci numbers in a table.

- To detect if a problem has optimal substructure and overlapping subproblems, consider the following:

  1. Optimal Substructure:
     - Analyze whether the problem can be divided into smaller subproblems that can be solved independently.
     - Determine if the main problem's optimal solution depends on the optimal solutions of its subproblems.
     - If solving the subproblems independently leads to the overall optimal solution, the problem likely has optimal substructure.

  2. Overlapping Subproblems:
     - Identify if the same subproblems are solved multiple times during the recursive process or iterative approach.
     - Determine if there is redundancy in the computations of these subproblems.
     - If the same subproblems are encountered multiple times, the problem likely has overlapping subproblems.

- In summary, problems with optimal substructure and overlapping subproblems are good candidates for dynamic programming optimization. Dynamic programming techniques can be applied to efficiently solve these problems by avoiding redundant computations and reusing solutions of subproblems.
