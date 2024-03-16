# Performance of the Ford-Fulkerson algorithm
When running the Ford-Fulkerson algorithm, we start with a flow value |f| = 0. After each iteration, |f| increases. The question is however whether |f| converges to the maximum flow value for the flow network G = (V, E). The answer is that if we allow irrational capacities c(u, v), the algorithm might not converge to the maximum flow value.

An example is shown in Figure 8, that depicts a network G = (V, E) consisting of 6 nodes and 9 edges with edge capacities of 1, $r =\dfrac{(\sqrt{5}-1) and M , where M ' 2 is an integer.