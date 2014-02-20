Feature: Server forms a Response
    The server knows what it wants the response to be
    this means it knows the response code, headers,
    and body that it wants to send
    
    Scenario: bad request
        Given the request was bad
        When the server parses the request
        Then it returns a bad request error
    
    Scenario: file not found
        Given the request was for a nonexistent file
        When the server parses the request
        Then it returns a file not found response
    
    Scenario: file found
        Given the request was for a proper file
        When the server parses the request
        Then it returns a proper response containing the data
    
    Scenario: folder found
        Given the request was for a proper directory
        When the server parses the request
        Then it returns a proper response containing the contents