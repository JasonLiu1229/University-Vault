## Prim's algorithm and binary heaps
A binary heap is a **complete** binary tree, where each vertex v in the tree has a **key value** k(v) such that the value of any parent vertex is smaller than or equal to the key value of both its children. Thus, the root of the tree holds the element with smallest key value. 

Four important heap operations:
1.  The first operation concerns the **Heapify(A, i)** operation. It is invoked when both the children of i are the root of a binary heap, but the key value k(i) of vertex i is larger than that of one of its children. **Heapify(A, i)** will exchange vertex i with the smallest child and will repeat this operation recursively until both children have a key value larger than or equal to k(i), the key value of vertex i at the start of the operation. Given that A has size n, the time complexity equals the depth of the tree, i.e., it is $O(\log n)$.
2. The **BuildHeap(A)** operation takes an array A as input and turns it into a heap, by making sure the heap property holds at the end of the operation. 
   It makes use of the Heapify operation. Notice, we only need to call Heapify on the first half of the array A as a leaf vertex is always the root of a heap (with one element). As a **Heapify** operation takes $O(\log n)$ time, one might conclude that the **BuildHeap** operation takes $O(n \log n)$ time, however, a somewhat more careful analysis shows that the runtime is $O(n)$.
3. The **DeleteMin(A)** operation removes the vertex with the smallest key value, which is the root node. It is implemented by exchanging the root element with the last element in the heap (i.e., the right most leaf at the last level). After removing the root vertex, we perform the **Heapify(A, 1)** operation to restore the heap structure. The runtime is therefore clearly $O(\log n)$.
4. The last operation of interest is the **DecreaseKey(A, i, v)** which decreases the key value of i to v. If the new key value is smaller than the key value of its parent, we recursively exchange the vertex i with its parent vertex, until the heap property is restored. This requires at most $O(\log n)$ time. 

To implement Prim’s algorithm using binary heaps, we need to start by building a heap with n=|V| entries. The key value of a vertex v is initialized as f(v) (according to Step 1 of Prim’s algorithm). Subsequently, we perform n **DeleteMin** operations, to find the vertex with the smallest f(v) value and after each **DeleteMin** operation we perform a **DecreaseKey** operation on each of the neighbors (in the graph G) of the deleted vertex. Hence, at most |E| **DecreaseKey** operations are needed, resulting in an overall time complexity of $O(|V| +  |E| \log |V| )$.
## Graph preprocessing for sparse graphs
Collaps the graph to a graph with one singular node or two nodes.

See explanation of pseudocode on page 61 of the book.
### Pseudocode
```
def Preprocess(G, T):
	for each v in V(G):
		mark(v) = False;
		MakeSet(v);
	
	for each u in V(G):
		if mark(u) == False:
			choose v in T(u) with w(u,v) minimal Union(u,v);
			T = T + orig(u,v);
			mark(u) = mark(v) = True;
	
	V(G') = {FindSet(v) | v in V(G)}
	E(G') = Null
	
	for each (x,y) in E(G):
		u = FindSet(x);
		v = FindSet(y);
		if u != v:
			if (u, v) not in E(G'):
				E(G') = E(G') + (u,v);
				orig(u,v) = orig(x,y); w(u,v) = w(x,y)
			elif w(x,y) < w(u,v):
				orig(u,v) = orig(x,y);
				w(u,v) = w(x,y);
	
	construct teh adjacency list Γ(u) for G'
	return G' and T
```
# Fibonacci Heaps
