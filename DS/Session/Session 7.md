# Replication
Replication in distributed systems is a strategy used to improve reliability, availability, and fault tolerance. It involves creating and maintaining multiple copies (replicas) of data or services across different nodes in a distributed network.

![[Pasted image 20240614140318.png]]
The image represents a basic client-server architecture with a direct mapping of data to a single server location. This design is straightforward and suitable for smaller systems where simplicity and data consistency are priorities.

![[Pasted image 20240614140338.png]]
The image illustrates a distributed system with replication across geographically dispersed servers. This architecture improves reliability, availability, and performance by ensuring that data is always accessible, even in the event of server failures. Middleware plays a crucial role in managing the replication process, ensuring data consistency and synchronization across the distributed network.
## Why replication?
1. Improving performance
	- Balancing the load between servers
	- Geographical spreading to reduce the latency
	![[Pasted image 20240614140759.png]]
2. Increased availability
	- There is P probability of failure of one server
	- Then $1-p^n$ probability that system with n replicas will still be available if replicates are independent
	For instance if we have p = 0.1, then when we have 1 replica, we have 90% chance that the system will still be available, while adding one more replica increases our chances to 99%. 
3.  Data corruption protection (fault-tolerance)
	- Replication can protect against corrupt data
	- How? Voting system: 2f +1 replicas can deal with f corrupt replicas
		- So, Result is accepted if the majority of the replicas return the same value.
## Replicas challenges
Replicas has its advantages, but is it always good?
One downside is that the data needs to be consistent between replicas, this increases the bandwidth overhead when changes happen in one replica.
### CAP theorem
Consistency Availability Partition-tolerance
- Consistency: all nodes always see the same data
- Availability: every request receives a response
- Partition-tolerance: guarantees remain even when network failures prevent communication
"It is impossible for a distributed computer system to simultaneously provide all three of these guarantees"
#### Impact in practice
- Optimize consistency at the cost of availability
- Or optimize availability at the cost of consistency
![[Pasted image 20240614171218.png]]
#### Can we loosen consistency?
Different applications, provide different consistency guarantees.
![[Pasted image 20240614171602.png]]
- **Financial Application (e.g., Online Banking)**:
    - **Consistency Requirements**: Strong consistency guarantees.
    - **Reason**: In financial transactions, it’s essential that all operations reflect the most recent data to prevent errors such as overdrafts or double spending. Consistency is critical to ensure the integrity and correctness of transactions.
    - **Characteristics**:
        - Immediate reflection of changes.
        - Ensures atomicity and durability.
        - Higher complexity and potential latency due to synchronization overhead.
    - **Examples**: Account balance updates, fund transfers, transaction histories.
- **Train Information Application**:
    - **Consistency Requirements**: Weak consistency guarantees.
    - **Reason**: Train information applications can tolerate slight delays in updating information such as schedules, delays, or platform changes. The system prioritizes availability and responsiveness over immediate consistency.
    - **Characteristics**:
        - Eventual consistency is acceptable.
        - Updates might not be immediately visible across all nodes.
        - Enhanced performance and availability.
    - **Examples**: Real-time train schedules, platform changes, delay notifications.

- **Strong Consistency**: Ensures that once a write is completed, any subsequent reads will reflect that write. This is crucial in applications where accurate and up-to-date information is critical.
- **Weak Consistency**: Accepts that not all reads reflect the most recent write immediately. Some delay is permissible, which can improve system performance and availability.
## Consistency Models
- Clear need for loosening the consistency guarantees
	- How? Through consistency models
![[Pasted image 20240614172408.png]]
### Data-centric consistency model
![[Pasted image 20240614173111.png]]
Consistency model = contract between client processes (C) and datastore of replicas (R)
- If client processes follow rules in the contract…
- …the datastore will work correctly & results will be predictable
- Rules deal with how parallel updates are received by other client processes
#### Strict consistency 
**Identical to single machine execution**

Strongest consistency guarantees 
**Immediate propagation** of all content updates 
Absolute **time ordering** of all shared access operations (global clock) 
A **read returns the last write** given that time ordering
![[Pasted image 20240614173325.png]]
#### Sequential consistency
**Relaxation: delay can exist in content updates**
Weaker consistency guarantees than strict consistency
Operations are interleaved in some fixed **order** 
All processes see the **same order**
![[Pasted image 20240614173505.png]]

