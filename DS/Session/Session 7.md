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
