# HTTP Status Codes

# Split into 5 categories

# 1. Information Responses (100-199)
# 100 - Continue            : Interim response which indicates that the client should continue or ignore the response
# 101 - Switching Protocols : Sent in response to an upgrade request header from the client
# 102 - Processing          : Indicates request has been received by the server, but no status was avaliable
# 103 - Early Hints         : Intended for use with Link header, letting user agent start preloading resources while server prepares a response


# 2. Successful Responses (200-299)
# 200 - OK                  : The request succeeded. Result of success depnds of HTTP method
# 201 - Created             : The request succed and a new resource was created as a result
# 202 - Accepted            : Request recieved but not yet acted upon
# 203 - NonAuth Information : The returned data isn't exactly the same as origin, but collected from local or third-party copy
# 204 - No Content          : No content to send for this request, but the headers are useful
# 205 - Reset Content       : Tells user agent to reset document which sent the request
# 206 - Partial Content     : This response code is in response to a range request where client requested a part of a resource
# 207 - Multi-Status        : Converys information for multiple resources. Used for situations for multiple resources
# 208 - Already Reported    : Used to avoid repeatedly enumerating the internal members of multiple bindings


# 3. Redirection Messages (300-399)
# 300 - Multiple Choices    : Request has more than one possible response and user agent should chose one
# 301 - Moved Permanently   : URL of the requested resource has been changed permanently. URL is given in the response
# 302 - Found               : URI of requested resource has been changed temporarily.
# 303 - See Other           : Response sent to direct client to different URI to get the requested resource
# 304 - Not Modified        : Tell client the resource hasn't changed, so the client can continue to use the same cached version
# 307 - Temporary Redirect  : Same as 302 FOUND exceot the user agent must not change HTTP method
# 308 - Permanent Redirect  : Same as 301 Moved Permanently except user agent must not change HTTP method


# 4. Client Error Responses (400-499)
# 400 - Bad Request         : Server cannot or will not process request due to percieved client error
# 401 - Unauthorized        : Unauthenticated. Client must authenticate itself to get requested response
# 403 - Forbidden           : Client does not have access rights to resource. Different from 401 because client is already known
# 404 - Not Found           : Server cannot find requested resource. Also possibly a more hidden version for 403 response.
# 405 - Method Not Allowed  : Method known by server but not supported by target resource
# 406 - Not Acceptable      : Server can't find any content that conforms to the criteria given by user agent
# 407 - Proxy Auth Required : Similar to 401 but authentication is needed to be done by a proxy
# 408 - Request Timeout     : Server would liek to shut down this unused connection
# 429 - Too Many Requests   : User has sent too many requests in a given amount of time. (Rate Limiter)


# 5. Server Error Responses (500-599)
# 500 - Internal Server Err : Server encountered a situation it can't handle. No 5XXcode to respond with so 500 it is
# 501 - Not Implemented     : Request method not supported by the server and cannot be handled. GET and HEAD must be supported
# 502 - Bad Gateway         : Server got an invalid response while acting as a gateway
# 503 - Service Unavailable : Server is not ready to handle the request. Server is down for maintenance or is overloaded. User-friendly page sent in response as well
# 504 - Gateway Timeout     : When server is acting as a gateway and can't get a response in time