**Some notation**
![[Pasted image 20240614173659.png]]
##### Exercises
![[Pasted image 20240614173847.png]]
**Answer:** Strict consistency

![[Pasted image 20240614173928.png]]
**Answer:**\
![[Pasted image 20240614173943.png]]

![[Pasted image 20240614174601.png]]
**Answer:**
We can't put a definite value on y, because the operation can happen between y = 16 and print y → 10, this means that if y is set to 16 and this print happens afterward but before y is set to 10, it is 16. But, it could also happen after y is set to 10 meaning it could also be 10. 

For x there is an answer, because we print x is 8 we can deduce that process one already happened, and it could not be 3. We print 12 before the second print, meaning P2 also already happened, so it can only stay 8. 

![[Pasted image 20240614181935.png]]
**Answer:**
![[Pasted image 20240614181946.png]]
Because we read "b" first, meaning we wrote "b" before this read. Next, we read "a", meaning that "a" we wrote a before the read, at last we see b again, but no write happened before this, so no order can be given.
#### Causal consistency
Causal relatedness 
	Does the operation potentially depend on another operation? If not, causally related otherwise concurrent.

Causally related?
![[Pasted image 20240614182334.png]]
**Causal consistent** writes are seen by all processes in the **same order**
**Concurrent** writes can be seen in **any order**
##### Exercise
![[Pasted image 20240614182633.png]]
**Answer:**
![[Pasted image 20240614182753.png]]\
The last two operations for P3 and P4 contradict each other leading it to no consistency. The relationship between W(x)a and W(x)b is because W(x)b happens after a read of x that outputs "a", for it to output "a" it needs to have been written that it was "a" at some time, that can only happen during P1 and so it is causally related.

For W(x)c there is no read that happened before, it can happen any time after "b" was written on x. You can especially tell that it could happen concurrent because P3 and P4 have contradictory outputs, because these two write could have happened at the same time.
#### PRAM / FIFO Consistency
Pipelined Random Access Memory consistency
- Writes from a single process arrive in the same order
- Writes from multiple processes can arrive in any order
![[Pasted image 20240614193111.png]]
#### Consistency & critical sections
![[Pasted image 20240614201034.png]]
#### Weak consistency
**Group operations to increase granularity of synchronization**
- Use of global synchronization variable S and synchronize operation
- Properties
	1. **Synchronize** cannot be performed until all previous writes have completed everywhere
	2. **Read** or **write** operations cannot be performed until all previous synchronize operations have completed
	3. **The order of synchronize operations is sequentially consistent**
![[Pasted image 20240614201231.png]]
#### Release Consistency
**Explicit synchronization operations defining critical section**
- **acquire(S)**: bring local state up to date (local updates can be propagated later) 
- **release(S)**: propagate local updates (remote updates can be propagated later) 
- **Properties** 
	1. Release cannot be performed until previous **reads and writes** done by the process have **completed**. 
	2. Read or write operations cannot be performed **until all previous acquire operations** done by the process have performed.
	3. The order of synchronization operations is **FIFO consistent**.
**Lazy Release Consistency**
- Acquire fetches newest state
- Do not send updates on release
- Efficiency gain if acquire/release done by same client
![[Pasted image 20240614201915.png]]
- **Reduced Synchronization Overhead**: By delaying the propagation of updates, lazy release consistency reduces the immediate synchronization overhead, which can improve performance.
- **Efficiency in Local Operations**: Particularly efficient when multiple acquire and release operations are performed by the same client, reducing unnecessary network communication.
#### Entry Consistency
**Associate specific data items (guarded data) to synchronization variables**
- **acquire(S)**
	- Obtain **exclusive** (write) or **non-exclusive** (read) access to the associated data 
	- **Synchronize** by fetching associated data from the variables owner (the last client that obtained exclusive access). 
	- Does not complete until guarded data is made up to date locally 
	- Exclusive access of a client precludes any other client from accessing guarded data (no process may hold synchronization variable even in non-excl. mode)
		- **Exclusive Access**:
		    - When a client (or process) acquires a synchronization variable (lock) in **exclusive mode**, it gains the sole right to read and write the associated guarded data.
		    - No other client can access the guarded data in any capacity (neither read nor write) until the lock is released.
		- **Preclusion of Other Access**:
		    - During the period when a client has exclusive access, other clients are completely blocked from accessing the guarded data. This ensures that no conflicting operations can occur on the data, maintaining consistency.
		- **Non-Exclusive Mode**:
		    - Typically, a synchronization variable might allow non-exclusive (read) access, where multiple clients can read the data simultaneously but cannot write to it.
		    - However, in the context of entry consistency with exclusive access:
		        - Even non-exclusive (read) access is prohibited if another client holds the lock exclusively.
		        - This means that while a client has exclusive access, no other client can even read the guarded data.
