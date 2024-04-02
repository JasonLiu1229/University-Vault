# Preflow-push algorithms
Preflow-push algorithms are different in nature than the Ford and Fulkerson method, as these algorithms do not construct a sequence of flows whose value |f| increases at each iteration.

Instead, a sequence of **preflows** f is constructed. Preflows are like flows in the sense that they also respect the skew symmetry and capacity constraints, but they are allowed to violate the flow conservation property

However, if there is no flow conservation in a vertex, then the amount of flow entering the vertex must dominate the amount of flow leaving it. Formally, a preflow is a function $f: V x V \rightarrow R$ for which
1. Capacity constraint: $f(u, v) \le c(u, v) \text{ for all } u, v \in V$.
2. Skew symmetry: $f(u,v) = -f(v,u) \text{ for all } u, v \in V$.
3. Excess property: $e(u) = \sum_{v\in V} f(v,u) \ge  \text{ for all } u \in V - \{s\}$.

If e(u) $\gt$ 0, we state that the vertex u $\ne$ t is **overflowing**. 

Intuitively, the preflow-push method works as follows. 
1. We start by giving vertex s a height h(s) of |V| and all other vertices v a height h(v) of 0.
2. Next, we push the maximum possible flow from s to its neighbors, causing these vertices to overflow. The algorithm repeatedly selects an overflowing vertex. This vertex u will either have a neighbor v (in the residual network) with a height h(v) = h(u) + 1 such that some of the excess flow in u can flow down to v (possibly overflowing v). Notice, if there is an edge in the residual network, then there still remains some capacity from u to v. If an excess vertex does not have such a neighbor, we lift the vertex (by increasing its height h(u)) creating such a neighbor.

Thus, the idea is that the initial flow in the neighbors of s will gradually flow downward through the network, while all the vertices (except the sink t and source s) gain height. At some point, this causes a maximum amount of flow |f| to reach the sink t. However, the initial flow pushed by s may be considerably larger. What happens next is that the vertices u $\ne$ s, t continue to gain height, such that the redundant flow returns to the source s. When all excess capacity has been removed, the preflow becomes a flow with the required maximum capacity |f|. 

A preflow-push algorithm will allow two operations (on overflowing vertices): a push and a lift. The applicability of these operations is regulated by the height of a vertex. A height function h : V $\rightarrow$ R must fulfill the following requirements:
1. h(s) = |V| and h(t) = 0,
2. If (u, v) $\in$ $E_f$: $h(v) \ge h(u) - 1$
Thus, the height may decrease by at most one when following an edge in the residual network $G_f = (V, E_f)$, where $E_f$ with f a preflow is defined in exactly the same manner as for a flow f, i.e., $(u, v) \in E_f \text{ if } c_f(u, v) = c(u, v) - f(u, v) \gt 0$. This height property/constraint is very important as it will guarantee the optimality of the end flow in a straightforward manner.

Let's now look at the pseudocode of push and lift. The push operation applies to an overflowing vertex u if there is at least one neighbor v in the residual network (i.e., one outgoing link with some remaining capacity) with a height one below u, that is, h(v) = h(u) - 1. In this case we increase the flow from u to v, if this causes f(u, v) to become equal to c(u, v) we state that the push operation saturates the link (u, v).
## Pseudocode push and lift
```
Push(u, v):
	Allowed if:
		e(u) > 0, (u,v) in Ef (i.e., cf(u,v)) and h(v) = h(u) - 1
	Push df(u,v) from u to v:
		df(u,v) = min(e(u), cf(u,v))
		f(u,v) = f(u,v) + df(u,v)
		f(v,u) = -f(u,v)
		e(u) = e(u) - df(u,v)
		e(v) = e(v) + df(u,v)
```

```
Lift(u):
	Allowed if:
		e(u) > 0, for all v in V:
			(u,v) in Ef implies h(v) >= h(u)
	Lift u:
		h(u) = 1 + min(h(v) : (u,v) in Ef)
```

If such a neighbor v is not available, we lift u such that its height is one above the lowest neighbor (in $G_f$). It is important to notice that a vertex u, with $e(u) \gt 0$, always has at least one neighbor in $G_f$. Indeed, $e(u) = \sum_{v\in V}f(v, u) \gt 0$, thus there is at least a $v \in V$ with $f(v, u) \gt 0$. 

Hence,
	$c_f(u, v) = c(u, v) - f(u, v) = c(u, v) + f(v, u) \gt 0$
and $(u, v) \in E_f$. 

Thus, whenever a vertex u is overflowing, we can either perform a push or a lift operation if h is a height function.

The preflow algorithm is initialized as follows:
1. $u \in V - \{s\} : h(u) = 0, h(s) = |V|$
2. $(u, v) \in E, u, v \ne s : f(u, v) = 0$
3. $(s, u) \in E : f(s, u) = c(s, u), f(u, s) = -c(s,u) and e(u) = c(s,u)$

Note, h is a height function, because f(s, u) = c(s, u) implies (s, u) not in $E_f$, while all other vertices have a height of 0; hence, following an edge (u, v) in $E_f$ we cannot decrease in height (and thus certainly not decrease by more than one).

The lift operation may increase the height h(u) of a vertrex u. Thus, for h remain a height