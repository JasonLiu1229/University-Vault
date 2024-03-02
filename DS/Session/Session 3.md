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
This is similar as OO-Design, where we instead of splits in component, we splits in objects that do things for us.
## The old days
