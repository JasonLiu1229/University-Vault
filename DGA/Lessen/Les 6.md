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
Each set is also said to have a representative (typically called the root item). A MakeSet(x) operation automatically makes x the representative, while a Union operation typically selects one of the two representatives to become the new representative. The FindSet does not alter the representative.

A first implementation of the disjoint-sets data structure is to maintain a linked-list per set $S_i$: this list links all items by placing a pointer from item i to i - 1, where item 0 is the representative. Further, all items also carry a pointer to the representative. This pointer, called the root pointer, allows us to perform the FindSet operation in time O(1) as the root item (representative) carries the identifier of the set. The Union operation is somewhat more involving as we need to append one linked list, say holding x, to the back of the other list, holding y, (which can be done in O(1) time by keeping a pointer to the last element) and to update the root pointers of all the entries in the list of x.

In order to reduce the amount of updates required by the Union operation, it is best to append the shorter list to the longer one. This leads to the following theorem:
## Theorem 1.1
The worst-case overall cost of a sequence of m operations, including exactly n MakeSet operations, is $O(m + n\log n)$ using a linked list representation.
### Proof
The only operation that costs more than O(1) is the Union operation which requires us to adapt multiple root pointers. Consider an item x. Its root pointer is adapted whenever its list is appended to a list holding y that contains at least as many items as the list of x.

As the list of x is initially size 1, it is at least size 2 after the first adaptation of the root pointer of x, size 4 after the second and eventually size 2k after the $k_{th}$ adaptation. Thus, as there are only n elements, the root pointer of x can be adapted at most log n times (as after log2 n adaptations, the list has a size of n or more). Hence, the total cost of all the Union operations is at most n log n.
# Disjoint-sets forest
