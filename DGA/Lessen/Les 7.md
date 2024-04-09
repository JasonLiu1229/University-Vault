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
# Kruskal’s algorithm (1956)
## Algorithm 2.1
(Kruskal’s algorithm (1956)). For a connected and weighted graph $G^α$ of order n:
1. Order the set of edges E(G) by non-decreasing weight, set i = 1.
2. Set $E(T) = \varnothing$ and for each edge $(u, v) \in E(G)$ in order by non-decreasing weight, check whether $E(T) + (u, v)$ contains a closed path. If there is no closed path, set $E(T) =  E(T) + (u, v)$, $e_i = (u, v)$ and i = i + 1.
The final outcome $T = (V(G)), E(T) = \{e_1, ..., e_{n-1}\})$ is a spanning tree with minimum weight.

Notice, E(T) need not be connected during the execution of the algorithm.
### Complexity
Step 1 orders the edges, which can be done in $O(|E| \log |E|)$ time. 

For Step 2, we can rely on the disjoint-sets data structure.  Indeed, initially we perform n = |V(G)| MakeSet operations, one for each node $v \in V(G)$. This creates n trees, each having 1 vertex. Next, each time we need to determine whether there is a closed path by adding an edge (u, v) to E(T), we test whether FindSet(u) = FindSet(v). If not, we perform a Union(u, v) to merge the component of u with the component of v. If u and v did belong to the same set, this implies that there already existed a path from u to v; hence, adding (u, v) creates a closed path.

Thus, using a disjoint-sets forest structure, we can implement Step 2 in time $O|E| \log_* |V|)$ as we perform at most |V| MakeSet operations, 2|E| FindSet operations and |V| - 1 Union operations.
## Theorem 2.1
Kruskal’s algorithm when applied on a connected weighted graph $G^α$ returns a minimum spanning tree T.
### Proof
We first argue that T = (V(G), E(T)) is a spanning tree of G. By construction it contains no cycles. Further, T must be connected, otherwise T has components $C_1$ and $C_2$. Any edge (u, v) with $u \in C_1$ and $v \in C_2$, should have been added to T as it does not create a closed path (such an edge exists as G is connected). 

Next, we show that T has the minimum total weight among all spanning trees of G. Suppose $T_1$ is a spanning tree of G. Let $e_k$ be the first edge produced by the algorithm that is not in $T_1$, meaning $\{e_1, . . . , e_{k-1}\} \in E(T_1)$. If we add $e_k$ to $T_1$, then a cycle C containing $e_k$ is created. Also, C must contain an edge e that is not in T (as T is a tree and therefore has no cycles). Replace e by $e_k$ in $T_1$, to obtain a new spanning tree $T_2 = T_1 + e_k - e$ (as $T_2$ is still connected and has $|E(T_2)| = |V(T_2)| - 1$).

However, by construction, $α(e_k) \le α(e)$, because $\{e_1, . . . , e_{k-1}, e\} \subseteq E(T_1)$ does not contain a cycle. Therefore, $α(T_2) \le α(T_1)$. Note that $T_2$ has more edges in common with T than $T_1$. Repeating the above procedure, we can transform $T_1$ to T by replacing edges, one by one, such that the total weight does not increase. We deduce that $α(T) \le α(T_1)$. 

So we have a minimum spanning tree T. $\square$
# Prim’s algorithm (1957)
## Algorithm 3.1
For a connected and weighted graph $G^α$ of order n with V(G) = $\{v_1, . . . , v_n\}$.
1. Define $f(v_1) = 0$ and $f(v_i) = α((v_1, v_i)$ if $(v_1, v_i) \in E(G)$ and $f(v_i) = \infty$ otherwise (for $i \gt 1$). Let $E(T) =  \varnothing$ and set $U = \{v_1\}$.
2. Choose $w \in V(G) - U$ with f(w) minimal. Replace E(T) by $E(T) \cup \{e\}$, where e is an edge incident to w and U for which α(e) = f(w) and set $U = U \cup \{w\}$. If U = V(G) stop.
3. For each $v \not\in U$ for which $wv \in E(G): f(v)  \min \{f(v), \alpha(w, v)\}$. Return to Step 2.
The final outcome T = (V(G), E(T)) is a spanning tree with minimum weight.

Notice, f(v) equals the minimal weight of any edge connecting v with U (f(v) equals if there is no such edge). Thus, at each iteration, we simply add a new edge e to T with a weight α(e) as small as possible.

A straightforward implementation of Prim’s algorithm has a runtime complexity of $O(|V|^2)$. Making use of a binary heap can improve this complexity to $O(|E| \log |V|)$ (making use of Fibonacci heaps it can be improved to $O(|E| + |V| \log |V|)$). Thus, Prim’s algorithm is faster on dense graphs, while Kruskal’s is faster on sparse graphs.
## Theorem 3.1
Prim’s algorithm when applied on a connected weighted graph $G^α$ returns a minimum spanning tree T.
### Proof
Let $G^α$ be a connected, weighted graph. By induction, we can show that T = (U, E(T)) is a spanning tree on the vertices of U during each iteration.

Indeed, at step 1 we have |U| = 1, |E(T)|0, hence, it is a spanning tree on U = $\{v_1\}$.

At every other iteration, we augment |U| and |E(T)| by one, meaning |U| = |E(T)| + 1 and T is connected. As a result, T is a spanning tree.

Let $T_1$ be a spanning tree for G. Let e = (u, v) be the first edge not belonging to $T_1$ that was added when T = (U, E(T)) was constructed. Then, by construction, one endpoint u of e = (u, v) was in U and the other v was not. Since $T_1$ is a spanning tree of G, there is a path in $T_1$ joining the two endpoints u and v of e. As one travels along this path, one must encounter an edge $f = (u', v')$ joining a vertex $u' \in U$ to $v' \not\in U$ (note, it could be that $v' = v$ or $u' = u$, but not both). Now, at the iteration when e = (u, v) was added to E(T), $f = (u', v')$ could also have been added, and it would be added instead of e = (u, v) if $α(f) \lt  α(e)$. Let $T_2 = T_1 + e - f$, then $α(T_2) \le α(T_1)$ and $T_2$ is a spanning tree as $T_2$ is connected and the number of vertices still matches the number of edges plus one.

Repeating the above procedure, we can transform $T_1$ to T by replacing edges, one by one, such that the total weight does not increase. We deduce that $α(T) \le α(T_1)$. $\square$