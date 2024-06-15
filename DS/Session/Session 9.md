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
- $V_i \cap V_j \neq \varnothing$ (Required)
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
- $V_i \cap V_j \neq \varnothing$ (Required)
- $|V_i| = K$ (Fairness) (Bonus) 
- Every $p_j$ contained in exactly M voting sets (Bonus)

**Checking this Vp ...**
	$p \in R_i, p\in C_j \Rightarrow p \in V_p$
	$V_p = R_i \cup C_j$
	$V_q = R_s \cup C_t$
	$\Rightarrow V_p \cap V_q = (R_i \cup C_j) \cap (R_s \cup C_t) = (R_i \cap Rs) \cup (R_i \cap C_t) \cup (C_j \cap R_s) \cup (C_j \cap C_t)$ 
	**BUT** $R_k \cap R_I \neq \varnothing$ (for any k, l)
	$\Rightarrow V_p \cap V_q \neq \varnothing$
	K = 2S - 1
	K = M
#### Example
	![[Pasted image 20240615171043.png]]
#### Algorithm OK?
1. **Safety** ✅
	Suppose p and q simultaneously active
	=> all processes in Vp and Vq voted for p AND q 
	=> process t in Vp ∩ Vq ≠ Φ voted for p AND q 
	impossible: 
		voted=True immediately after voting for 1 process
2. Liveness ❌✅
	Deadlock prone![[Pasted image 20240615171413.png]]
	- **Circular Wait**: When processes form a circular chain of waiting, where each process in the chain is waiting for permission from the next process, deadlock can occur. For example, if process P0 is waiting for P1, P1 is waiting for P2, and P2 is waiting for P0, they form a circular wait.
	- **Mutual Exclusion**: Each voting set must provide permission for a process to enter its critical section. If multiple processes request access simultaneously, the voting sets' intersections might cause them to block each other.
	- **Hold and Wait**: Processes hold permissions they have already received while waiting for additional permissions. This can cause a situation where all processes hold some permissions but cannot proceed because they are waiting for others.
	![[Pasted image 20240615171655.png]]
	But if we use Lamport clock, this will solve the deadlock.
3. Fairness ❌✅
	Also no because one process can keep requesting before the others can reply that the next one needs to start. But can be solved with Lamport clocks.
#### Algorithm efficient?
1. **Bandwidth**
	enter() same as Ricart-Agrawala
		But message sent to voting set only! 
			-> K Request messages 
			-> K Reply messages 
	leave() 
		explicit Leave message now needed 
			-> K Release messages
2. **Client delay**
	same as Ricart-Agrawala 
		enter() : 2δ 
		leave() : 0δ
3. **Synchronization delay**
	![[Pasted image 20240615172146.png]]
	Because the intersection between p2 and p1 voting sets, would result in to waiting for p1, it needs to wait till p2 releases p1 and then p1 can reply.
### Summary on efficiency
| Algorithm         | Bandwidth enter() | Bandwidth leave() | Client delay enter() | Client delay leave() | Synchronization delay |
|-------------------|-------------------|-------------------|----------------------|----------------------|-----------------------|
| Central server    | 2M                | 1M                | 2δ                   | 0.5δ                 | 2δ                    |
| Ring algorithm    | constant          | (N+1)/2           | Nδ/2                 | 0                    | (N+1)δ/2              |
| Ricart-Agrawala   | (2N-1)M           | 0M                | 2δ                   | 0.5δ                 | 1δ                    |
| Maekawa voting    | 2KM               | KM                | 2δ                   | 0.5δ                 | 2δ                    |

* N: number of processes
* M: number of voting sets that each process belongs to
* δ: cost of sending a message
## Election Mechanisms
### The Election Problem