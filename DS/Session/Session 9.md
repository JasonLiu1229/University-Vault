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
- $V_i \cup V_j \neq$ (Required)
- $|V_i| = K$ (Fairness) (Bonus) 
- Every $p_j$ contained in exactly M voting sets (Bonus)

**Basic idea**
- process $q \in (V_i \cup V_j)$ 
- —> q makes sure $p_i$ and $p_j$are not simultaneously executing critical section 
- —> safety condition met 
- q only votes for one process 
- Additional state needed per process: **voted**
#### Algorithm
