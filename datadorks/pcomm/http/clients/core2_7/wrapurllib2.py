'''
Created on Oct 23, 2019

@author: crackphantom
'''
import urllib2
from datadorks.pcomm.http import wrappers, utils


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
    def doRequest(self, wrappedhttprequest):
        # was verb, url, headers, body
        # where headers is a dict and body is a string

        req = urllib2.Request(wrappedhttprequest.url)
        if wrappedhttprequest.headers:
            for key, value in wrappedhttprequest.headers.iteritems():
                req.add_header(key, value)
        req.get_method = lambda: wrappedhttprequest.method
        resp = wrappers.HttpResponse()
        try:
            if wrappedhttprequest.multipart:
                boundary = utils.getMultiPartBoundary()
                body = utils.getMultiPartBody(boundary, wrappedhttprequest)
                req.add_data(body)
                contentType = 'multipart/form-data; boundary={}'.format(boundary)
                req.add_header('Content-type', contentType)
                req.add_header('Content-length', len(body))
                responseFile = urllib2.urlopen(req)
            else:
                responseFile = urllib2.urlopen(req, wrappedhttprequest.body)
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
