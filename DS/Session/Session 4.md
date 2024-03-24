# Web services
## Definition
"A Web service is a software system designed to support interoperable machine-to-machine interaction over a network"
![[Pasted image 20240324170336.png]]
**Intuition:** access a service using the web
Interaction through messages with a standardized format (HTTP/XML)
Focus is on exposing functionality to third parties (read & writes)
**No one-size-fits-all underlying technology:** SOAP, REST, etc.
## A more detailed definition
"A Web service is a software system designed to support **interoperable machine-to-machine interaction** over a network. It has an interface described in a machine-processable format (specifically WSDL). Other systems interact with the Web service in a manner prescribed by its description using SOAP or RESTful messages, typically conveyed using HTTP with an XML or JSON serialization **in conjunction with other Web-related standards.**"

**Key elements:**
- Machine-to-machine interaction
- Interoperable (with other applications and services) 
- Machine-processable format

**Key technologies:**
- SOAP, REST: used for communication 
- WSDL (Web Services Description language; XML-based)
## Benefits of Web Service
- **Loose Coupled Design**
	Each service exists **independently** of the other services that make up the application. Individual pieces of the application to be **modified without impacting** unrelated areas.
- **Ease of Integration**
	Data is isolated between applications. Web Services **act as glue** between these and enable easier communications within and across organizations.
- **Service Reuse**
	Takes code reuse a step further. A specific function within the domain is only ever **coded once and used over and over** again by consuming applications.
# REST
- **RE**presentational **S**tate **T**ransfer
- Capture **key** characteristics and **principles of the Web** in an **architectural style**
## Introduction
Representational state transfer (REST) is a style of software architecture for distributed systems such as the World Wide Web.

**It’s an architectural style not a protocol**

**Resource is a central concept**
= Any item of interest identified by some identifier
- National Product of Belgium in 2012, Maximum Flow algorithm, Kill Bill 2
- http://www.gambling.com/bets?horse=bigbrown&jockey=ken

![[Pasted image 20240324193136.png]]

**Identifier is a Uniform Resource Identifier (URI)**
- Can be URL, URN or both
- Uniform Resource Locator: 
	The location where you can find the resource, method for finding it
- Uniform Resource Name 
	Defines an item identity
## URI design
- **Remember:** REST is an architectural principle – not a protocol
- Anyone can claim that his API is RESTful
- A few design principles you need to stick to

**REST URI design: how are REST resources described?**
- Describe resources, not applications 
- Non-restful URIs: 
	- /admin/updatebook.jsp?book=5 
	- bookview.jsp?book=5 
	- /bookandreviews.jsp?book=5 
- Make it short: https://www.flickr.com/services/api/rest 
- Hackable up the tree: 
	- uantwerp/courses/computer-science/master/distributed-computing 
	- Uantwerp/courses/ 
- Meaningful: • http://ua.ac.be/main.aspx?c=jose.oramas https://www.uantwerpen.be/en/staff/jose-oramas/ 
- Predictable, human-readable 
- Nouns, not verbs 
- Permanent 
- Query arguments are only for parameters 
- Avoid extensions
## REST and RESTful and HTTP
- REST principles were used for designing HTTP 1.1
- REST was initially described with HTTP in mind 
- REST is often linked with HTTP 
- But REST on top of application layers is also possible

**RESTful API:**
Web Service API that adheres to the REST style, meaning
- It has a base URI, such as http://example.com/resources/ 
- It has an Internet media type for the data. 
- It uses standard HTTP methods 
- It uses hypertext links to reference state 
- It uses hypertext links to reference related resources
## It has an Internet media type for the data
This can be everything: XML, Atom, images, etc.

Often used: JSON

**JSON:** JavaScript Object Notation 
- Open Standard • Human-Readable text 
- Alternative to XML 
- Language-independent 
- Support in many programming languages

JSON has...
- The ability to define a schema for validation 
- Its own RPC system (web service)
## It uses standard HTTP methods
REST uses HTTP methods GET, PUT, POST and DELETE to modify / access resources

According to CRUD: all major functions that are implemented in databases
- **C**reate HTTP PUT or HTTP POST 
- **R**ead HTTP GET 
- **U**pdate HTTP PUT 
- **D**elete HTTP DELETE
## REST architectural constraints
1. **Interface uniformity between components**
	They need to speak the same language and know what to expect in order to understand each other.
2. **Client-server model (separation of concerns)**
	Client and server are fully decoupled and can be developed independently
3. **Stateless client-server communication**
	Each request from client to server must contain all the information necessary to understand the request, and cannot take advantage of any stored session state on the server
4. **Caching**
	Clients can cache responses to requests, improving scalability and performance. The fact that responses are not cache-able should be implicitly or explicitly defined.
5. **Layering**
	A client cannot tell if it is directly connected to a server or to some intermediary (proxy, cache, tunnel, firewalls, …). This allows for load-balancing, fail-over and data transformation.
6. **Code-on-demand (optional)**
	Client functionality can be dynamically extended through the transfer of executable code (e.g. JavaScript)
## REST vs RPC
**RPC (and Distributed Object Systems, SOAP Web Services)**
- Many operations, few URI
- Address software components
- Procedure name and parameters are transferred\

**REST**
- Few operations, many URI
- Address resources
- Resource representations are transferred
# SOAP WEB SERVICES
**Requirements:**
- Text protocol: needs to be readable on the wire 
- Object oriented: needs to describe components of a service
## The SOAP principle
![[Pasted image 20240324212743.png]]
## Interaction protocol = SOAP
**Simple Object Access Protocol**
- W3C Standard (originated from Microsoft)
- Promoted as right style for Web Services
- Rich feature set
- Older than REST
- Still very popular

**Typical use**
![[Pasted image 20240324213028.png]]
## Unlike REST, SOAP is only linked with XML
- Message **format** and **processing rules**
- Stateless and one-way
- Can be used to develop more complex “conversations” 
- Significant overhead XML-is “human-readable” argument?

**Why XML?**
One level above XML RPC
- Adds processing and extensibility models to the story 
- Style for exchanging arbitrary data
It was the de facto standard in human-readable text back then
## SOAP Messages
![[Pasted image 20240324213354.png]]
**Envelope is root element of a SOAP message and contains**
- An optional SOAP header: for extensions (see later) 
- SOAP body: can be anything
## WSDL
**Web Services Description Language**
- XML **grammar to specify collection of “access end points”** 
	(1 URL specifies a single access end point) 
- Designed to automate application-to-application interaction (or B2B interaction) 
- Defines the communication protocol to be used at runtime 
	- Message format 
	- Methods to be invoked 
	- Parameter lists, return types 
	- … 
- WSDL descriptions can be automatically generated for existing code 
- Stub classes can be generated from WSDL descriptions
