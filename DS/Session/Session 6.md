# Distributed storage
## Algorithmic complexity
There were many algorithms that could be applied to have good storage, but these resulted in many problems.

**Cons:**
- page fault 
- cache miss 
- memory access 
- disk access (swap space) 
- network fetch 
- communication between workers
## Moore's law
It states how our hardware needs to grow over the years.
![[Pasted image 20240418140233.png]]

Till 2005 we wanted faster execution of the programs, but after a while this was not possible anymore because of physical limits. Afterwards parallel execution was the main priority.

**Why?**
- Atomic boundaries
- Speed of light
- limited 3D layering
-> Paradigm Shift
## Basics of parallel processing
Now we introduce Hadoop.
### What is Hadoop?
Apache top level project, open-source implementation of **frameworks for reliable, scalable, distributed computing and data storage.**

It is a flexible and highly-available architecture for large scale computation and data processing **on a network of commodity hardware.**
### Google clusters
- 1000 individual machine failures 
- 1000’s of disk failures 
- 1 PDU failure (~500-1000 machines disappear for ~6 h) 
- 20 rack failures (40-80 machines disappear for 1-6 hours) 
- 5 racks go wonky (40-80 machines see 50% packet loss) 
- 3 router failures (have to immediately pull traffic for 1h) 
- ...

Most large jobs see failures and **NO** we are not smart enough to program around it.
### Google MapReduce
A framework for processing LOADS of data
- Framework’s job: fault tolerance, scaling & coordination
- Programmer’s job: write program in MapReduce form

So Hadoop is
- Big data storage
- and Big data processing
### HDFS (Hadoop Distributed File System)
Steps:
- We have a certain file
- It splits it into blocks of certain size
- It will store 3 copies of each block
- Stores these blocks on datanodes
- It distributes the blocks to the DNs

In case a datanodes dies, this will not result in to a problem because the blocks are stored over several datanodes.

Now the Namenode will let the other datanodes know that a datanode died, now it needs to copy the lost data so we have 3 copies again of every block.

![[Pasted image 20240418141522.png]]
### MapReduce
Model for distributed processing

Mantra:
	Move the computation to the data
In practice this means running the processing on a machine whose HDFS Datanode holds the data.
### Hadoop Architecture 
![[Pasted image 20240418141646.png]]

We have a backup of the monitory node (secondary NN), just in case the main one fails. 

Client contacts the Job Tracker. It will check if the racks has the data, if so it will contact the task tracker and check if it can process this data. If not it will contact his neighbor Datanodes until it succeeds. If it still fails, it will contact the other racks until it succeeds.
### Hadoop MapReduce
Data in the form of a <key, value> pair
- <byte, text> 
- <user id, user profile> 
- <timestamp, log entry> 
- <user id, list of user id’s of friends> 
- …

Inspired by list processing (Lisp) , functional programming:
- immutable data 
- pure functions (no side effects): map, reduce

Simple model = easy to reason about
### Google MapReduce
**Map**: map each <key, value> of input list onto 0, 1, or more pairs of type <key2, value2> of output list
![[Pasted image 20240418142344.png]]
**Behaviour**: 
- Map to 0 elements in the output → filtering 
- Map to +1 elements in the output → distribution

**Reduce**: combine the <key, value> pairs of the input list to an aggregate output value
![[Pasted image 20240418142502.png]]

**Bringing it together:**
![[Pasted image 20240418142529.png]]
### What you need to write
**Mapper: application code** 

Partitioner: send data to correct Reducer machine 

Sort: group input from different mappers by key 

**Reducer: application code**
![[Pasted image 20240418142712.png]]
### Hadoop Architecture Overview