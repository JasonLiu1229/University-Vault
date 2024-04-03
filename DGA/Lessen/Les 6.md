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

The lift operation may increase the height h(u) of a vertex u. Thus, for h to remain a height function we must have that $h(v) \ge h(u) - 1$ for $(u, v) \in E_f$. As h(u) is increased to one plus the height of the lowest neighbor in $G_f$, this remains valid. A push operation does not alter the height of any vertex, but it may delete or add a new edge from or to $G_f$. If the push operation saturates (u, v), the edge (u, v) is removed, which causes no problem.
The push operation may also add the edge (v, u) to $E_f$ (as $c_f(v,u) = c(v,u) +f(u,v)$). Following the edge from v to u increases the height by one, clearly fulfilling the height constraint, which forbids decreasing the height by more than one along such an edge. Therefore, we have proven that: Whenever a vertex is overflowing, i.e., $e(u) \gt 0$, we can perform a push or a lift operation. 

Assuming that at some point there are no overflowing vertices left, we can easily prove that f is a maximum flow as follows.
## Theorem 5.1
If the preflow-push algo terminates, because e(u) = 0 for all $u \in V - \{s,t\}$, it produces a max flow f for the flow network G = (V, E).
### Proof
We first prove that at any stage during the execution of the algorithm, there is no simple path from s to t in $G_f$. Then, this path is composed of at most |V| - 1 edges (as it is simple). It must start in s with h(s) = |V| and follow a sequence of |V| -1 edges in $E_f$. While following each of these edges, the height can decrease by at most one (due to the height constraint), meaning while reaching t, the height must still be at least one. However, h(t) = 0. **Contradiction**

When the algorithm terminates, there is no excess flow and thus f is a flow. Moreover, there is no path from s to t in $G_f$, meaning there is no augmenting path in the Ford and Fulkerson sense. 

As a result, the miun-cut max flow theorem proves the statement. 
# Performance of the Preflow-push algorithm
In this section we will place an upper bound on the number of lift, saturated and unsaturated push operations. Recall, a push on (u, v) is saturating if $d_f(u,v) = c_f(u,v)$, causing the removal of the edge (u, v) from $E_f$
## Lemma 6.1
When performing the preflow-push algorithm on G = (V, E) a flow network, there is a simple path from any overflowing vertex u to s in $E_f$ and the height h(u) of any vertex is at most 2|V| - 1.
### Proof
Assume u in V is overflowing, that is, excess $e(u) \gt 0$.

Let U be the set of vertices reachable via a simple path from u in $E_f$. Let also $\bar{U}$ = V - U and assume s not in U. 

If v in U and w not in $\bar{U}$ then (v, w) not in $E_f$, meaning $f(v, w) = c(v, w) \ge 0$, and by skew symmetry we find $f(w, v) \le 0$. Hence, $f(\bar{U}, U) \le 0$. Now, $e(U) = f(V,U) = f(\bar{U}, U) + f(U, U) = f(\bar{U}, U) \le 0$, where the flow to its own set f(U, U) = 0 due to the skew symmetry. Notice, e(U) is well-defined as s not in U. But, $e(v) \ge 0$ for all v in V meaning e(u) must be zero, contradicting $e(u) \gt 0$.

As this simple path has a length of at most |V| - 1, h(s) = |V| and the height can only decrease by one along an edge in $E_f$, we find $h(u) \le 2|V| - 1$ for u overflowing. 

Moreover, any vertex is still overflowing immediately after a lift. 
## Lemma 6.2
When performing the preflow-push algorithm on G = (V, E) a flow network, at most (2|V| - 1)(|V| - 2) lifts and 2|V| |E| saturated pushes are performed.
### Proof
Only vertices u in V - {s, t} van be lifted.

Each lift increases h(u) by at least one, with h(u) = 0 initially. Hence, at most (2|V| - 1)(|V| - 2) lifts occur.

A push operation that saturates an edge (u, v) removes this edge from $E_f$. During this operation, h(v) = h(u) - 1. To recreate this edge there has to be a push from v to u, which requires that h(v) = h(u) + 1, thus h(v) has to increase by two. Meaning, h(h) + h(v) increases by at least two between any two saturated pushes on either (u, v) or (v, u).

Now, during the very first push between u and v, we must have $h(u) + h(v) \ge 1$. Due to Lemma 6.1, we know that during the last such push, we have $h(u) + h(v) \ge (2|V| -1) + (2|V| -2) = 2(2|V| - 1) - 2$.

This implies there can be at most $\dfrac{h(u) + h(v) + 1}{2} \le 2|V| - 1$ saturated pushes along (u, v) or (v, u), as thus sum increases by 2 in between two such pushes. In total, we therefore have at most $(2|V| - 1)|E| \lt 2 |V||E|$ saturated pushes.
## Lemma 6.3
When performing the preflow-push algorithm on G = (V, E) a flow network, at most $4|V|^2 (|V| + |E|)$ non-saturating pushes are performed.
![[Pasted image 20240403152933.png]]
### Proof
Define $\psi = \sum_{v \in X} h(v)$, where X is the set of overflowing vertices. 

Initially $\psi = 0$. Due to lemma 6.1, each lift operation can increase $\psi$ by at most 2|V| (minus one) as X remains the same. A saturated push along (u, v) may turn v into an overflowing vertex. Thus, v might be added to X, potentially increasing $\psi$ by 2|V| (minus one). Thus, due to the previous bounds on the number of lifts and saturating pushes, $\psi$ increases by at most $(2|V|)(2|V|^2) + (2|V|)(2|V||E|) = 4|V|^2 (|V| + |E|)$. 

A non-saturating push along (u, v) implies that e(u) becomes 0, i.e., u is no longer overflowing. The vertex v may become an overflowing vertex due to this push, but h(v) = h(u) - 1; hence, an desaturating push decreases $\psi$ by at least 1 and $\psi \ge 0$ at all times. This allows us to conclude that at most $4|V|^2 (|V| + |E|)$ non-saturating pushes can occur.
## Theorem 6.1
