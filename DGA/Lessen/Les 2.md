# DFS
The **depth-first search (DFS)** strategy differs from the BFS, in the sense that DFS tries to search **deeper** into the graph before exploring the **breadth**. As with the BFS algorithm, vertices are initially undiscovered and thus colored White (except for the source node s in BFS). 

Furthermore, each vertex u is also linked to its parent upon discovery, where the parent node π(u) is the node from which u is discovered. 

An important distinction with the BFS is that the DFS will produce a set of trees as its output (instead of a single BFS tree holding the shortest paths from the source s to all the vertices reachable from s).
```python
enum:
	WHITE = Not visited
	GRAY = Discoverd
	BLACK = All neigbours have been discovered

def DFS(G: graph):
	for u in V:
		color(u) = WHITE
		pi(u) = NULL
	
	time = 0
	
	for u in V:
		if color(u) == WHITE:
			DFS_visit(u)

def DFS_visit(u: vertex):
	color(u) = GRAY
	time += 1
	d(u) = time # discovery time
	
	for v in Γ(u):
		if color(v) = WHITE:
			pi(v) = u
			DFS_visit(v)
	
	color(u) = BLACK
	time += 1
	f(u) = time # finish time
```
Runtime:
- Init: O(|V|)
- DFS with not the secondary function: O(|V|)
- Because the secondary function is only called when a vertex is WHITE, we can say it will run at most O(|Γ(u)|), this is because the secondary function itself runs the same check. This causes it to finish faster than expected.
## Theorem 3.1 Parenthesis theorem
Given a graph G = (V, E) and u, v in V, then either of the two following cases holds after running DFS:
1. The intervals \[d(u), f(u)] and \[d(v), f(v)] do not overlap, and v is not a descendant of u.
2. The interval \[d(u), f(u)] completely engulfs interval \[d(v), f(v)], then v is a descendant of u in the DFS tree/forest (vice versa in case the roles are switched between u and v).
So, v is only a descendant if and only if $d(u) \lt d(v) \lt f(v) \lt f(u)$.
### Proof
Without loss of generality assume $d(u) \lt d(v)$.

1. If $f(u) \lt f(v)$ then we can clearly see that both intervals are disjoint, because $d(v) \lt f(v)$. This leads us then to that v is not a descendant of u, because u is marked GRAY when the descendants are found (finish time of u is greater than of v). 
2. If $d(v) \lt f(u)$ then we know that v is discovered before u finishes, and so with the recursive nature of DFS v will finish first before u finishes and v is a descendant of u.
## Theorem 3.2 White path theorem
Given that we perform a DFS search on G = (V, E) with u, v in V, v will be a descendant of u in the DFS tree if and only if at time d(u) there exists a White path from u to v in G.
### Proof
$\Rightarrow$) Assume v is a descendant of u in the DFS tree and w is a vertex in the path going from u to v. So using the parenthesis theorem we know that the discovery time of w is less than u's discovery time, so by the time u is discovered w is still WHITE.

$\Leftarrow$) Assume we have a white path from u to v at time d(u), but v is not a descendant of u. Further, we can select v such that w, the vertex just prior to v on this path, is a descendant of u in the DFS tree. Now, due to Parenthesis theorem, we have $f(w) \lt f(u)$ and v is WHITE at the time u is discovered, we have $d(u) \lt d(v)$.

Now, either v is discovered before w explores the edge (w, v) or it is discovered at the time we visit the edge (w, v), then we have $d(v) \le f(w) \lt f(u)$. 

Looking at both inequalities, we can make use of the parenthesis theorem to see that v is a descendant of u.
## Theorem 3.3 
A DFS search of an undirected graph G = (V, E) only encounters tree and back edges.
### Proof
Let (u, v) be an arbitrary edge in E. 

Suppose that v is Black when exploring the edge (u, v) from u. This implies that v has been discovered and all its outgoing edges have been explored. Thus, as (u, v) in E, so is the edge (v, u) and this edge must have been explored. 

At this time u was either White or Gray (as it is still Gray) and hence the edge is either a tree or back edge.
## Theorem 3.4
A directed graph G contains no cycles if a DFS traversal of the graph does not encounter a back edge.
### Proof
Clearly, if the DFS tree contains a back edge, then G contains a cycle. 

The reverse statement can be proven as follows. Assume C is a cycle with vertices $u_1, . . . , u_k$ in G and without loss of generality, let $u_1$ be the first vertex on G that is discovered by the DFS search. Then, by the white path theorem, the entire cycle is part of the DFS tree of $u_1$, including $u_k$. 

When we visit $u_k$, we will explore the edge $(u_k, u_1)$ and this edge is a back edge as $u_1$ was already discovered at that time (but not finished as $u_k$ is a descendant of $u_1$).
## Extra terminology p13
1. Tree edges are those edges (u, v) in E that are also part of the depth-first forest described by $E_π$. 
2. Back edges (u, v) in E connect a vertex u with one of its ancestors in the DFS tree/forest (i.e., u is a descendant of v). 
3. Forward edges (u, v) in E are those connecting a vertex u with one of its descendants v in the DFS tree. 
4. Finally, cross edges are all the remaining edges. These can be edges in a single DFS tree or edges between different trees in the DFS forest.