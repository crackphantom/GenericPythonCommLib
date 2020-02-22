'''
Created on Feb 21, 2020

@author: crackphantom
'''
import string
import random

CHARS = string.ascii_letters + string.digits

def getMultiPartBoundary():
    # https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html
    # boundary := 0*69<bchars> bcharsnospace 
    # bchars := bcharsnospace / " " 
    # bcharsnospace :=    DIGIT / ALPHA / "'" / "(" / ")" / "+"  / "_" / "," / "-" / "." / "/" / ":" / "=" / "?"
    return ''.join(random.choice(CHARS) for _ in range(random.randint(40, 69)))


def getFormDataStr(boundary, name, value):
    return '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}'.format(boundary,
                                                                                name,
                                                                                value)
def getFileDataStr(boundary, name, filename, fileType, fileStr):
    return '--{}\r\nContent-Disposition: file; name="{}"; filename="{}"\r\nContent-Type: {}\r\n\r\n{}\r\n'.format(boundary, name, filename, fileType, fileStr)

def getMultiPartBody(boundary, wrappedhttprequest):
    body = ''
    for name, requestFile in wrappedhttprequest.files.items():
        body += getFileDataStr(boundary,
                               name,
                               requestFile.get('filename','file'),
                               requestFile.get('Content-Type','text/plain'),
                               requestFile.get('value',''))
    for name, value in wrappedhttprequest.parameters.items():
        body += getFormDataStr(boundary, name, value)
    body += '--{}--'.format(boundary)
    return body
