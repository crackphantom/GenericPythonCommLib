'''
Created on Oct 23, 2019

@author: crackphantom
'''
import logging
LOGGER = logging.getLogger()

PY27URLLIB2 = 'core2_7.wrapurllib2'
PY3URLLIB = 'core3.wrapurllib'

SYNC_CLIENT_CLASSES = {}
ASYNC_CLIENT_CLASSES = {}

try:
    from datadorks.pcomm.http.clients.core2_7 import wrapurllib2 as core2_7wrapurllib2
    SYNC_CLIENT_CLASSES[PY27URLLIB2] = core2_7wrapurllib2.HttpClient
except(ImportError, ValueError, AttributeError):
    LOGGER.warning("Unable to load the core2_7.wrapurllib2 client")
    if LOGGER.isEnabledFor(logging.DEBUG):
        LOGGER.exception("The exception when loading was")

try:
    from datadorks.pcomm.http.clients.core3 import wrapurllib as core3wrapurllib
    SYNC_CLIENT_CLASSES[PY3URLLIB] = core3wrapurllib.HttpClient
except(ImportError, ValueError, AttributeError):
    LOGGER.warning("Unable to load the core3.wrapurllib2 client")
    if LOGGER.isEnabledFor(logging.DEBUG):
        LOGGER.exception("The exception when loading was")

def getNewSyncHttpClient(whitelist=None, blacklist=None):
    if whitelist:
        for httplib in whitelist:
            if httplib != None and httplib in SYNC_CLIENT_CLASSES:
                return SYNC_CLIENT_CLASSES[httplib]()
        # fail if nothing found on the whitelist
        raise RuntimeError("Unable to create a sync http client from configured library, libs provided in whitelist were unavailable")
    if blacklist is None:
        # nothing is blacklisted if empty, so we will use first lib found in next loop
        blacklist = []

    for httplib in SYNC_CLIENT_CLASSES.keys():
        if httplib != None and httplib not in blacklist:
            # based on requested lib or system configuration, instantiate a new http client
            return SYNC_CLIENT_CLASSES[httplib]()
    
    #Nothing loaded that was acceptable given the 2 lists or lack there of
    raise RuntimeError("Unable to create a sync http client from configured library")

def getNewAsyncHttpClient(whitelist=None, blacklist=None):
    if whitelist:
        for httplib in whitelist:
            if httplib != None and httplib in SYNC_CLIENT_CLASSES:
                return SYNC_CLIENT_CLASSES[httplib]()
        # fail if nothing found on the whitelist
        raise RuntimeError("Unable to create an async http client from configured library, libs provided in whitelist were unavailable")
    if blacklist is None:
        # nothing is blacklisted if empty, so we will use first lib found in next loop
        blacklist = []

    for httplib in SYNC_CLIENT_CLASSES.keys():
        if httplib != None and httplib not in blacklist:
            # based on requested lib or system configuration, instantiate a new http client
            return SYNC_CLIENT_CLASSES[httplib]()
    raise RuntimeError("Unable to create an async http client from configured library")
