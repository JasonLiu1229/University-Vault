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
## O