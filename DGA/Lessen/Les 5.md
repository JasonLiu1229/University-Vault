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

Hence, cf1 p1  r and p1 decreases the capacity on x2, x1 such that cf2 x2, x1  1  r  r2. 