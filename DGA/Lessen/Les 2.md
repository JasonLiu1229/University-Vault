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
## Theorem 3.1
Given a graph G = (V, E) and u, v in V, then either of the two following cases holds after running DFS:
1. The intervals \[d(u), f(u)] and \[d(v), f(v)] do not overlap, and v is not a descendant of u.
2. The interval \[d(u), f(u)] completely engulfs interval \[d(v), f(v)], then v is a descendant of u in the DFS tree/forest (vice versa in case the roles are switched between u and v).
So 

### Proof
## Theorem 3.2
### Proof
## Theorem 3.3
### Proof
## Theorem 3.4
### Proof