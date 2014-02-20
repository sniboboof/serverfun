httpserver.py runs a simple http server that will accept requests and return responses

it should open up a socket with the client and accept a requests

although it should accept any request without breaking, the only request that can get a non-error response will be a GET response for a valid file or directory. any other request should return a relevant error.