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
