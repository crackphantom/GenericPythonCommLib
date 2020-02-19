'''
Created on Oct 23, 2019

@author: crackphantom
'''
# Uncomment to set logging at debug
# first thing so other loggers are properly set when loading modules etc...
# import logging
# logging.basicConfig(level=logging.DEBUG)

import unittest
from datadorks.pcomm.http.clients import factory

# address 'No handlers could be found for logger "root"' which annoys me
# code used to address doesn't belong in the lib we're testing
import logging
logging.basicConfig()


class TestHttpFactory(unittest.TestCase):

    def testBadDefaultClientForGetSync(self):
        exceptionThrown = False
        try:
            client = factory.getNewSyncHttpClient(["badwhitelist"])
        except Exception as e:
            exceptionThrown = True
            self.assertEquals("Unable to create a sync http client from configured library, libs provided in whitelist were unavailable", str(e))
        self.assertTrue(exceptionThrown)

    def testBadDefaultClientWithBlacklistEverythingForGetSync(self):
        exceptionThrown = False
        try:
            factory.SYNC_CLIENT_CLASSES.keys()
            client = factory.getNewSyncHttpClient(None, factory.SYNC_CLIENT_CLASSES.keys())
        except Exception as e:
            exceptionThrown = True
            self.assertEquals("Unable to create a sync http client from configured library", str(e))
        self.assertTrue(exceptionThrown)

    def testSpecifyGoodClientWithWhiteListForGetSync(self):
        client = factory.getNewSyncHttpClient(factory.SYNC_CLIENT_CLASSES.keys())
        self.assertIsNotNone(client)

    def testSpecifyGoodClientWithNoListsForGetSync(self):
        client = factory.getNewSyncHttpClient()
        self.assertIsNotNone(client)

    def testSpecifyGoodClientWithBlacklistForGetSync(self):
        client = factory.getNewSyncHttpClient(None, ['badblacklist'])
        self.assertIsNotNone(client)

    def testBadDefaultClientForGetAsync(self):
        exceptionThrown = False
        try:
            client = factory.getNewAsyncHttpClient(["bad"])
        except Exception as e:
            exceptionThrown = True
            self.assertEquals("Unable to create an async http client from configured library, libs provided in whitelist were unavailable", str(e))
        self.assertTrue(exceptionThrown)

if __name__ == "__main__":
    # /usr/bin/python2.7 -m unittest -v tests.standalone.testhttpfactory.TestHttpFactory
    # /usr/bin/python3 -m unittest -v tests.standalone.testhttpfactory.TestHttpFactory
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
