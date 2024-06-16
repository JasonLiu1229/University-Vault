# Introduction
## What is this course about?
![[Pasted image 20240218161030.png]]
Distributed systems is about how two different processes/systems can work together, how we can allocate recourses appropriately, etc.
## What?
### Informal definition
A distributed system is a collection of independent computers that appears to its users as a single coherent system.
![[Pasted image 20240218180106.png]]
Application can run on multiple computers, with different operating systems. These applications can communicate with each other through an extra layer. This is what we call middleware. Doesn't mean that we work on separate computers that the applications have to be separate, multiple computers can work on one application and communicate through the middleware.

Main key point: Build a powerful system out of many simpler systems. The network is the computer.
## Defining a DS
### Service 
= part of a computer system managing a collection of related resources, presenting their functionality to users and applications.
### Service, Client and server
![[Pasted image 20240218180551.png]]
### Server
= running process on networked computer.
- Accepting requests to perform a service 
- responding appropriately
So when we speak about a server, we talk about the process that is running on the hardware. In case we talk about the hardware, this will be explicitly mentioned. 
### Client
= running process on a networked computer sending service requests to servers.
### Remote invocation
= complete interaction between client and server to process a single request.
![[Pasted image 20240218180842.png]]
There can also be multiple invocation in series.
![[Pasted image 20240218180923.png]]
## Why?
- Cost
	- Networked commodity systems can render the best performance for its price
- Capability
	- Many computational problems are too large for any single system because of memory, data storage, computational requirements
- Concurrency
	- Many ‘large’ problems have inherent options for parallelism 
		- Era of horizontal versus vertical scaling
- Reliability
	- Distributing redundant components minimizes the probability faults impact the user
- Integration
	- For organizations to interact, their systems need to interact Highly specialized infrastructures need to be integrated and shared (e.g. radio telescopes, mass storage facilities, experimental facilities)
		- Overall, integration in distributed systems allows for a more connected and cooperative environment where resources and capabilities can be shared across different systems and organizations, leading to improved efficiency and effectiveness in achieving common goals.
- Distribution
	- E-mail, WWW, … are inherently distributed as users are geographically spread
### Many problems and challenges
- no limit on spatial extent, difficult to manage
- no global time notion
- almost always concurrent execution
- (partial) failures likely to happen
## Logical architecture styles
### Coupled architectures
- Components are **tightly** linked with each other
- Removing/adding a component is **non-trivial**
#### Layered
![[Pasted image 20240218181442.png]]
**Layer only interacts with neighbor**
	\+ reduced number of interfaces, dependencies
	\+ easy replacement of a layer
	\- possible duplication of functionality
#### Object-based
![[Pasted image 20240218181709.png]]
**Interacting objects**
	no predefined interaction pattern
	\+ highly flexible
	\- complex to manage and maintain
### Decoupled architectures
- Components are **loosely** linked with each other
- Removing/adding a component is **easier** and can happen **frequently**
#### Event-based
![[Pasted image 20240218181943.png]]
**Event based interaction**
	“publish-subscribe” style
	\+ Loose coupling of components related: message based interaction (also decoupling in time) often used to integrate legacy systems
	\+ Fault tolerance: because it is decoupled, services that fail causes the others not a big hassle or at least lessens the hassle.
	\+ Fan Out and Less Technical Debt: event-driven architecture is push-based, so if multiple downstream systems need to act based on the occurrence of the event, then the event can be fanned out to these systems in parallel without the need for custom code. This also saves the downstream systems from continuous polling to check for an event occurrence, resulting in **less resource utilization** in terms of network bandwidth, CPU, etc.
	\- Increased complexity
	\- Debugging and troubleshooting more of a problem
	\- Difficulties with monitoring
#### Data-centric
![[Pasted image 20240218182051.png]]
**Data centric architecture**
	only interaction through shared database
	\+ loose coupling of components
	\- possibly slow (central bottleneck, locking, ...)
## System architecture
How is the software architecture instantiated using hardware components? How are the hardware components organized? How to map logical components to actually deployed components (replicated ?, P2P, pure client server, ...)
![[Pasted image 20240218182218.png]]
### Client-server
#### Client-multiserver
![[Pasted image 20240218182310.png]]
#### Proxy server
![[Pasted image 20240218182343.png]]
### Peer-to-peer architecture
Deliver a service that is fully **decentralized** and **self-organizing**
![[Pasted image 20240218182455.png]]
Processes (nodes) organized in an overlay network (virtual network)
- Each node fulfills **both** a **client** and a **server** role (**servant**)
- Nodes and data item keys are assigned **Globally Unique Identifiers** (GUIDs)
- Nodes have no or limited direct knowledge on other nodes
	- Nodes typically have limited or no direct knowledge about the entire network. Instead, they know about a subset of nodes, which helps in scaling the network without overwhelming any single node.
- Application-level message routing
	- Messages and data requests are routed at the application level, meaning nodes handle the routing decisions themselves rather than relying on lower network layers.
- Nodes are **volatile**
	- Nodes in P2P networks are volatile, meaning they can join or leave the network at any time.
- Structured or unstructured
	- **Structured P2P Networks**: Use predefined rules to organize the nodes and manage data (e.g., Chord, CAN).
	- **Unstructured P2P Networks**: Nodes randomly connect to each other without a predefined structure (e.g., Gnutella, BitTorrent).

\+ **Scalability**: Can handle many nodes efficiently due to its decentralized nature.
\+ **Fault Tolerance**: The absence of a central point of failure makes the network resilient to individual node failures.
\+ **Resource Sharing**: Efficiently utilizes the resources of all nodes, distributing the load evenly.