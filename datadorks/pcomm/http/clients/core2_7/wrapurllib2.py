'''
Created on Oct 23, 2019

@author: crackphantom
'''
import urllib2
from datadorks.pcomm.http import wrappers


class HttpClient(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.cookieprocessor = urllib2.HTTPCookieProcessor()
        opener = urllib2.build_opener(self.cookieprocessor)
        urllib2.install_opener(opener)
        '''
        Constructor
        '''
    def doRequest(self, verb, url, headers, body):
        # headers is a dict
        # body is a string

        req = urllib2.Request(url)
        if headers:
            for key, value in headers.iteritems():
                req.add_header(key, value)
        req.get_method = lambda: verb
        resp = wrappers.HttpResponse()
        try:
            responseFile = urllib2.urlopen(req, body)
            resp.url = responseFile.geturl()
            resp.statusCode = responseFile.code
            resp.statusText = responseFile.msg
            for rawHeaderStr in responseFile.info().headers:
                resp.headers.append(rawHeaderStr)
                headerPair = rawHeaderStr.split(':', 1)
                # TODO: Update Magic numbers with consts
                resp.parsedHeaders.setdefault(headerPair[0].lower(), []).append(headerPair[1])
            resp.body = responseFile.read()
        except urllib2.HTTPError as e:
            resp.exists = False
            resp.caughtException = e
        return resp
