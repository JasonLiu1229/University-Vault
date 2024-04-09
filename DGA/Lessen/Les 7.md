Start of spanning trees chapter
# Basic properties and definitions
A connected graph is called a **tree** if the removal of its edges makes the graph disconnected. A tree T is called a subtree of some graph G if $T \subseteq G$. A subtree $T \subseteq G$ is said to be a **spanning tree** if it contains all the vertices of G, i.e., $V(T) = V(G)$. We call a graph G weighted if G has a weight function $\alpha : E(G) \rightarrow \mathbb{R}^+$ (positive reals) on its edges, where $\alpha(e)$ denotes the weight of e $e \in E(G)$. For each spanning tree T, we can define its **weight** as the sum of the weights of its edges as $\alpha(T) = \sum_{e\in E(T)} \alpha(e)$

Whenever we wish to build a network connecting n nodes (towns, computers, chips in a computer) it is desirable to decrease the cost of construction of the links to the minimum. In graph theoretical terms, we wish to find an a spanning tree T of a weighted graph G, with α(T) minimal.

Minimum weight spanning trees are useful in a variety of disciplines. For instance, minimum spanning trees are useful in constructing networks, by describing the way to connect a set of sites using the smallest total amount of wire. Much of the work on minimum spanning (and related Steiner) trees has been conducted by the phone company. They also provide a reasonable way for clustering points in space into natural groups. When the cities are points in the Euclidean plane, the minimum spanning tree provides a good heuristic for traveling salesman problems. The optimum traveling salesman tour is at most twice the length of the minimum spanning tree.
## Theorem 1.1
The following statements are equivalent:
1. G is a connected graph, where the removal of any edge of G makes G disconnected. 
2. There exists a unique path between every two vertices of G. 
3. G does not hold any closed paths and for $n \gt 2$ every additional edge creates a closed path in G. 
4. G is connected and contains no closed path. 
5. G does not contain a closed path and e = n - 1. 
6. G is connected and e = n - 1.
## Kruskal’s algorithm (1956)
## Algorithm 2.1
(Kruskal’s algorithm (1956)). For a connected and weighted graph $G^α$ of order n:
1. Order the set of edges E(G) by non-decreasing weight, set i = 1.
2. Set $E(T) = \varnothing$ and for each edge $(u, v) \in E(G)$ in order by non-decreasing weight, check whether $E(T) + (u, v)$ contains a closed path. If there is no closed path, set $E(T) =  E(T) + (u, v)$, $e_i = (u, v)$ and i = i + 1.
The final outcome $T = (V(G)), E(T) = \{e_1, ..., e_{n-1}\})$ is a spanning tree with minimum weight.

Notice, E(T) need not be connected during the execution of the algorithm.
### Complexity
Step 1 orders the edges, which can be done in $O(|E| \log |E|)$ time. For Step 2, we can rely on the disjoint-sets data structure. 