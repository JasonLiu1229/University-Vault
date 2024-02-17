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
- BFS is 