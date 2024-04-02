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
2. Next, we push the maximum possible flow from s to its neighbors, causing these vertices to overflow. The algorithm repeatedly selects an overflowing vertex. 