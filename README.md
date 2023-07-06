# Create a Django application that get data from
an endpoint that have Basic Auth, your task are:

1- Get de data from a remote endpoint using Basic Auth. (User:Password)

2- Parse the data and response a json order by one field in descending order
   example: http://localhost:8000/test/data 

3- Save the data in a table and create a public GET endpoint 
   that expose that table as json, the data should it order by one field 
   in descending order
   example: http://localhost:8000/test/list (GET)

4- Push the code to an public repository

Regards



``` Json

{
    "data": {
        "frameworks": {
            "Bottle": "28 %",
            "Web2Py": "55 %",
            "Flask": "35 %",
            "Django": "65 %",
            "CherryPy": "16 %"
        },
        "desc": [
            "Web2Py: Create, modify, deploy and manage application from anywhere using your browser",
            "Bottle: Is a fast, simple and lightweight WSGI micro web-framework for Python",
            "Django: Is a high-level Python web framework that encourages rapid development and clean",
            "CherryPy: Is a pythonic, object-oriented web framework",
            "Flask: provides configuration and conventions, with sensible defaults, to get started"
        ]
    }
}
```