# Microservices
## Traditional way
So when we design an app or service, this can be done in multiple ways. One way is to split our component in layers/flows/features. In case our app needs to scale hardware wise, we can replace components, add components horizontally or vertically. This method is only applicably to a certain level.
![[Pasted image 20240401123811.png]]
## Service concept
![[Pasted image 20240401123824.png]]
Where we turn every set of flows in to a service and let those service interact with each other.

This is more scalable because we only have to scale a single service instead of scaling the whole application.
## Service Oriented Architecture
Software architecture design pattern based on **distinct pieces** of software providing application **functionality as services** to other applications.

We do this until this ends up with monoliths again. So indicating we get similar problems as before but now with fat services.
![[Pasted image 20240401132907.png]]

Now we see services as the new monolithic entities, but this does not solve our issue. 

So let's design based on scalability in mind.
![[Pasted image 20240401133117.png]]
This introduces us to the concept of **microservices**. 
Designing our application as loosely-coupled microservices:
- Small functional granularity organized around capabilities
- Lightweight communication protocols
- Independently deployable and replaceable
## Definition
A way of designing software applications as suites of **independently deployable services**.
## From monolithic application to suites of services
![[Pasted image 20240401153458.png]]
### Definition
**Microservice architectural style**
- Approach to developing a single application as a suite of small services
	- Each running in its own process
	- Communicating with lightweight mechanisms (e.g. REST or message queues)

**Micro-Services**
- Built around business capabilities
- Independently deployable by fully automated deployment machinery
- Bare minimum of centralized management
- Written in different programming languages
- Using different data storage technologies
## Componentization via services
- Component
	- Unit of software that is independently replaceable or upgradeable
		- Libraries = linked into a program
		- Services = out-of-process component
- So why choose services over libraries?
	- Services are independently deployable
	- Changes in libraries = redeploying entire application
	- Explicit (remote) component interface when using services
- Services require more coarse-grained interfaces
	- Remote calls more expensive than in-process calls
## Smart services, dumb pipes
This means designing systems where the services are intelligent, handling complex logic and processing, while the communication channels between them are simple and efficient.
- Enterprise Service Bus (ESB)
	- Sophisticated message routing, choreography, transformation and business rule application
- Microservices
	- Act more as filters: receive request, apply logic, produce response
- Most commonly used protocols
	- REST (versus WS-Choreography, BPEL)
	- Reliable messaging over lightweight bus (Kafka, RabbitMQ, ZeroMQ, …)
## Decentralized governance
- Each service picks the right technology
	- In a decentralized approach, each microservice can choose the most suitable technology stack (programming languages, frameworks, databases) that best fits its specific needs. This flexibility allows for optimizing performance, scalability, and development speed.
- Service contracts define the interfaces
	- Microservices communicate with each other through well-defined interfaces, known as service contracts. These contracts ensure that the services can interact seamlessly, even if they are built with different technologies.
- Allows for different conceptual models, even of the same entity
	- e.g. “customer” is different for sales than it is for support department
- Polyglot persistence
	- This means using different types of databases for different services based on their specific needs. For instance, some services might use relational databases, others might use NoSQL databases, and others might use in-memory databases.
- Transaction-less so cope with eventual consistency
	- Unlike monolithic systems that rely on ACID transactions for consistency, microservices often use eventual consistency. This means updates propagate over time, and the system will become consistent eventually, rather than immediately. This approach suits the distributed nature of microservices, enhancing performance and availability.
![[Pasted image 20240401170546.png]]
## Organized around business capabilities
![[Pasted image 20240401170706.png]]
Identifying business capabilities and hence services requires an understanding of the business. An organization’s business capabilities are identified by analyzing the organization’s purpose, structure, business processes, and areas of expertise. Bounded contexts are best identified using an iterative process. 
## Continuous delivery automation
- Continuous integration
	- Integrating, building and testing code within the development environment
- Continuous delivery
	- Software can be released to production at any time
- Continuous deployment ~
	- Software is automatically pushed into production

