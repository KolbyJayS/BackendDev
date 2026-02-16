"""
Three Tier Architecture is a common architecture pattern in web development that  promotes the seperation of concerns.

The Components are as such :
Client -> Route -> Controller -> Service -> Repository -> Database

Client:
    The end-user interface (Typically web browser or mobile application) which sends request to the applications backend. (HTTP)

Route:
    This defines the path or URL that the client calls, routing the request to the proper controller function

Controller:
    This is what recieves the request from the route, validates the data, handles any errors, but delegates the processing
        to the server layer. Also is responsible for returning the final response to the client. No business logic

Service:
    This handles the core business logic and processing which was delegated from the Controller. Orchestrates calls to 
        repositories or other services to fulfill requests.

Repository:
    Acts as abstraction layter for data access layer, encapsulating the logic required to access the data source. Interacts directly
        with the database to perform data operations (Create, Read, Update, Delete) and returns data to the service layer.

Database:
    Persistence layer where app data is stored, managed, and retrieved. This is your SQL or NoSQL Database.

"""


