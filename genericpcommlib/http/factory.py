'''
Created on Oct 23, 2019

@author: crackphantom
'''
import logging

LOGGER = logging.getLogger()

URLLIB2 = 'core2_7.wrapurllib2'

SYNC_CLIENT_CLASSES = {}
ASYNC_CLIENT_CLASSES = {}

try:
    from genericpcommlib.http.clients.core2_7 import wrapurllib2
    SYNC_CLIENT_CLASSES[URLLIB2] = wrapurllib2.HttpClient
except(ImportError, ValueError, AttributeError):
    LOGGER.warning("Unable to load the core2_7.wrapurllib2 client")
    if LOGGER.isEnabledFor(logging.DEBUG):
        LOGGER.exception("The exception when loading was")


def getNewSyncHttpClient(httplib=None):
    # based on requested lib or ystem configuration, instantiate a new http client
    if httplib == None or httplib not in SYNC_CLIENT_CLASSES:
        #TODO: try to load a default
        raise RuntimeError("Unable to create a sync http client from configured library")
    return SYNC_CLIENT_CLASSES[httplib]()

def getNewAsyncHttpClient(httplib=None):
    # based on requested lib or ystem configuration, instantiate a new http client
    if httplib == None or httplib not in SYNC_CLIENT_CLASSES:
        #TODO: try to load a default
        raise RuntimeError("Unable to create an async http client from configured library")
    return SYNC_CLIENT_CLASSES[httplib]()