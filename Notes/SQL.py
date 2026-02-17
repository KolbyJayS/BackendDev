"""

SQL (Structured Query Language)
    Also referred to as Relational Database Management Systems (RDBMS)
    Relational Databases work with data orginzaed into tables with rows and columns

Usual Relational Database Capabilities:
    Data Querying (DQL) : SELECT, JOIN, WHERE : Retrieve specific data
    Data Manipulation (DML) : INSERT, UPDATE, DELETE : Modify data
    Data Definition (DDL) : CREATE, ALTER, DROP : Define Structure 
    Data Control (DCL) : GRANT, REVOKE : Manage access permissions  

JOIN Types
    This is for manipulation of 2 pre-existing tables
    INNER JOIN : Returns only the rows where there is a match in BOTH tables. 
    LEFT (Outer) JOIN : Return all rows from left table and matching from right table
    RIGHT (Outer) JOIN : Return all rows from right table and matching from left table
    FULL (Outer) JOIN : Returns all rows where there is a match in either left or right table
    CROSS JOIN : Combines each row of the first table with every row of the second table
    SELF JOIN : Table is joined with itself    

Popular Relational Database Systems:
    MySQL : Open-source DB
    PostgreSQL : Advanced Open-source DB
    Microsoft SQL Server : Enterprise DB
    Oracle DB : Commercial DB
    SQLite : Often used in embedded

CRUD (Create, Read, Update, Delete)
    The four essential basic opertations for persistent data storage
    Create : INSERT : Adds new record or entry
    Read : SELECT : Retrieves existing data from database
    Update : UPDATE : Modifies existing data
    Delete : DELETE : Removes unwanted data

Indexes
    An index in SQL is a database structure used to speed up data retrieval by allowing quick access to records 
        instead of scanning the full database. Think something like binary search.
    This works by storing indexed column values in a seperate, ordered structure. Typically as a B-tree.
        The DB then searches the index, finds row locations, and then retreives the rows.
    Common Index Types:
        Primary Key Index : created automatically
        Unique Index : enforces uniqueness
        Single Column Index : Single column index
        Composite Index : Multiple column indexes
    Benefits of an index are faster reads, joins, and sorting. However, every time the tables are updated the index need to
        be updated as well resulting in slower insert, update, and delete functionality.
        
Constraints
    PRIMARY KEY : uniquely identifies each row; cannot be NULL
    FOREIGN KEY : enforces relationship between tables
    UNIQUE : prevents duplicate values
    NOT NULL : column must contain a value
    CHECK : value must satisfy a condition
    DEFAULT : assigns a value of none provided

Basic Normalization
    Process of structuring tables to reduce redundancy and prevent data anomalies

    1st Normal Form (1NF)
        No Repeating groups or arrays
        Each field holds a single value
        Each row identifiable by a key

    2nd Normal Form (2NF)
        Must be in 1NF
        Non-key columns depend on the entire primary key (import for composite keys)

    3rd Normal Form (3NF)
        Must be in 2NF
        Non-key columns depend only on the primary key, no other non-key columns

"""