- **release(S)**
	- Relinquish exclusive access
![[Pasted image 20240614202556.png]]
#### Type of consistency models
![[Pasted image 20240614203049.png]]
### Use cases
**NoSQL**: Not-Only SQL or Non-Relational SQL
- New generation of databases 
- Increasing availability 
- Often distributed 
- Looser consistency models

Different products, with different consistency models
- Strict consistency
	![[Pasted image 20240614203209.png]]
- Sequential consistency
	![[Pasted image 20240614203223.png]]
### Client-centric consistency models
**Focus on how the users see the data**
#### Why?
- Number of reads >> number of writes
- No write-write conflicts or easy to resolve 
- Data items have an **owner** 
- Suitable for environments with unreliable network connectivity and limited network performance
![[Pasted image 20240614221719.png]]

**Example:** Facebook
![[Pasted image 20240614221818.png]]
#### Notation
![[Pasted image 20240614222026.png]]
#### Monotonic-Read Consistency 
**Definition:** If a process reads the value of a data item x, any successive read operation on **x** by that process will always return that **same or a more recent value**.

**Intuition**: Client “**sees**” only same or newer version of data.
![[Pasted image 20240614223234.png]]
- **Monotonic Reads**:
    - Ensures a consistent and non-decreasing sequence of reads for a process.
    - If a process reads a newer value, it will never read an older value afterward.
- **No Monotonic Reads**:
    - No such guarantees. A process can read older values even after having read newer values.
    - This can lead to inconsistencies in the view of the data for the process.
##### Examples
1. Automatically reading your personal calendar updates from different servers.
	- Monotonic Reads guarantees that the user sees all updates, no matter from which server the automatic reading takes place.
2. Reading (not modifying) incoming e-mail while you are on the move.
	- Each time you connect to a different e-mail server, that server fetches (at least) all the updates from the server you previously visited.
3. DNS System
	- Once you see the update of a DNS entry, you never see the old one.
#### Monotonic-Write Consistency
**Definition**: A write operation by a process on a data item x is completed before any successive write operation on x by the same process. In other words, once a process writes to a data item, it cannot write to that data item again until the first write has been completed and acknowledged.

**Intuition**: Write happens on a copy only if it’s brought up to date with preceding write operations on same data (but possibly at different copies)
![[Pasted image 20240614224108.png]]
- **Monotonic Writes**: Ensures that a subsequent write on the same data item by the same process only happens after the previous write is completed. This maintains a consistent write order and avoids conflicts or inconsistencies.
- **No Monotonic Writes**: Does not guarantee that the previous write is completed before initiating a new write. This can lead to inconsistencies or conflicts, as the newer write might overwrite or interfere with the previous one before it’s completed.

**Examples**
- Software version control: always update before committing changes.
#### Read-Your-Writes Consistency
**Definition**: The effect of a write operation by a process on data item x, will always be seen by a successive read operation on x by the same process. 

**Intuition**: All previous writes are always completed before any successive read
![[Pasted image 20240614224719.png]]

**Examples**
- Password databases 
- Update of web page immediately pushes new version to caches
#### Writes-Follow-Reads Consistency
**Definition**: A write operation by a process on a data item x following a previous read operation on x by the same process, is guaranteed to take place on the same or a more recent value of x that was read. 

**Intuition**: Any successive write operation on x will be performed on a copy of x that is same or more recent than the last read.
![[Pasted image 20240614224823.png]]

**Examples**
- Comments on a web page, Forum…
### Trade-offs in choosing a consistency model
We can avoid system-wide consistency, by concentrating on what specific clients want, instead of what should be maintained by servers.
1. Consistency and redundancy
	- All copies must be strongly consistent 
	- All copies must contain full state 
	- Reduced consistency leads to reduced redundancy
1. Consistency and performance
	- Consistency induces extra computation and communication 
	- Increased consistency leads to decreased performance
1. Consistency and scalability
	- Scalability depends on the implementation of a consistency model 
		- Avoid centralized approaches 
		- Avoid strong increase in communication