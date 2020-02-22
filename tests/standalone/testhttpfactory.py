'''
Created on Oct 23, 2019

@author: crackphantom
'''
# first thing so other loggers are properly set when loading modules etc...
# set to DEBUG for troubleshooting
import logging
logging.basicConfig(level=logging.ERROR)

import unittest
from datadorks.pcomm.http.clients import factory


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
