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
	- remote calls more expensive than in-process calls
## Smart services, dumb pipes
- Enterprise Service Bus (ESB)
	- Sophisticated message routing, choreography, transformation and business rule application
- Microservices
	- Act more as filters: receive request, apply logic, produce response
- Most commonly used protocols
	- REST (versus WS-Choreography, BPEL)
	- Reliable messaging over lightweight bus (Kafka, RabbitMQ, ZeroMQ, …)
## Decentralized governance
- Each service picks the right technology
- Service contracts define the interfaces
- Allows for different conceptual models, even of the same entity
	- e.g. “customer” is different for sales than it is for support department
- Polyglot persistence
- Transaction-less so cope with eventual consistency
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
# [Reactive manifesto]( www.reactivemanifesto.org)
- Aims to condense knowledge on how to design highly scalable and reliable applications
	- Set of required architecture traits
	- Common vocabulary, technology-agnostic
- Why? 
	- Because today's demands are simply not met by yesterday’s software architectures
		- Large applications a few years ago
			- >10 servers, response time: seconds, hours of offline maintenance, gigabytes of data
		- Today
			- Deployed on everything from mobile devices to cloud-based clusters running thousands of multi-core processors, response time: milliseconds. Petabytes of data.
![[Pasted image 20240401184935.png]]
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
## Resilient to failure: Netflix’s Simian Army
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
