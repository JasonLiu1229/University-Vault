# Service oriented architecture (SOA's)
Distributed systems can scale to massive services, where 100's or more distributed systems work together for one application, but how do we organize this? 

One example is Twitter, how did Twitter do this? [Twitter monorail](https://iosifache.me/twitter-architecture-trends)
![[Pasted image 20240302175022.png]]
They made use of something like this, where 3 of the 4 services are maintained with something called "Monorail" and the storage part is maintained with MySQL. 

Monorail or a monolithic service, where one service does all the work. This had some weaknesses, of course:
- Storage I/O Bottlenecks
- Poor concurrency, runtime performance
- Too many cooks in the same kitchen, so lots of code for little value
- Lack of clear ownership, because code was done all in one service, there was no good tell who did the most to make the service work properly.
- Too tight coupling

Later on they switched to something like this:
![[Pasted image 20240302175908.png]]
Why did Twitter do this?

They had several reasons, but one big reason is that if one service fails, the rest won't be too much or at all affected. Another reason was that working on one service was easier.
## Tightly vs loosely coupled
### Coupled architectures
- Components are **tightly** linked with each other
- Removing/adding a component is non-trivial
![[Pasted image 20240302180223.png]]![[Pasted image 20240302180228.png]]
### Decoupled architectures
- Components are **loosely** linked with each other
- Removing/adding a component is easier and can happen frequently
![[Pasted image 20240302180313.png]]
This is similar as OO-Design, where we instead of splits in component, we split in objects that do things for us.
## The old days (Distributed computing 1.0)
A **HISTORICAL** distributed system in practice 
A traditional Operating Support System = System for operating a communications network
![[Pasted image 20240302181209.png]]
But this resulted in a stovepipe system. (The Stovepipe System Anti-Pattern is **the single-system analogy of Stovepipe Enterprise, which involves a lack of coordination and planning across a set of systems**.)
![[Pasted image 20240302181306.png]]
Many things could go wrong at any stage.

This lead to a new approach, involving software engineering.
![[Pasted image 20240302181416.png]]
Where we slowly evolved and slowly broke down more things in pieces. This lead to less coupling and fewer problems for others in case something went wrong on your end of the service.
## Distributed computing 2.0
Before we dive in, we need to ask ourselves 2 questions:
- What is service orientation?
- What is an architecture? Or what is not?
### What is a service?
- Physical independent software program
- Loosely coupled
- Distinct design characteristics
- Capabilities are often defined in terms of a contract
**General idea: Service composition and inventory**
![[Pasted image 20240303121347.png]]
#### Coupling of services & value
![[Pasted image 20240303122222.png]]
As we can see on the graph that the value of the services differentiate depending on the amount of coupling we have in our system.

But it is important that we have good "glue", otherwise it has no point that our services are loosely coupled if they can't or don't interact with each other.
#### Example of a SOA application
![[Pasted image 20240303122505.png]]
### What is an architecture? What is it not?
**Service oriented architecture**
- Architecture = **style of design**
	- Enterprise architectural style. Technology neutral!
- Service-oriented: **the core unit of design is a service**
	- Implementing a capability so that it can be easily consumed
- An approach to designing systems, a set of design principles
- A way of thinking about a problem, a mindset

**From a technical perspective**
- An architecture for designing systems
	- A “service” **exposes a discrete capability**
	- Any application that needs the capability uses the service
- A service exposes its capability **via an interface**
- Compared against an application-centric design perspective
	- Monolithic application silos
	- Duplication of functionality
#### Definition
“A **paradigm** for **organizing** and **utilizing distributed capabilities** that may be under the control of different ownership domains. It provides a uniform means to offer, discover, interact with and use capabilities to produce desired effects consistent with measurable preconditions and expectations.”
## Technical aspects
**Service Architecture != Product**
Enterprise Java Beans: Powerful, but Java only

CORBA
- **C**ommon **O**bject **R**equest **B**roker **A**rchitecture
- Independent of OS and language, but very complex
- Limited amount of vendors
- Historical

Web Services
![[Pasted image 20240303141416.png]]
## Why do we need SOA?
- …promotes reusability
- …promotes exchangeability
**Allows multi-tenancy: a single instance of the software runs on a server, serving multiple client-organizations (tenants)**
![[Pasted image 20240303142008.png]]
Multi-tenancy = is **a reference to the mode of operation of software where multiple independent instances of one or multiple applications operate in a shared environment**.
### Types of multi-tenancy
#### Data multi-tenancy
![[Pasted image 20240303143314.png]]
Same application + different conditions on the data
#### Application multi-tenancy
![[Pasted image 20240303143330.png]]
Tenant-configured applications
