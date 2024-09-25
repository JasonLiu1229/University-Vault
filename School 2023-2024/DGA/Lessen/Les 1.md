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
1. If d(u) = k, vertex u is at level k of the BFS tree and δ(s, u) $\le$ k = d(u). 
2. If Q = v1, v2, . . ., vr during the algorithm, we have d(v1) $\le$ d(v2) $\le$ . . . $\le$ d(vr) $\le$ d(v1) + 1. 
3. If v is dequeued before u, we have d(v) $\le$ d(u)

1. Trivial
2. The second holds by noting that Q = s at the start and whenever we add a vertex v to Q when u is at the head of the queue, we have d(v) $\le$ d(u) + 1. 
3. The last one follows up on the second statement.

The proof completes as follows. Assume the theorem does not hold and let v be a vertex for which d(v) $\gt$ δ(s, v) with δ(s, v) as small as possible. Note by statement 1, it is impossible to have d(v) < δ(s, v). Let u be the last vertex on a shortest path from s to v. As δ(s, v) was chosen as small as possible, we have d(u) = δ(s, u) =  δ(s, v) - 1.

When u is dequeued, there are two options. Either v was dequeued earlier, and we have d(v) $\le$ d(u) (by statement 3). This yields d(v) $\le$ δ(s, u) $\le$ δ(s, v). Otherwise, as (u, v) in E, the vertex v must be in the queue when u is dequeued. 

Hence, by statement 2 we have d(v) $\le$ d(u) + 1 = δ(s, v). Thus, in both cases we have d(v) $\le$ δ(s, v) which contradicts the assumption that the theorem does not hold. $\square$