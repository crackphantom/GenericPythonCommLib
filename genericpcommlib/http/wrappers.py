'''
Created on Oct 23, 2019

@author: crackphantom
'''

class HttpResponse(object):

    def __init__(self):
        # underlying library failed to get a response
        self.exists = True # do we even have a response?
        self.caughtException = None# if any
    
        # http response status line
        self.statusProtocol = 'HTTP/1.1' # default
        self.statusCode = None
        self.parsedStatusCode = None # string turned into a number
        self.statusText = None
    
        # http response headers
        self.headers = [] # list of raw text
        # dict of lists where the key is the header name.
        # try to follow the convention of lowercasing the header key
        # Lists handles header name being used multiple times
        self.parsedHeaders = {}
    
        # http response body
        self.body = '' # raw text
