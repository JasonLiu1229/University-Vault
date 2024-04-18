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
![[Pasted image 20240418143810.png]]

**Components:**
- **MapReduce Framework**: implement MapReduce paradigm 
- **Cluster**: host machines (nodes).
- **HDFS federation**: provides logical distributed storage. 
- **YARN Infrastructure**: assign resources (CPU, memory, etc.=
### YARN 
#### Infrastructure
**Yet Another Resource Negotiator**
- Resource Manager (1/cluster): assign cluster resources to applications 
- Node Manager (many/cluster): monitor node 
- App Master: app (MapReduce) 
- Container: task (map, reduce, …)
#### Application lifecycle
1. Client submits app 
2. RM allocates AM container 
3. AM registers with NM 
4. AM requests containers from RM 
5. AM tells NM to launch containers 
6. Application code is executed 
7. Monitor app status in RM/AM 
8. AM unregisters with RM

![[Pasted image 20240418144326.png]]

Application developers only need to write code for 6.
### Multithreading
In theory it sounds nice, but in practice this is not always perfect.
### Shotcoming of MapReduce 
Forces your data processing into **MAP** and **REDUCE** 
- Other workflows missing include join, filter, flatMap, groupByKey, union, intersection, … 

Based on “Acyclic Data Flow” from Disk to Disk (HDFS) 
- Not efficient for iterative tasks, i.e. Machine Learning 

Only for Batch processing 
- Interactivity, streaming data
### Hadoop and disks
Hard drive access is killing performance and blocking functionality
#### Solution
**Apache Spark**

**Works on top of Hadoop**, HDFS, ……

**Has many other workflows**, i.e. join, filter, flatMapdistinct, groupByKey, reduceByKey, sortByKey, collect, count, first… (around 30 efficient **distributed operations**)

**In-memory caching of data** (for iterative, graph, and machine learning algorithms, etc.)

Spark makes use of memory instead of disk.
![[Pasted image 20240418150939.png]]
#### Sort competition
Spark is 3x times faster with 1/10 the nodes.
#### Logistic regression performance
![[Pasted image 20240418151109.png]]
Spark needs less time.
### Apache Spark
Apache Spark supports data analysis, machine learning, graphs, streaming data, etc. 

It can read/write from a **range of data types** and allows **development in multiple languages.**
![[Pasted image 20240418151243.png]]
### Resilient Distributed Datasets (RDDs)
Immutable distributed collection of objects 

All Spark components use RDDs 

Use transformations to create new RDDs 
- From storage 
- From other RDDs 

Fault tolerant
### DataFrames & SparkSQL
Organize the data in named columns 
Similar to a relational database… 
- Immutable once constructed 
- Enable distributed computations

How to construct Dataframes 
- Read from file(s) 
- Transforming an existing DFs
- Parallelizing a python collection list 
- Apply transformations and actions
### RDDs vs. DataFrames
- RDDs provide a **low level interface** into Spark 
- DataFrames **have a schema** 
- DataFrames are **cached and optimized by Spark** 
- DataFrames are **built on top of the RDDs and the core Spark API**
### Directed Acyclic Graphs (DAG)
DAGs track dependencies (also known as Lineage ) 
- nodes are RDDs 
- arrows are Transformations

**Why?**
- Program resonates with humans and computers 
- Improvement via: 
	- Sequential access to data 
	- Predictive processing
### Narrow Vs. Wide transformation
![[Pasted image 20240418152351.png]]
Narrow: required elements for computation in a single partition live in the single partition of parent RDD

Wide: required elements for computation in a single partition may live in many partitions of parent RD
#### Spark workflow
![[Pasted image 20240418152422.png]]
#### Main use cases
- Streaming Data 
- Machine Learning 
- Interactive Analysis 
- Data Warehousing 
- Batch Processing 
- Exploratory Data Analysis 
- Graph Data Analysis 
- Spatial (GIS) Data Analysis 
- And many more
#### When not to use
Even though Spark is versatile, that doesn’t mean Spark’s in-memory capabilities are the best fit for all use cases: 
- For many simple use cases Apache MapReduce and Hive might be a more appropriate choice 
- Spark was not designed as a multi-user environment 
- Spark users are required to know that memory they have is sufficient for a dataset 
- Adding more users adds complications, since the users will have to coordinate memory usage to run code

![[Pasted image 20240418152631.png]]