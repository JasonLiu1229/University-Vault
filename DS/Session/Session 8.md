# Coordination
> Part 1

Coordination is really important in distributed systems, many things rely on each other, so good coordination is key. 

One example is, 2000 drones light up in the sky. Many things can go wrong when the drones are not coordinated properly.
## General problem
**Given a set of processes Π={pi}, distributed over multiple hosts**
- How to coordinate actions?
	- Processes need to work together harmoniously, even though they are running on different hosts. This requires protocols and algorithms to manage the coordination.
- Agree on contents of shared variables (“global state”)?
	- In distributed systems, it is crucial for processes to have a consistent view of shared variables or the global state. This consistency ensures that all processes have the same data, which is essential for correct operation.

**Example problems**
- Control access to common database (locking) 
	- When multiple processes need to access a shared database, mechanisms like locking are used to ensure that only one process can modify the database at a time, preventing data corruption.
- Elect central node in ad hoc network 
	- In an ad hoc network, there might be a need to elect a central node (leader) that coordinates the actions of other nodes. Election algorithms like the Bully algorithm or the Paxos algorithm can be used for this purpose.
- Elect time-server in network 
	- Time synchronization is crucial in distributed systems. Electing a time-server ensures that all nodes in the network have a consistent view of time. Protocols like the Network Time Protocol (NTP) can help achieve this.
- Avoid static master-slave relations to enhance robustness
	- Static master-slave configurations can lead to single points of failure. To enhance robustness, distributed systems often use dynamic leader election and failover strategies to ensure that the system can recover from failures.

We will cover two mechanism that will help fix these problems.
- **Distributed Mutual Exclusion**
	1. Problem statement 
	2. Evaluation metrics 
	3. Centralized approach 
	4. Ring approach 
	5. Multicast approach 
		1. Ricart-Agrawala 
		2. Maekawa voting
- Election mechanism
## Distributed Mutual Exclusion
### Critical sections
**Goal: Coordinate process access to shared resourced**
![[Pasted image 20240615121428.png]] 
- Accesses common resource 
- No other process should access same resource

**Distributed mutual exclusion**
- No shared variables between processes 
- No support from common coordinating OS kernel 
- Only rely on message passing
### Problem statement
**Consider**
- N processes {$p_1, ... , p_N$}, NO shared variables 
- Access common resources in a critical section 
- Asynchronous system 
- Processes CAN communicate (know each other)

**Failure modes** 
- Reliable channel (each message delivered, exactly once) 
- No process failures 
- Processes are well-behaved (leave critical section eventually)

![[Pasted image 20240615125651.png]]
#### A good solution should ...
1. 