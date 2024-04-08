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
The only operation that costs more than O(1) is the Union operation, which requires us to adapt multiple root pointers. Consider an item x. Its root pointer is adapted whenever its list is appended to a list holding y that contains at least as many items as the list of x.

As the list of x is initially size 1, it is at least size 2 after the first adaptation of the root pointer of x, size 4 after the second and eventually size 2k after the $k_{th}$ adaptation. Thus, as there are only n elements, the root pointer of x can be adapted at most log n times (as after log2 n adaptations, the list has a size of n or more). Hence, the total cost of all the Union operations is at most n log n.
# Disjoint-sets forest
Instead of storing each disjoint set as a linked-list, one can also store them as a tree, creating a disjoint-set forest. In this case, the representative will be the root of the tree and each item x holds a pointer p(x) to its parent in the tree, where the representative has x = p(x).

The advantage is that we can now perform a Union operation by simply making the root of one tree a child of the root of the other tree. However, a FindSet(x) operation requires us to follow the p(x) pointers until we reach the root item that carries the set identifier. Notice, each item does not carry the set identifier, as all these values would require an update when performing a Union operation.

To achieve a good overall performance, **two heuristics** are used to improve the performance of a disjoint-set forest. First, all items keep track of their rank, which is initially 0 and may increase due to a Union operation. The variable rank(x) will hold the length of the longest path from x to one of its descendants in the tree (or an upper bound in case it is combined with path compression). Whenever we link two trees, the tree whose root item has the lowest rank is appended to the one with the larger rank. This heuristic is called **the union by rank heuristic**.

Second, while traversing the path from an item x to the root, we could afterward also adapt all the pointers p(x) on this path such that they directly point to the root item. Hence, any future FindSet operation on one of these items will be performed more efficiently. We will refer to this improvement by **path compression**.
## Pseudocode
```
MakeSet(x):
	p(x) = x; 
	rank(x)=0;
```

```
FindSet(x):
	if p(x) != x:
		then p(x) = FindSet(p(x))
	return p(x)
```

```
Link(x, y):
	if rank(x) > rank(y)
		then p(y) = x
		else p(x) = y
	if rank(x) = rank(y)
		then rank(y) = rank(y) + 1

Union(x, y):
	Link(FindSet(x), FindSet(y))
```

FindSet uses a two-pass method as we first track down the root element by following the p(x) pointers, while upon return we set all the p(x) pointers equal to the root element.
## Theorem 2.1
The worst-case overall cost of a sequence of m operations, including exactly n MakeSet operations, is $O(m \log n)$ using a disjoint-set forest and the union by rank heuristic.
### Proof
The only operation that costs more than O(1) is the FindSet operation where we need to traverse multiple p(x) pointers to find the root (and the FindSet calls needed by the Union calls).

Consider an item x, whose rank is initially equal to 0. In order for x to increase its rank from k to k + 1, a link between two rank k trees is required. 

Thus, by induction, if x gets rank k it is the root of a tree with at least $2^k$ items. As there are n items in total, $2^{rank(x)} \le n$ or $rank(x) \le \log n$.

Moreover, by induction, we easily see that the length of the longest path from the root x to a descendant equals rank(x) (as there is no path compression). Meaning, any FindSet operation takes at most log n time. Resulting in a total cost of $O(m \log n)$. $\square$

Let us now analyze the performance when the **path compression** is combined with union by rank. First, we observe the following properties:
1.  
## Theorem 2.2
The worst-case overall cost of a sequence of m operations, including exactly n MakeSet operations, is $O(m \log_* n)$ using a disjoint-set forest, the union by rank and the path compression heuristic. 
### Proof