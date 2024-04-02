# Preflow-push algorithms
Preflow-push algorithms are different in nature than the Ford and Fulkerson method, as these algorithms do not construct a sequence of flows whose value |f| increases at each iteration.

Instead, a sequence of **preflows** f is constructed. Preflows are like flows in the sense that they also respect the skew symmetry and capacity constraints, but they are allowed to violate the flow conservation property

However, if there is no flow conservation in a vertex, then the amount of flow entering the vertex must dominate the amount of flow leaving it. Formally, a preflow is a function $f: V x V \rightarrow R$ for which
1. Capacity constraint: $f(u, v) \le c(u, v) \text{ for all } u, v \in V$.
2. Skew symmetry: $f(u,v) = -f(v,u) \text{ for all } u, v \in V$.
3. Excess property: $e(u) = \sum_{v\in V} f(v,u) \ge  \text{ for all } u \in V - \{s\}$.

If e(u) $\gt$ 0, we state that the vertex u $\ne$ t is **overflowing**. 

Intuitively, the preflow-push method works as follows. 
1. We start by giving vertex s a height h(s) of |V| and all other vertices v a height h(v) of 0.
2. Next, we push the maximum possible flow from s to its neighbors, causing these vertices to overflow. The algorithm repeatedly selects an overflowing vertex. This vertex u will either have a neighbor v (in the residual network) with a height h(v) = h(u) + 1 such that some of the excess flow in u can flow down to v (possibly overflowing v). Notice, if there is an edge in the residual network, then there still remains some capacity from u to v. If an excess vertex does not have such a neighbor, we lift the vertex (by increasing its height h(u)) creating such a neighbor.
Thus, the idea is that the initial flow in the neighbors of s will gradually flow downward through the network, while all the vertices (except the sink t and source s) gain height. At some point, this causes a maximum amount of flow |f| to reach the sink t. However, the initial flow pushed by s may be considerably larger. What happens next is that the vertices u $\ne$ s, t continue to gain height, such that the redundant flow returns to the source s. When all excess capacity has been removed, the preflow becomes a flow with the required maximum capacity |f|. 

A preflow-push algorithm will allow two operations (on overflowing vertices): a push and a lift. The applicability of these operations is regulated by the height of a vertex. A height function h : V $\rightarrow$ R must fulfill the following requirements:
1. h(s) = |V| and h(t) = 0,
2. If (u, v) $\in$ $E_f$: $h(v) \ge h(u) - 1$
Thus, the height may decrease by at most one when following an edge in the residual network $G_f = (V, E_f)$, where $E_f$ with f a preflow is defined in exactly the same manner as for a flow f, i.e., $(u, v) \in E_f \text{ if } c_f(u, v) = c(u, v) - f(u, v) \gt 0$.