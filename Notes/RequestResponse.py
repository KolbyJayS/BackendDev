# HyperText Transfer Protocol

# The standard used for request/response cycle of web apps. The client sends a request to the server. 
# The server sends a response

# HTTP Request comes from the client, where it sends a payload of data to a server as a "request"
# A request is made up of 5 components:

# 1 - HTTP Method : This specifies the type of action to perform
# 5 Most common HTTP Verbs:
# GET       : Retrieve some information to be READ by the client
# POST      : CREATE a new resource with information contained in the request
# PUT       : UPDATE an entire resource with information contained in the request
# PATCH     : UPDATE a part of a resource with information contained in the request
# DELETE    : DESTROY a resource, typically indicatiing that it is removed from the database

# 2 - Endpoint (URL) : Address of the resource on the server
# Examples of a URL Path:
# /tasks
# /tasks/4
# /items/6/reviews


# 3 - Headers : Key-Value pairs which provide additional information about the request (authentication, content type, caching)
# Two Types of HTTP Headers.
# Request : From the Client to the Server
# Response : From Server to the Client 
# Common HTTP Headers:
# Authorization : Used for auth : Authorization Bearer {Access_token}
# Content-Type : Specifies the format of content : Content-Type: application/json
# Accept : Indicates the expected format : Accept: application/json
# User-Agent : Identifies the client : User-Agent: Mozilla/5.0
# Cache Control : Specifies caching policies : Cache-Control: no-cache
# Host : Specifies the domain name : Host: 
# Referer : Indicates referring URL : Referer: <https://example.com>
# Cookie : Sends client cookies : Cookie: session_id=abc123

# Why use HTTP Headers?
#   Authentication, Content Negotiation, Performance Optimization, and Debugging/Analytics
# When to use HTTP Headers?
#   Always use auth for secure API Calls
#   Use Content-type and Accept when sending/recieving structured data (JSON)
#   Use Cache-Control to optimize performance for frequently accessed resources


# 4 - Query Parameter : Optional Key-Value Pairs appended to the URL to filter or modify request
#   Query parameters are appended to the URL after a ? symbol. Multiple parameters are separated by an &
#   Ex : https://api.example.com/resources?filter=active&sort=asc

# Why use Query Parameters?
#   Efficiency : Retrieve only the data you need, reducing response size
#   Flexibility : Customize requests wihtout modifying server side logic
#   Standardization : Query parameters follow a standard format, making them easy to understand


# 5 - Request Body : Contains data sent to the server (used in POST, PUT, or PATCH requests)
#   The format of which is define by the Content-Type Header (XML, Form Data, JSON, Plain text, Raw Bytes)
