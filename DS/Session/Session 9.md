# Coordination
> Part 2

## Distributed Mutual Exclusion
### Maekawa Voting
**Philosophy** 
- Drawback of Ricart-Agrawala: all processes need to agree —> linear scaling 
- Maekawa voting: only SUBSET of processes involved 
- Basic idea: “vote on behalf of others” 
- Candidate process must collect sufficient votes before entering

**Voting set for each process** $p_i$: $V_i$
- $V_i \subseteq \{p_1, ..., p_N\}$ (Required)
- $p_i \in V_i$ (Required)
- $V_i \cup V_j \neq \varnothing$ (Required)
- $|V_i| = K$ (Fairness) (Bonus) 
- Every $p_j$ contained in exactly M voting sets (Bonus)

**Basic idea**
- process $q \in (V_i \cup V_j)$ 
- —> q makes sure $p_i$ and $p_j$are not simultaneously executing critical section 
- —> safety condition met 
- q only votes for one process 
- Additional state needed per process: **voted**
#### Algorithm
- **Process i requesting access**
	**Initialization**
		state = Released
		voted = False
	**Enter()**
		state = Wanted
		multicast Request(pi) to voting set Vi
		wait until K reply messages received
		state = Held
	**Leave()**
		state = Released
		multicast Release to voting set Vi
- **Member of Vi receiving request**
**When receiving Request(pj) at pi**
```
if ((state == Held) or (voted == True)) { 
	enqueue Request in Q 
	// do NOT reply 
} else { 
	send Reply to pj 
	voted = True 
}
```

**When receiving Release(pj) at pi** 
```
if (Q != empty) { 
	dequeue pending Request m from Q 
	send Reply to sender(m) 
	voted = True 
} else { 
	voted = False 
}
```

Differences w.r.t. Ricart-Agrawala 
- Additional state variable per process needed (voted or not) 
- Multicast request to enter to voting set only 
- Explicit leave needed (so voting processes can vote for other process)
#### Constructing voting sets
**Choosing parameters**
- Theoretical result : optimal solution (minimal K)
	- K ≈ sqrt(N)
	- M = K
- In practice : difficult to calculate optimal Vi
	Sub-optimal solution
	- K ≈ 2sqrt(N)
	- M = K

**Practical algorithm (for N=$S^2$)**
- S = 3
	![[Pasted image 20240615165314.png]]

**In general**
	Construct SxS matrix A, consisting of all processes
- i is row where p is found
- j is column where p is found
- Ri = i-th row of A
- Cj = j-th column of A 
Voting set Vp = Ri $\cup$ Cj

**Voting set for each process** $p_i$: $V_i$
- $V_i \subseteq \{p_1, ..., p_N\}$ (Required)
- $p_i \in V_i$ (Required)
- $V_i \cup V_j \neq \varnothing$ (Required)
- $|V_i| = K$ (Fairness) (Bonus) 
- Every $p_j$ contained in exactly M voting sets (Bonus)

**Checking this Vp ...**
$p \in R_i, p\in C_j \Rightarrow p \in V_p$
