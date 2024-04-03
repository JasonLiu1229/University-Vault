New chapter, starting from bipartite matching algorithms
# The graph matching problem 
## Basic definitions
Let G = (V, E) be an undirected graph and $M \subseteq E$ be a subset of the edges of G.

We call M a **matching** of G if all edges e in M are vertex disjoint. The vertices incident to M are referred to as matched vertices, whereas the remaining vertices are termed unmatched. A matching M is said to be maximum if for all other matching M' we have $|M| \ge |M'|$. 
# A network flow solution
We will construct a simple flow network with source s and sink t such that a maximum flow in this network corresponds to a maximum matching and vice versa.

Let $\bar{G} = (\bar{V}, \bar{E})$ be a bipartite graph where $\bar{V}$ is partitioned into a set L and R (being the left and right vertices of $\bar{G}$ such that (u, v) in $\bar{E}$ implies that u in L and v in R). Define G = (V, E) as $V = \bar{V} \cup \{s, t\}, E = \bar{E} \cup \{(s, y) | y \in L \} \cup \{(v,t) | v \in R\}$, where each undirected edge (u, v) in $\bar{E}$ contributes one directed edge to E being (u, v) with u in L and v in R. The capacity function c(u, v) = 1 for all (u, v) in E.
## Theorem 2.1
Let $\bar{G} = (\bar{V}, \bar{E})$ an undirected bipartite graph and G = (V, E) its corresponding flow network. A maximum matching in $\bar{G}$ corresponds to a maximum flow f in G with |f| = |M| and vice versa.
### Proof
Assume $M \subseteq \bar{E}$ is a matching of $\bar{G}$ and let $L_M$ and $R_M$ be the set of matched vertices in L and R respectively. Define the flow f as $\begin{equation} f(u, v)=\begin{cases}1 & u = s, v \in L_M, \\1 & (u, v) \in M, \\1 & u \in R_M, v = t,\\ 0 & otherwise. \end{cases}\end{equation}$ 
Clearly, this is a flow f as the input and output rate of the vertices in $L_M$ and $R_M$ equals one, while all 