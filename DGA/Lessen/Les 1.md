# BFS (breadth first search)
The idea is to select a specific vertex s, called the source, as the starting point of the search. Next, we discover each of the neighbors of s, say s1 to sk. Subsequently, the undiscovered neighbors of s1 are discovered, followed by those of s2 and so on. Each time we discover a vertex v we will draw an edge between v and u if u was the vertex from which we (first) discovered v. The vertex u will be termed the parent π(v) of v.
```python
# init
for each vertex u in (V - {s}) 
	color(u) = White; d(u) = inf; π(u) = Nil 

color(s) = Gray; d(s) = 0; π(s) = Nil 
Q = {s} 

# BFS 
while Q is not empty:
	u = Head(Q) 
	for each v in Γ(u) 
		if color(v) = White 
			color(v) = Gray; d(v) = d(u) + 1; π(v) = u 
			Enqueue(Q, v) 
	Dequeue(Q)
	color(u) = Black
```
Runtime: 
- Init is O(|V|)
- BFS is O(|E|) because we need to look at every edge
- So O(|V| + |E|)

## Theorem 2.1 
Given G = (V, E) a graph with s in V the source vertex, the BFS algorithm returns a tree containing all vertices reachable from s and d(u) = δ(s, u) upon termination, where δ(s, u) gives the length of the shortest simple path from s to u in G (that is, the number of edges needed to get from s to u).
### Proof
To prove this theorem we start by arguing that the following three statements hold:
1. If du  k, vertex u is at level k of the BFS tree and δs, u & k  du. 
2. If Q  v1v2 . . . vr during the algorithm, we have dv1 & dv2 & . . . & dvr & dv1  1. 
3. If v is dequeued before u, we have dv & du