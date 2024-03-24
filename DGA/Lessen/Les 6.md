# Preflow-push algorithms
Preflow-push algorithms are different in nature than the Ford and Fulkerson method, as these algorithms do not construct a sequence of flows whose value |f| increases at each iteration.

Instead, a sequence of **preflows** f is constructed. Preflows are like flows in the sense that they also respect the skew symmetry and capacity constraints, but they are allowed to violate the flow conservation property

However, if there is no flow conservation in a vertex, then the amount of flow entering the vertex must dominate the amount of flow leaving it. Formally, a preflow is a function $f: V x V \rightarrow R$ for which
1. 