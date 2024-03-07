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
1. Assume d(C) $\lt$ d(C') and let x be the first node of C that is discovered. Thus, at time d(x) all the nodes in C and C' are still White. Further, as (u, v) in E, all the nodes in C and C' are reachable from x, thus, due to the white path theorem, all the nodes in C $\cup$ C' are descendants of x. This implies that f(x) = f(C) $\gt$ f(C').
2. Assume now d(C') $\lt$ d(C) and by the white path theorem f(x) = f(C'), where x is the first node of C' that is discovered. Further, as (u, v) in E, none of the vertices in C are reachable from x as this would imply that all the nodes in C and C' belong to the same SCC. Hence, f(C) $\gt$ f(C') as required. This implies that if (u, v) in E', with u and v belonging to two different SCCs C and C', then f(C) $\lt$ f(C').

Now, assume by induction that the first m trees produced by the second DFS search correspond to the first m SCCs $C_1$ to $C_m$ such that $f(C_1) \gt . . . \gt f(C_m)$.

Denote x as the root node of the next tree produced by the second DFS, and denote C as its SCC. Clearly, all the nodes in C will be part of the tree rooted by x (as they do not belong to $C_1$ $\cup . . . \cup$ $C_m$ by induction). Further, as the vertices of G' in the main for-loop of the second DFS algorithm are ordered in decreasing value of f(u), we have f(x) = f(C). 

Next, suppose there exists an edge (u, v) in E', with u in C and v not in $C_1$ $\cup . . . \cup$ $C_m$ $\cup$ C, but part of SCC C'. Let y in C' be the vertex with f(y) = f(C'). Then, f(x) = f(C) $\lt$ f(C') =  f(y) as shown earlier, but this is impossible as f(x) $\gt$ f(y) (as the nodes in the main for-loop of the second DFS were ordered in decreasing value of f(u)).

As a result, tree m+1 will consist of the nodes of C only and therefore corresponds to the m+1-st SCC
# Flow networks
## Definition 1.1
A flow network G = (V, E) is a directed graph in which each edge (u, v) in E has a capacity c(u, v) $\ge$ 0. Let s, t be two specific vertices in V called the **source** and **sink** of the network. If (u, v) not in E, we define c(u, v) = 0.

To simplify our discussion, we assume that for each v in V, there exists a path from s via v to t. Nodes in V for which there is no such path have no use, as they cannot carry any flow from s to t.
## Definition 2.1
A flow f in a flow network G, is a real-valued function f from V x V to R satisfying:
1. *Capacity constraint*: f(u, v) $\le$ c(u, v) for all u, v in V.
2. *Skew symmetry*: f(u, v) = -f(v, u) for all u, v in V.
3. *Flow conservation*: $\sum_{v \in V}$ f(u, v) = 0 for all u in V - {s, t}.

The value of f(u, v) is the net flow from u to v and the value of f, denoted as |f|, equals $\sum_{v \in V}$ f(s, v), where s is the source vertex.
## Lemma 1.1
Let $f_1$ and f2 be two flows in G with f1u, vf2u, v & cu, v for all u, v " V , then f defined as f u, v  f1u, vf2u, v for all u, v " V , defines a flow in G with ¶f ¶  ¶f1¶  ¶f2¶.