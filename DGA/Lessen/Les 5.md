# Performance of the Ford-Fulkerson algorithm
When running the Ford-Fulkerson algorithm, we start with a flow value |f| = 0. After each iteration, |f| increases. The question is however whether |f| converges to the maximum flow value for the flow network G = (V, E). The answer is that if we allow irrational capacities c(u, v), the algorithm might not converge to the maximum flow value.

An example is shown in Figure 8, that depicts a network G = (V, E) consisting of 6 nodes and 9 edges with edge capacities of 1, $r =\dfrac{(\sqrt{5}-1)}{2} \lt 1$ and M, where M $\ge$ 2 is an integer. Note, r is an irrational number that satisfies the equation 1 - r =  $r^2$. Define the paths $p_0, p_1, p_2$ and $p_3$ as
- $p_0 : s \rightarrow x_2 \rightarrow x_3 \rightarrow t$,
- $p_1 : s \rightarrow x_4 \rightarrow x_3 \rightarrow x_2 \rightarrow x_1 \rightarrow t$,
- $p_2 : s \rightarrow x_2 \rightarrow x_3 \rightarrow x_4 \rightarrow t$,
- $p_3 : s \rightarrow x_1 \rightarrow x_2 \rightarrow x_3 \rightarrow t$.

![[Pasted image 20240316140715.png]]

Now consider what happens to the residual capacities $c_f(x_2, x_1), c_f(x_3, x_2)$ and $c_f(x_4, x_3)$ if we use the paths $p_0$ followed by $p_1, p_2, p_1, p_3$.

We denote $f_n$ as the flow obtained after using n paths. If we start with path $p_0$, with $c_{f_0}(p0)$ = 1, we get the following residual capacities: $c_{f_1}(x_2, x_1)$ = 1= $r^0$, $c_{f_1}(x_3, x_2)$ = 1 and $c_{f_1}(x_4, x_3)$ = r.

Hence, $c_{f_1}(p_1)$ = r and $p_1$ decreases the capacity on $(x_2, x_1)$ such that $c_{f_2}(x_2, x_1)$ = 1 - r = $r^2$. The residual capacity on $(x_4, x_3)$ and ($x_3, x_2$) is also reduced by $p_1$, however, path $p_2$ will restore these capacities as $c_{f_2}(p_2)$ = r (due to $c_{f_2}(x_2, x_3)$ = r), meaning $c_{f_3}(x_2, x_1)$ = $r^2$, $c_{f_3}(x_3, x_2)$ = 1 and $c_{f_3}(x4, x3)$ = r. Similarly, if we now use the paths $p_1$ followed by $p_3$, we find that $c_{f_3}(p1)$ = $c_{f_4}(p3)$ = $r^2$. Path $p_1$ reduces the residual capacity on the edge $(x_4, x_3)$ to r - $r^2$ = r3, while path $p_3$ restores the residual capacities of $(x_2, x_1)$ and $(x_3, x_2)$ back to 1 and $r_2$. In other words $c_{f_5}(x_2, x_1)$ = $r^2$, $c_{f_5}(x_3, x_2)$ = 1 and $c_{f_5}(x_4, x_3)$ = $r^3$.

If we now repeatedly use the paths $p_1, p_2, p_1, p_3$, one finds that $c_{f_7}(x_2, x_1)$ = $r^4$, $c_{f_7}(x_3, x_2)$ = 1 and $c_{f_7}(x_4, x_3)$ = $r^3$ and $c_{f_6}(p_1)$ = $c_{f_7}(p_2)$ = $r^3$; $c_{f_9}(x_2, x_1)$ = $r^4$, $c_{f_9}(x_3, x_2)$ = 1 and $c_{f_9}(x_4, x_3)$ = $r^5$ and $c_{f_8}(p_1)$ = $c_{f_9}(p_3)$ = $r^4$, etc. In other words, the Ford and Fulkerson algorithm does not terminate and the net total flow |$f_i$| converges to $2 \sum_{i=0}^{\inf} r^i - 1 = 2 + \sqrt{5} \lt 5$, while the maximum flow is 2M + 1 $\ge$ 5. Hence, the Ford-Fulkerson algorithm does not guarantee convergence in general.

However, things are less problematic when all the capacities are rational (r in the previous example is an irrational number). In this case, we can multiply all capacities by the smallest common multiple of all denominators that appear in a capacity c(u, v), thereby reducing the capacities to integer numbers. When all the capacities are integers, then all augmenting paths clearly have an integer maximum flow.

As a result, the Ford-Fulkerson algorithm 3 Performance of the Ford-Fulkerson algorithm 28 guarantees convergence in at most |f\*| steps, where |f\*| is the maximum flow of the network of interest (and which is certainly upper bounded by the sum of all capacities c(u, v)). Thus, if a network has a maximum flow of 1,000,000, the algorithm might potentially take as many as 1,000,000 steps.

To avoid such a slow convergence one may rely on the Edmonds-Karp algorithm that will select the augmenting path p in the residual network by applying a breadth-first search to determine the shortest path from s to t, in the next section we prove that the time complexity of such an approach is O(|V|$|E|^2$), with |V| the number of vertices and |E| the number of edges in the flow network, independent of the flow capacity.
# The Edmonds-Karp algorithm (1969)
The analysis of the Edmonds-Karp algorithm depends on the length of the shortest paths $δ_f(s, u)$ between the vertex s and u in V in the residual network $G_f$, where f is a flow in G. The next lemma proves that the shortest-path distances monotonically increase with each flow augmentation.
## Lemma 4.1
Let f and f' be two successive flows obtained by the Edmonds-Karp algorithm and $G_f$ and $G_{f'}$ their residual networks, respectively. Then, for all v in V : $δ_f(s, v) \le δ_{f'}(s, v)$
### Proof
Suppose the lemma is false and choose:
	v in V : $δ_f(s, v) \gt δ_{f'}(s, v)$
such that 


