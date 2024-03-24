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

