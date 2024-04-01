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
