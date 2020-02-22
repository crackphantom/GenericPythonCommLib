'''
Created on Oct 23, 2019

@author: crackphantom
'''
import urllib.request
from datadorks.pcomm.http import wrappers, utils

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
    def doRequest(self, wrappedhttprequest):

        req = urllib.request.Request(wrappedhttprequest.url, method=wrappedhttprequest.method)
        if wrappedhttprequest.headers:
            for key, value in wrappedhttprequest.headers.items():
                req.add_header(key, value)

        resp = wrappers.HttpResponse()
        try:
            encodedBody = None
            if wrappedhttprequest.multipart:
                boundary = utils.getMultiPartBoundary()
                body = utils.getMultiPartBody(boundary, wrappedhttprequest)
                encodedBody = body.encode(UTF8_BYTE)
                contentType = 'multipart/form-data; boundary={}'.format(boundary)
                req.add_header('Content-type', contentType)
                req.add_header('Content-length', len(encodedBody))
            elif wrappedhttprequest.body is not None:
                encodedBody = wrappedhttprequest.body.encode(UTF8_BYTE)

            responseFile = urllib.request.urlopen(req, encodedBody)
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