- Automated tests ran at each stage of delivery.
- Deployment pipeline tools near-mandatory.
![[Pasted image 20240401183120.png]]
## Products, not projects (aka DevOps)
“The traditional model is that you take your software to the wall that separates development and operations, throw it over and then forget about it. Not at Amazon. You build it, you run it.”

The quote advocate for a DevOps culture where developers are accountable for the operational aspects of their software, leading to better quality, faster delivery, and a more collaborative environment. This approach shifts the mindset from treating software development as a series of isolated projects to managing it as a continuous product lifecycle.
# [Reactive manifesto]( www.reactivemanifesto.org)
The Reactive Manifesto outlines the principles of building responsive, resilient, elastic, and message-driven systems. It was created to address the challenges faced by traditional software architectures in the face of modern demands such as high concurrency, scalability, and resilience
- Aims to condense knowledge on how to design highly scalable and reliable applications
	- Set of required architecture traits
	- Common vocabulary, technology-agnostic
- Why? 
	- Because today's demands are simply not met by yesterday’s software architectures
		- Large applications a few years ago
			- >10 servers, response time: seconds, hours of offline maintenance, gigabytes of data
		- Today
			- Deployed on everything from mobile devices to cloud-based clusters running thousands of multicore processors, response time: milliseconds. Petabytes of data.
![[Pasted image 20240401184935.png]]
- **Responsiveness** is the cornerstone of usability. Systems should ensure low latency, quick responses, and maintain interactivity. This involves handling requests promptly and delivering timely feedback to users, which improves the overall user experience.
- **Resilience** is achieved through replication, containment, isolation, and delegation. By isolating failures, the system can contain them and avoid cascading effects. Components can fail and recover without affecting the overall system’s responsiveness.
- **Elasticity** involves the ability to scale up or down based on the current load. Systems can dynamically adjust resources to handle changes in traffic or data volume, ensuring consistent performance and responsiveness regardless of the load.
- **Asynchronous communication** through messaging allows components to interact without being directly dependent on each other. This approach decouples system components, leading to more manageable, scalable, and resilient architectures. **Message-driven** systems often utilize techniques like event sourcing and CQRS (Command Query Responsibility Segregation).
## Architectural trait: message driven
- Asynchronous message-passing between components
	- Addressable recipients await the arrival of messages and react to them
	- Establishes a boundary that enables
		- Loose coupling
		- Isolation
		- Location transparency
- Enables load management, elasticity and flow control by monitoring and shaping the message queues in the system
	![[Pasted image 20240401185101.png]]
## Architectural trait: responsive
- The system responds in a timely manner (aim: 0.1 seconds)
	- Client side lazy loading: first load important stuff and show it ASAP
	- Show progress
	- Individual slow performing service should not slow down others

As far as users know, when the response time exceeds their expectation, the system is down
## Architectural trait: elastic
- System stays responsive under varying workload
	- Changes in input rate lead to increased or decreased resource allocations
	- No contention points or central bottlenecks
	- Distribution of input amongst components
- An elastic system can allocate / deallocate resources for every individual component dynamically to match demand
- Predictive and reactive elastic scaling
## Architectural trait: resilient
- Any service call can fail
- Detect failures quickly by monitoring
	- Service metrics (e.g. requests per second)
	- Business metrics (e.g. orders per minute received) and automatically restore services when issues are detected
- Provide fallback services
	- E.g. Netflix graceful degradation
		- If recommendation service is down, revert to most popular movies instead of personalized picks
### Resilient to failure: Netflix’s Simian Army
- Chaos Monkey
	- Introducing random failures in their production AWS services
	- Team of engineers ready to intervene
- Latency Monkey
	- Introducing artificial delays
- Janitor Monkey
	- Seeks unused resources and disposes of them
- Security Monkey
	- Seek misconfigured services / security issues

The best defense against failures is to fail often, forcing your services to be built in a resilient way.
# Microservice frameworks
There are many different frameworks for different languages and different use cases.
## Containers as a microservice enabler
- Virtual machines (VMs)
	- Virtualization of hardware.
	- Flexible, robust and safe, but big performance hit
- Containers
	- Lightweight 
	- Better use of resources (sharing host OS and potentially binaries/libraies)
