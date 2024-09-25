# Fibonacci Heaps
The following 3-step procedure shows that both Dijkstra’s SP-algorithm or Prim’s MST-algorithm can be implemented using a priority queue:
1. Maintain a priority queue on the vertices V(G).
2. Put s in the queue, where s is the start vertex (Shortest Path) or any vertex (MST). Give s a key of 0. Add all other vertices and set their key to infinity.
3. Repeatedly delete the minimum-key vertex v from the queue and mark it scanned. For each neighbor w of v do: If w is not scanned (so far), decrease its key to the minimum of the value calculated below and w’s current key:
   -  SP: key(v) + length(vw),
   - MST: weight(vw).
Continued on page 64.
## Amortized analysis
Amortized analysis can be used to show that the average cost of an operation is small, if one averages over a sequence of operations, even though a single operation might be expensive. Amortized analysis differs from average-case analysis in that probability is not involved; an amortized analysis guarantees that average performance of each operation in the worst case.

There are several techniques used to perform an amortized analysis, the method of amortized analysis used to analyze Fibonacci heaps is the **potential method**. When using this method we determine the amortized cost of each operation and may overcharge operations early on to compensate for undercharges later.

 The potential method works as follow:
- We start with an initial data structure $D_0$ on which s operations are performed.
- For each i = 1, . . . , s, we let $c_i$ be the actual cost of the i-th operation and $D_i$ be the data structure that results after applying the i-th operation to the data structure $D_{i-1}$.
- A potential function we call $\phi$ maps each data structure $D_i$ to a real number $\phi (D_i)$, which is the potential associated with the data structure $D_i$.
- TODO continue at page 69