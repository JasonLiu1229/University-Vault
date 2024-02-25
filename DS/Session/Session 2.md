# Middleware and communication 
![[Pasted image 20240225144948.png]]
**Middleware the plumbing of distributed systems:**
1. It is mostly invisible
2. Provides a standard way of doing things
3. It ties parts together of complex systems
4. It lets u focus on the core task
### Search in chord
![[Pasted image 20240225150053.png]]
Instead of broadcasting to everyone and asking where is file ...? We make use of a hash table and ask the entity with hash ... where the file is. In case the file is not in the first device, the device will redirect us to another, and this will repeat until the file is found. 
## What are we going to look at today?
![[Pasted image 20240225150324.png]]
1. How to achieve basic communication?
2. Why middleware? 
3. The middleware principle
4. Middleware architecture
### Establishing communication
![[Pasted image 20240225150538.png]]
To establish a communication between two devices, we make use of sockets. Where we call API services to communicate the necessary functionalities between each other. 
#### Sockets
![[Pasted image 20240225150750.png]]
This is a variant of sockets that you might find online. The first three functions of the server is to open his communication to the client. 
##### Sockets in java
Here is an example how it could be done in java.
###### Client
![[Pasted image 20240225151100.png]]
###### Server
![[Pasted image 20240225151132.png]]
#### Remote invocations requires ...
![[Pasted image 20240225151306.png]]
Here are some important points that we need to remember in case we want to invoke remotely. 
### Why middleware? 
![[Pasted image 20240225151459.png]]
#### Hardware and OS architecture
![[Pasted image 20240225151536.png]]
Where the OS architecture of the multi-computer model might look like this:
![[Pasted image 20240225161424.png]]
Where our applications are distributed over systems. 
#### Middleware layers
![[Pasted image 20240225161707.png]]
#### Method invocation for ...
##### Local Objects
**Within one process’s address space** 
###### Object 
- Consists of a set of data and a set of methods. 
- E.g., C++/Java object 
###### Object reference 
- An identifier via which objects can be accessed. 
- i.e., a pointer (C++) 
###### Interface 
- Signatures of methods 
	- Types of arguments, return values, exceptions 
- No implementation 
- E.g., hash table: 
	- insert (key, value) 
	- val
	- ...
##### Remote objects
**May cross multiple process’s address spaces** 
###### Remote objects 
- Objects that can receive remote invocations. 
###### Remote object reference 
- An identifier that can be used globally throughout a distributed system to refer to a particular unique remote object. 
###### Remote interface 
- Every remote object has a remote interface that specifies which of its methods can be invoked remotely 
- Interface Definition Language
#### A Remote Object and Its Remote Interface
![[Pasted image 20240225162357.png]]
The remote objects can interact with other remote object making use of the remote interface. 
#### Remote object references
**Purpose : unique ID for objects in distributed system**
- uniqueness over time
- uniqueness over space
![[Pasted image 20240225162549.png]]
![[Pasted image 20240225162618.png]]
#### Local and remote invocations
![[Pasted image 20240225162642.png]]
Local invocation
- Use Object Reference
- Any public method
- Invocation: exactly once

Remote invocation
- Use Remote Object Reference
- Limited access, remote interface
- Invocation: ???

The amount of invocations is determined by the situation, in case there is a failure during the invocation, could lead to multiple or less invocations then intended.
### Failure Modes of RMI/RPC
![[Pasted image 20240225162814.png]]
Some example of what could go wrong during remote method invocations or remote procedure call. 
### Fault tolerance
**Techniques**:
1. Retry-request message
2. Duplicate request filtering
3. Retransmission of results
	1. Re-executes call
	2. History table of results - Retransmit reply

These are some techniques to prevent this faults, they will determine the following amount of invocations: (Invocation semantics)
1. Maybe
2. At least once
3. At most once
#### ![[Pasted image 20240225163343.png]]
### Role of the middleware…
