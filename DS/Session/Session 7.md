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
### Strict consistency 
**Identical to single machine execution**

Strongest consistency guarantees 
**Immediate propagation** of all content updates 
Absolute **time ordering** of all shared access operations (global clock) 
A **read returns the last write** given that time ordering
![[Pasted image 20240614173325.png]]
### Sequential consistency
**Relaxation: delay can exist in content updates**
Weaker consistency guarantees than strict consistency
Operations are interleaved in some fixed **order** 
All processes see the **same order**
![[Pasted image 20240614173505.png]]

**Some notation**
![[Pasted image 20240614173659.png]]
#### Exercise
![[Pasted image 20240614173847.png]]
**Answer:** Strict consistency

![[Pasted image 20240614173928.png]]
**Answer:**\
![[Pasted image 20240614173943.png]]

![[Pasted image 20240614174601.png]]
**Answer:**
Let's first look at P3 first. Print x → 12 is done first, that means P2 happened before P3 to set x to 12. Next, we have Print y → 16, this means y is set to 16, so before P3 print, P1 happened. Now, y is set to 10, that could only mean that P2 happened after the previous process. Now the next value is print x → 3, meaning we executed P1 again before this print, because print x → 8, we can assume that P1 finished his process and x remained 8.

Let's look at P4, first we have print x -> 12, meaning that P2 happened before P4. After the print y -> ???, we have print -