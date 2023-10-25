
## Unsupervised learning
 - ML approaches that involves finding hidden structure in unlabeled data.
 - Example: **Clustering** 
    - *The process of organizing objects into groups whose members are similar in some way.* J. V. Guttag

### Clustering
 - *"Clustering is an optimization problem. The goal is to find a set of clusters that optimizes an objective function, subject to some set of constraints. Given adistance metric that can be used to decide how close two examples are to each other, we need to define an objective function that minimizes the distance between examples in the same cluster, i.e., minimizes the dissimilarity of the examples within a cluster."* J. V. Guttag

 - **Variability**: 
   - For a given cluster $c$, ($c \in C$, where $C$ is a set of clusters)
   - $variability(c) = \sum_{e \in c} distance(x_c, e)^2$
        - where $x_{c}$: is the center of the cluster $c$ (i.e., the mean of the feature vectors of all the examples in the cluster)
    - $dissimilarity(C) = \sum_{c \in C} variability(c)$
        - NB: A large incoherent cluster increases the value of $dissimilarity(C)$ more than a small incoherent cluster does (raison:  $variability(c)$ is not normalized by the size of $c$)

- Optimization problem: Minimizing $dissimilarity(C)$ with some constraints
    - Example of constrains
        - minimum distance between clusters
        - set the maximum number of clusters to be $k$
        - etc, ...
    - NB: Without constraint, we cah get the minimum of $dissimilarity(C)$ by considering each data point as a cluster
