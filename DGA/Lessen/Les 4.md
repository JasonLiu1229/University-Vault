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

## Corollary 2.1.
## Algorithm 2.1
## Definition 2.3
## Lemma 2.2
## Theorem 2.1