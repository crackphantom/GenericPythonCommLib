'''
Created on Oct 23, 2019

@author: crackphantom
'''
import urllib.request
from datadorks.pcomm.http import wrappers

UTF8_BYTE = 'utf-8'


class HttpClient(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.cookieprocessor = urllib.request.HTTPCookieProcessor()
        opener = urllib.request.build_opener(self.cookieprocessor)
        urllib.request.install_opener(opener)
        '''
        Constructor
        '''
    def doRequest(self, verb, url, headers, body):
        # headers is a dict
        # body is a string

        req = urllib.request.Request(url, method=verb)
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        # req.get_method = lambda: verb
        resp = wrappers.HttpResponse()
        try:
            # TODO: https://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json/26876308#26876308
            responseFile = urllib.request.urlopen(req, body.encode(UTF8_BYTE))
            resp.url = responseFile.geturl()
            resp.statusCode = responseFile.code
            resp.statusText = responseFile.msg
            for hVTup in responseFile.getheaders():
                #resp.headers.append(rawHeaderStr)
                #headerPair = rawHeaderStr.split(':', 1)
                # TODO: Update Magic numbers with consts
                resp.parsedHeaders.setdefault(hVTup[0].lower(), []).append(hVTup[1])
            resp.body = responseFile.read()
        except urllib.request.HTTPError as e:
            resp.exists = False
            resp.caughtException = e
        return resp
