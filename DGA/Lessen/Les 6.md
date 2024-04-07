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
Clearly, this is a flow f as the input and output rate of the vertices in $L_M$ and $R_M$ equals one, while all other vertices in $L \cup R$ receive no flow. Moreover, |f| = |M|.

Assume on the other hand that f is an integer valued flow, meaning $f(u, v) \in \mathbb{N}$ for all (u, v) in E. All vertices u in L have only one incoming edge, being (s, u) with capacity 1, and all vertices v in R have only one outgoing edge, being (v, t) with capacity 1. Therefore, all vertices in $\bar{V}$ either have a net input flow of 1 or 0 and thus all edges have f(u, v) = 0 or 1. 

Define $M \subseteq E$ as M = $\{(u,v) | f(u,v) = 1 , u \in L, v \in R\}$. Let $(u, v)$ and $(u', v')$ be in M, then $u = u'$ implies that u has an outgoing flow of at least two, which contradicts our earlier statement. Similarly, $v = v'$ would imply that v has an incoming flow of 2, thus M is a matching. We also immediately see that |M| = |f|.

Due to the Ford and Fulkerson algorithm we know that an integer valued maximum flow of G = (V, E) exist and hence, determines a maximum matching M. $\square$ 

Recall, the number of augmenting paths for an integer valued flow network that can be generated via the Ford and Fulkerson method was bounded by $|f^*|$ where $f^*$ is a maximum flow. Clearly the size of the maximum matching $|M^*| \le |L| \le |V|$, meaning O(|V|) iterations suffice. To find an augmenting path, we can use the Edmonds-Karp algorithm, which determines the shortest augmenting path via a breath-first search in O(|E|) time.

The overall performance of matching a bipartite graph via a flow network therefore equals O(|V||E|).
# Disjoint-sets operations and the linked-list representation
Some functions we define beforehand before diving in to the chapter. These functions are needed for future algorithms like Kruskal's algorithm. 
1. MakeSet(x): This operation creates a set holding exactly one item x.
2. FindSet(x): Searches the set in which item x is located.
3. Union(x, y): takes two sets as input, being the set holding x and y respectively, and creates a single set by taking all items of both sets as its contents.
