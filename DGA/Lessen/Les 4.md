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

We need to introduce two more concepts before we can prove the max-flow min-cut theorem and thus the correctness of the algorithm above.
## Definition 2.3
A cut (S, T) in a flow network G = (V, E) is defined as a partitioning of V into S and T such that s in S, t in T (and S $\cap$ T as it is a partitioning).

Given a flow f in G, we define the net flow f(S, T) across the cut (S, T) as
	$f(S,T) = \sum_{u \in S, v \in T} f(u,v)$
The capacity c(S, T) of the cut (S, T) on the other hand, is defined as 
	$c(S, T) = \sum_{u \in S, v \in T} c(u,v)$
Notice some of the terms f(u, v) may be negative, which is never the case for the capacity c(u, v).
## Lemma 2.2
Let f be a flow in G and let (S, T) be any cut, then f(S, T) = |f| $\le$ c(S, T)
### Proof 
Let X and Y be two subsets of V, then define
	$f(X, Y) = \sum_{u \in X, v \in Y} f(u, v)$
1. f(X, X) = 0, due to skew symmetry
2. f(X, $Y_1$, $Y_2$) = f(X, $Y_1$) + f(X, $Y_2$) and f($X_1$, $X_2$, Y) = f($X_1$, Y) + f($X_2$, Y) if $Y_1 \cap Y_2$ = $X_1 \cap X_2$ = $\varnothing$.
As a result, since V = S $\cup$ T and S $\cap$ T = $\varnothing$, we have
	f(S, T) = f(S, V) - f(S, S) = f(S, V) = f(s, V) + f(S - s, V) = f(S, V) = |f|,
 where f(S - s, V) = 0. The inequality can be established as follows 
	 |f| = f(S, T) = $\sum_{u \in S, v \in T} f(u,v) \le \sum_{u \in S, v \in T} c(u,v)$ = c(S, T).
## Theorem 2.1
(Max-flow Min-cut theorem). Let f be a flow in a flow network G with source s and sink t, then the following three statements are equivalent:
1. f is a maximum flow in G,
2. The residual network $G_f$ contains no augmenting paths (that is, there is no simple path from s to t in $G_f$),
3. |f| = c(S, T) for some cut (S, T) of G.
### Proof
