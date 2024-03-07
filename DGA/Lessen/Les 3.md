# Topological sort
Directed acyclic graphs can be sorted topologically using the DFS algorithm.
We state that G is topologically sorted if for all (u, v) in E, vertex u must appear before vertex v. Clearly, when a graph G contains cycles, this sort is impossible.

To perform a topological sort, we simply run the DFS algorithm on G and each time a vertex is finished, we add it as the first element of a linked list. Initially, the list is empty, as more and more vertices are finished, the list grows until it has size |V| and all vertices are finished. The following property shows that this approach sorts G topologically.
## Theorem 4.1
A directed acyclic graph G can be sorted topologically by calling the DFS algorithm and adding the vertices in the order they are finished to the front of a linked list.
### Proof
Suppose we run the DFS algorithm on G and f(u) is the finishing time of a vertex u in V. 

Thus, if f(v) $\lt$ f(u), u appears before v in the linked list. Assume that (u, v) in E, we need to show that f(v) $\lt$ f(u).

At some point, we explore this edge from u (which is Gray). At this time v cannot be Gray as this would mean that (u, v) is a back edge (contradicting Theorem 3.4). 
1. If v is White, it is a descendant of u with d(u) $\lt$ d(v), implying f(v) $\lt$ f(u) as required (due to the parenthesis Theorem).
2. If v is Black then f(v) $\lt$ f(u) as u is still Gray.
# Strongly Connected Components
The vertices V of a graph G = (V, E) can always be partitioned into k subsets $C_1, . . . , C_k$ (for some k $\ge$ 1) such that two vertices (u, v) in V belong to the same subset if and only if there is a path from u to v and from v to u in G.
These k subsets are called the strongly connected components (SCCs) of the graph G. Notice, if u and v belong to the same component C, any node on a path from u to v (or from v to u) also belongs to C.

The following algorithm, that relies on two DFS searches, computes the SCCs of a directed graph G.
1. Perform a DFS on G and denote the finishing time of a node u as f(u).
2. Construct the graph G' = (V, E'), where (u, v) in E' if and only if (v, u) in E.
3. Perform a DFS search on G', where the nodes of G' in the main for-loop of the DFS algorithm are ordered in decreasing value of f(u).
Each tree produced by the second DFS will correspond to an SCC.
## Theorem 5.1
The algorithm above correctly computes the SCCs of a graph G.
### Proof
We start by defining $f(C) = max_{u \in C} f(u)$ and $d(C) = min_{u \in C} d(u)$ as the finishing time and discovery time of an SCC C during the first DFS, respectively. 

We first show that if (u, v) in E, u in C and v in C', where C and C' are two different SCCs, then f(C) $\gt$ f(C).

We distinguish two cases:
1. Assume d(C) $\lt$ d(C') and let x be the first node of C that is discovered. Thus, at time d(x) all the nodes in C and C' are still White. Further, as (u, v) in E, all the nodes in C and C' are reachable from x, thus, due to the white path theorem, all the nodes in C $C¬ are descendants of x.