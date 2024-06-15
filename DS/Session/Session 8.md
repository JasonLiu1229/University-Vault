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
1. Be safe, **REQUIRED**
	- At most ONE process may execute in critical section at any time
2. Ensure liveness, **REQUIRED** 
	- Requests to enter/leave critical sections eventually succeed 
	- Deadlock-free algorithm 
	- No starvation
3. Be fair, **Bones** 
	- Access to critical section is granted using “happened-before” relation. Thus, use logical clock to order access requests.
#### Critical section access API
**Application level primitives**
- **enter()**: enter critical section, block if necessary 
- **resourceAccess()**: access the shared resource (in critical section) 
- **exit()**: leave critical section – make free for other processes
![[Pasted image 20240615130106.png]]
### How to quantify solution quality?
**Evaluation metrics**
1. **Bandwidth consumption**
	= number of messages sent to enter/leave critical section
2. **Client delay**
	- Time needed to enter/leave critical section 
	- Measured in UNLOADED system 
	- One-way network delay
3. **System throughput**
	- How many processes can access critical section in given time period? 
	- depends on resourceAccess() time
	- **derived measure**: synchronization delay = average (time process (i+1) enters – time process (i) leaves) 
	- LOADED system
![[Pasted image 20240615130511.png]]
### How would you build such a system?
#### Central server
**Centralized algorithms (one server)**
- Easy 
- But typically poor scaling
![[Pasted image 20240615132707.png]]
**Messages**
- Client -> Server : **Request** 
- Server -> Client : **Grant** 
- Client -> Server : **Leave**
##### Algorithm
![[Pasted image 20240615132759.png]]
**Token variable**
	== process ID currently active 
	== -1 if critical section not taken
**Message queue Q**
	Stores pending requests
![[Pasted image 20240615132913.png]]

**Client side**
1. enter() 
	send Request message to server 
	wait until Grant received
2. accessResource() 
	perform any application specific logic
3. leave() 
	send Leave message to server

**Server side**
When receiving request:
```
if (token == -1) { 
	send Grant to requesting process token=sender(Request) 
} 
else {
	enqueue Request in Q
}
```
When receiving leave:
```
1. Dequeue oldest message m from Q
2. Token = sender(m)
3. send Grant to sender(m)
```
##### Algorithm OK ?
1. Safety ✅
	Guarded by tokens 
2. Liveness ✅
	1. Request to enter
		- All processes eventually leave
		- Each leave dequeues a message from Q
		- If oldest request dequeued
		- => every request eventually handled 
	2. Request to leave
		- No permission needed from server
3. Fairness ✅
	Order Q according to "happened-before"
		They ordered based on their arrival times, ensuring they are processed based on when they are made.
##### Algorithm efficient?
1. **Bandwidth usage**
	![[Pasted image 20240615133921.png]]
	During every enter, two messages are needed. During every leave, only one message of the client is needed.
	So, there is not much bandwidth needed.
2. **Client delay (unloaded system)**
	δ=time needed for 1 communication 
	RTT = 2δ
	![[Pasted image 20240615134055.png]]
	It takes 1 delta for each request and one delta for each grant, so two deltas each enter. For the leave, it does not block any other request, so this will not take any delta time. 
3. **Synchronization delay (loaded system)**
	![[Pasted image 20240615134509.png]]
	First 