# The Ford-Fulkerson method
## Definition 2.1
Given a flow network G and a flow f in G, we can define the residual flow network $G_f$ by setting $G_f$ = (V, $E_f$) and $c_f(u, v)$ = c(u, v) - f(u, v). The set of edges $E_f$ = {(u, v) | $c_f(u, v)$ $\gt$ 0}.

The residual network $G_f$ thus represents the remaining capacity given flow f. 

Notice, if (u, v) not in E, that is, c(u, v) = 0 and there was a flow from v to u, i.e., f(u, v) $\lt$ 0 due to the skew symmetry, then $c_f(u, v)$ = 0 - f(u, v) $\gt$ 0, meaning (u, v) in $E_f$.
## Lemma 2.1
Let f be a flow in G and f' in $G_f$, then f + f' defined as (f + f')(u, v) = f(u, v) + f'(u, v), for all (u, v) in V, is a flow and |f + f'| = |f| + |f'|.
### Proof
The proof is completely analogue to Lemma 1.1, except that we also need to verify the capacity constraints:
(f + f')(u, v) = f(u, v) + f'(u, v) $\le$ f(u, v) + $c_f(u, v)$ = c(u, v).
## Definition 2.2
An augmenting path p with respect to a flow network G and a flow f is a simple path from s to t in $G_f$, meaning each vertex on the path is visited only once.

Notice, all edges $E_f$ in $G_f$ have a positive capacity, meaning an augmenting path p has a positive residual capacity $c_f(p)$ defined as $min\{c_f(u, v) | (u, v) \in p\}$. An augmenting path p therefore immediately results in a flow $f_p$ in the residual network $G_f$, by defining $f_p(u, v)$ = $c_f(p)$ for the edges (u, v) on p and $f_p(u, v)$ = -$c_f(p)$ for (v, u) on p. Combining this with the previous two lemmas, we have the following corollary.
## Corollary 2.1
Let f be a flow in G and p an augmenting path with respect to G and f, then f' = f + $f_p$ defines a new flow in G with |f'| $\gt$ |f|.

This gives cause to the Ford-Fulkerson method:
## Algorithm 2.1 (Ford-Fulkerson)
```python
Initialize f(u, v) = 0 for all u, v;
while there exists an augmenting path p:
	augment flow f with $f_p$;
return f;
```

## Definition 2.3
## Lemma 2.2
## Theorem 2.1