### Pros and cons of containers
- Pros
	- No performance hit due to emulation of instructions
	- Flexibility
		- containerize a “system”
		- containerize “application(s)”
	- Lightweight
		- no entire OS in each container
		- sharing of bins and libraries 
		- provisioned/instantiated in milliseconds to seconds 
		- minimal per-container penalty 
		- “Just Enough OS” on the server (e.g. CoreOS)
- Cons
	- Cannot host a guest OS different from the host one*
	- Weaker isolation and thus security
### Container checklist
The "Container Checklist" refers to a set of considerations and configurations important for managing and deploying containers in distributed systems.
- Processes 
- Throttling/limits 
- Prioritization 
- Resource isolation 
- Root file system 
- Security
$\rightarrow$ Focus on Linux Containers (LXC) to explain the basics
## Linux Control Groups (cgroups)
- Problem
	- How do I throttle, prioritize, control and obtain metrics for a group of tasks (processes)?
- Solution: Linux control groups (cgroups)
	- cgroups (abbreviated from control groups) is a Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, disk I/O, etc.) of a collection of processes.

- Device Access 
- Resource limiting: memory, CPU, devices, block I/O, etc.. 
- Prioritization: who gets more of the CPU, memory 
- Accounting: resource usage per group 
- Control: freezing and check pointing 
- Injection: packet tagging
### Subsystems
![[Pasted image 20240401192607.png]]
### CPU control
- Use CPU shares (and other controls) to prioritize jobs / containers
- Carry out complex scheduling schemes 
- Segment host resources 
- Adhere to SLAs (service level agreements)
	- It refers to a document that outlines a commitment between a service provider and a client, including details of the service, the standards the provider must adhere to, and the metrics to measure the performance.
- Pin containers / jobs to CPU cores 
	- Reduce core switching cost
### Device access
- Limit device visibility
	- isolation 
- Implement device access controls 
- Secure sharing 
- Segment device access 
- Device whitelist / blacklist
### Container enabler: cgroups
![[Pasted image 20240401194408.png]]
## Linux namespaces
- Problem
	- How do I provide an isolated view of global resources to a group of tasks (processes)?
- Solution 
	- Namespaces
		- Create abstraction of a system resource and make it appear as a separated instance to processes within a namespace

- MNT; mount points, files systems, etc. 
- PID; processes 
- NET; NICs, routing, etc. 
- IPC; System V IPC 
- UTS; host and domain name 
- USER; UID and GID
	![[Pasted image 20240401194533.png]]
### Conceptual overview
![[Pasted image 20240401194558.png]]
### Container enabler: namespaces
![[Pasted image 20240401194619.png]]
## Changing root
- Problem
	- Give each process the illusion that it is mounted from the root directory
- Solution
	- pivot_root command duplicates entire root directory in MNT namespace
### Container enabler: separate filesystem from root
![[Pasted image 20240401194725.png]]
## Secure containers
- Problem
	- Hostile process can break out of container since entire system is not in a namespace or is containerized 
	- Some namespaces have leaks 
		- If kernel has exploits, the container can exploit these too
- Solution
	- Linux Security Modules (LSM)
		- Mandatory access control
		- Define capabilities per process (system call access)
### Container enabler: Linux security modules
![[Pasted image 20240401194914.png]]
# Related technologies
![[Pasted image 20240401194929.png]]
## Lightweight OS
- Lightweight OS's being developed focused on container-usage, some popular ones:
	- CoreOS (focused on server containers) 
	- Red Hat Project Atomic (focused on server containers) 
	- Ubuntu Core / Snappy (focused on IoT) 
	- Microsoft Nano Server (focused on server containers)
## Container management
There are many management applications to help manage containers, a popular one is Kubernetes.
# Bringing it all together…. How do you build a future proof distributed architecture?
## Architectural view
![[Pasted image 20240401195240.png]]
## Deployment view
- Step 1: Choose which technology & platform is most suited for each microservice 
- Step 2: Package each service in a container 
- Step 3: Let Kubernetes manage the containers 
	\+ setup scaling rules 
- Step 4: Deploy them on your cloud or infrastructure
	![[Pasted image 20240401195322.png]]
