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

A socket is an endpoint of a distributed communicating machine that uses sockets to implement the client-server model and solve different network applications. The distributed communication requires two sockets provided as two endpoints: one in the client and one in the server.
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
It provides functionality to connect applications intelligently and efficiently so that you can innovate faster. Middleware acts as a bridge between diverse technologies, tools, and databases so that you can integrate them seamlessly into a single system.
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
- uniqueness over time, so it stays unique over time and will be unique over a long time interval.
- uniqueness over space, it will stay unique across the entire distributed system.
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

The amount of invocations is determined by the situation, in case there is a failure during the invocation, could lead to multiple or less invocations than intended.
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
1. When no fault tolerance measures are applied, the system does not guarantee the execution of the remote method. The invocation might succeed or fail depending on the state of the network and the remote server.
2. The system ensures that the remote method is executed at least once. If an acknowledgment is not received, the request is retransmitted. However, without duplicate filtering, this can result in the method being executed multiple times if the retransmitted requests are processed again.
3. The system ensures that the remote method is executed at most once. Retransmissions are used if no acknowledgment is received, but duplicate filtering ensures that the method is not executed more than once. Instead of re-executing the procedure, the old reply is retransmitted, providing a strong guarantee against multiple executions.
### Role of the middleware…
**Hide all these underlying complexity: provide transparency**
make invocation syntax similar to local invocation, hiding:
- Locate/contact remote object
- Marshalling: converting arguments to bit stream
- Fault tolerance measures
- Communication details (sockets)

**BUT ...**
Not everything should be hidden ...
- Programmer should know object is remote (network latency, potential invocation semantics, additional failures) **!!!!**

→ Typical approach:
- same invocation syntax (but catch exceptions ...)
- Use of remote interface reflects remoteness
## Middleware Architecture
### Proxy and Skeleton in Remote Method Invocation
![[Pasted image 20240225164835.png]]
#### Proxy
Is responsible for making remote method invocation transparent to clients by behaving like a local object to the invoker. 

The proxy implements (Java term, not literally) the methods in the interface of the remote object that it represents. But, …

Instead of executing an invocation, the proxy forwards it to a remote object:
1. Marshals a request message
	- Target object reference
	- Method ID
	- Argument values
1. Sends request message
2. Unmarshals reply and returns to invoker
![[Pasted image 20240225203415.png]]
**Skeleton = reverse of proxy at server side**
#### Marshalling
= transform object in memory to bitstream

Marshalling is the process of transferring and formatting a collection of data structures into an external data representation type appropriate for transmission in a message.

![[Pasted image 20240225205011.png]]
**Options**
- marshalling using external standard
	= External Data Representation e.g. CORBA’s common data representation (CDR) Java serialization Google Protocol Buffer
- marshalling using sender standard AND send this standard along
#### Communication Module
- Implements the invocation semantics
- Runs a request-reply protocol
- Ensures communication between proxy & server-side
![[Pasted image 20240225205217.png]]
#### Dispatcher
- The dispatcher receives all request messages from the communication module.
- For the request message, it uses the method id to select the appropriate method in the appropriate skeleton, passing on the request message.
![[Pasted image 20240225205331.png]]
#### Skeleton
Is responsible for making RMI transparent to **servers** by behaving like a **local invoker** to the **object**.

The **skeleton** ...
1. Accepts a request message
2. Unmarshals the request
	- Target object reference
	- Method ID
	- Argument values
3. Invokes the method on the server object
4. Marshals reply and returns to proxy
![[Pasted image 20240225205609.png]]
#### Remote Reference Module
Is responsible for translating between local and remote object references and for creating remote object references.
Has a remote object table:
- **Server-side:** An entry for each remote object held by any process. E.g., B at host B.
- **Client-side:** An entry for each local proxy. E.g., proxy-B at host A
![[Pasted image 20240225213025.png]]
#### Binding Service
How do you get the initial reference?
**Option 1) Contact the server:**
- Go to the server and ask for the name
- What if multiple processes are running of the same class?
**Option 2) Contact a Binding Service**
- Dictionary service for Middleware
- Or DNS system for RPC
- ![[Pasted image 20240225213147.png]]
#### Do I need to write all this code?
NO! Generated by middleware … based on IDL
![[Pasted image 20240225213219.png]]
### Putting it all together
![[Pasted image 20240225213235.png]]