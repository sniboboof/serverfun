from lettuce import step
from lettuce import world

import server

@step('the request was bad')
def bad_request(step):
    world.string = unicode("GERT /README.md HTTP/1.1\r\nHost:http://example.com")

@step('the server parses the request')
def parse_request(step):
    world.string = server.getResponse(world.string)

@step('it returns a bad request error')
def check_if_error(step):
    assert world.string.split()[1] == u'400', "got %s" % world.string.split()[1]

@step('the request was for a nonexistent file')
def no_file(step):
    world.string = unicode("GET /notreal.nope HTTP/1.1\nHost:http://example.com\r\n")

@step('it returns a file not found response')
def check_file_404(step):
    assert world.string.split()[1] == u'404', "got %s" % world.string.split()[1]

@step('the request was for a proper file')
def file_found(step):
    world.string = unicode("GET /README.md HTTP/1.1\nHost:http://example.com\r\n")

@step('it returns a proper response containing the data')
def check_file_found(step):
    assert world.string.split()[1] == u'200', "got %s" % world.string.split()[1]
    assert world.string.split('\n')[2].split()[1] == u'file'

@step('the request was for a proper directory')
def folder_found(step):
    world.string = unicode("GET /sample HTTP/1.1\nHost:http://example.com\r\n")

@step('it returns a proper response containing the contents')
def check_folder_found(step):
    assert world.string.split()[1] == u'200', "got %s" % world.string.split()[1]
    assert world.string.split('\n')[2].split()[1] == u'directory'
