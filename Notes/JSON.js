/* JSON : JavaScript Object Notation
 JSON is a lightweight format used for storing and transporting data.
 Often used when data is sent from server to web page.

 JSON Example
{
"employees":[
    {"firstName":"John", "LastName":"Doe"},
    {"firstName":"Anna", "LastName":"Smith"},
    {"firstName":"Peter", "LastName":"Jones"},
]
}

 JSON Syntax Rules
 Data is in name/value pairs
 Data is seperated by commas
 Curly braces hold objects
 Square brackets hold arrays

 JSON format is syntactically identical to the code for creating JavaScript Objects
 Therefore, you can convert JSON text directly to a JS object
*/ 
// First, save the JSON text to a string variable

var text = '{"employees": [ ' +
    '{"firstName":"John", "LastName":"Doe"},' +
    '{"firstName":"Anna", "LastName":"Smith"},' +
    '{"firstName":"Peter", "LastName":"Jones"}]}';

// Then use the JS JSON method to convert the string into a JS Object

var obj = JSON.parse(text)

// The object can now be used freely in its given format
obj.employees[1].firstName // Anna
obj.employees[2].lastName // Jones