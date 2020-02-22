'''
Created on Oct 23, 2019

@author: crackphantom
'''
from datadorks.pcomm.http.consts import EMPTY_BODY, GET_METHOD


class HttpResponse(object):

    def __init__(self):
        # underlying library failed to get a response
        self.exists = True # do we even have a response?
        self.caughtException = None# if any
    
        # http response status line
        self.statusProtocol = 'HTTP/1.1' # default
        self.url = None # the url you were sent to (may stay the same as request or may change)
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

class HttpRequest(object):
    
    def __init__(self, url, method = GET_METHOD):
        self.url = url
        self.method = method
        self.headers = {}
        self.body = EMPTY_BODY
        self.parameters = {}
        self.files = {}
        
        self.multipart = False

    def addHeader(self, name, value):
        self.headers[name] = value
    
    def addParameter(self, name, value):
        self.parameters[name] = value
    
    def addFile(self, name, filename, value, contentType):
        self.files[name] = {'filename': filename,
                            'value': value,
                            'Content-Type': contentType}
