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
	First p1 starts a request and enters the critical section (CS), when it leaves it sends a message to the server and the server has to grant the up following requests that might have entered when p1 was in the CS. P2 requested a request when p1 was in the CS, so we will grant the request after p1 leaves.
	
	The time it took for p1 to leave and p2 to start (so granting from server) is 2 deltas, and could be considered long.
#### Ring-based algorithm
- Processes {p0, ..., pN-1} arranged in logical ring 
- Process pi has one unidirectional communication channel to p(i+1) 
- Token = message passed along ring
	![[Pasted image 20240615140156.png]]
So token gets passed around for every interval t. When a process wants to enter the CS, it needs to wait until the token is passed to him.
	![[Pasted image 20240615140348.png]]
##### Algorithm Ok?
**Each process p**
When process p receives "Token":
```
if (p wants access) { 
	execute logic in critical section leave() 
} else { 
	send(Token) to next process
}
```
1. **Safety** ✅
	- Process can only send Token if it has received Token
2. **Liveness** ✅
	- Process eventually leave 
		=> Token circulates in the ring (p not allowed new access !) 
		=> No starvation
1. **Fairness** ❌
	- Not guaranteed : processes need luck for early access 
	- Access order not based on “happened-before” of requests
##### Algorithm efficient?
1. **Bandwidth**
	![[Pasted image 20240615140850.png]]
	**Worst case:**
		The worst case would be when the process would request access right after his turn ended. This leads to N messages it needs to wait before it can access the CS.
	**Best case:**
		The best case would be that we ask permission right before we get access, this results in 1 message.
	**Average:**
		By average we have then (N+1)/2
2. Client delay (unloaded system)
	![[Pasted image 20240615140933.png]]
	Same analogy can be used here. For the best case, we get it at the same time when we ask it for so zero delta instead of one.
3. Synchronization delay (loaded system)
	![[Pasted image 20240615141442.png]]
	Synchronization delay could be rather long because we need to wait for N delta before we get the token at the worst case scenario. While best case scenario it takes one delta before it enters the CS. 
	
	So by average we say (N+1)$\delta$/2
### Multicast: Ricart-Agrawala algorithm
**Philosophy** 
- Use multicast to reduce bandwidth 
- Use logical clock (Lamport clock) to realize fairness 
- Basic mechanism to enter CS: multicast request and enter if all others agree

**Each process pi** 
- Has state variable 
	- Released : outside critical section 
	- Wanted : wants to enter 
	- Held : inside critical section 
- Lamport clock T 
- Queue Q to store pending Requests
![[Pasted image 20240615142005.png]]
**Organization of Q?**
- Lamport-clock based happened-before 
- Total ordering implemented to ensure consistency
<p1,T1> < <p2,T2> ⬄ (T1<T2) or ((T1 == T2) and (p1 < p2))
#### Lamport clock
A Lamport clock is a logical clock algorithm used in distributed systems to order events in a system where no global clock exists. It was introduced by Leslie Lamport in 1978. The purpose of a Lamport clock is to provide a partial ordering of events in a distributed system, ensuring that the causality of events is respected.

- **Initialization**: Each process initializes its logical clock to 0.
- **Event Handling**:
    - **Internal Event**: When a process performs an internal event, it increments its logical clock by 1.
    - **Send Message**: When a process sends a message, it increments its logical clock by 1 and attaches this clock value to the message.
    - **Receive Message**: When a process receives a message, it sets its logical clock to be the maximum of its current clock value and the clock value in the received message, then increments by 1.
#### Ricart-Agrawala algorithm
**Messages**
- Request(pi,Ti)
- Reply

**Each process pi**
- Initialization
	state = Released
- enter()
	state = Wanted 
	multicast Request(pi,Ti) to all processes 
	store T=Ti of Request message 
	wait until (N-1) Reply messages received 
	state = Held
- leave()
	 state = Released 
	 send Reply to all pending Requests in Q

**When receiving Request(pj, Tj) at pI (i != j)**
```
if ((state == Held) or ((state==Wanted) and (T,pi)<(Tj,pj))) { 
	enqueue Request in Q 
	// do NOT reply 
} else {
	send Reply to p
}
```
##### Examples
1.  Process p requests entry, all others in RELEASED-state
	- all (N-1) other processes reply immediately 
	- p can enter CS
2. Process p requests entry, one process q in HELD-state, all others in RELEASED-state
	- (N-2) other processes reply immediately 
	- p waits until q has left CS 
	- p can enter CS
	![[Pasted image 20240615143647.png]]
3. Processes p1 and p2 request entry, p3 not
	![[Pasted image 20240615143724.png]]
	Because p2 requested before p1, it will enter the critical section before p1 does.
##### Algorithm OK ?
1. **Safety: a proof** ✅
	Suppose p and q simultaneously executing critical section
	- both p and q received (N-1) Reply-messages
	- p sent Reply to q AND q sent Reply to p
	- condition (state(i) == Held) or ((state(i) == Wanted) and (Ti, pi) < (Tj, pj))
		Does not hold for 
			a. (pj = q), (pi = p)
			b. And (pj=p),(pi=q) 
	
	Some logic for (a)
	- => !\[(state(p) == Held) or ((state(p) == Wanted) and (Tp,p)<(Tq,q))]
	- => (state(p)!=Held) AND \[(state(p)!=Wanted) or (Tq,q)<(Tp,p)]
	- => \[ (state(p) != Held) and (state(p)!=Wanted)] or \[(state(p) != Held) and (Tq,q)<(Tp,p)]
	- => (state(p) == Released) or \[(state(p) != Held) and (Tq,q)<(Tp,p)] 
	- => p can NOT be in state Released (because now in CS) 
	- => \[(state(p) != Held) and (Tq,q)<(Tp,p)]
	  
	Same logic for (b)
	  
	=> p and q can NOT be executing simultaneously in critical section
2. Liveness ✅
	Every Request eventually granted 
	- immediately 
	- after dequeueing from Q
	
	=> every process will eventually receive (N-1) answers
3. Fairness ✅
	Requests replied in happened-before order
##### Algorithm efficient?
1. Bandwidth
	![[Pasted image 20240615145105.png]]