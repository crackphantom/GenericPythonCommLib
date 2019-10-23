'''
Created on Oct 23, 2019

@author: crackphantom
'''
import unittest
from genericpcommlib.http import factory

class TestHttpFactory(unittest.TestCase):


    def testBadDefaultClientForGetSync(self):
        exceptionThrown = False
        try:
            client = factory.getNewSyncHttpClient("bad")
        except Exception as e:
            exceptionThrown = True
            self.assertEquals("Unable to create a sync http client from configured library", str(e))
        self.assertTrue(exceptionThrown)

    def testSpecifyGoodClientForGetSync(self):
        client = factory.getNewSyncHttpClient(factory.URLLIB2)
        self.assertIsNotNone(client)

    def testBadDefaultClientForGetAsync(self):
        exceptionThrown = False
        try:
            client = factory.getNewAsyncHttpClient("bad")
        except Exception as e:
            exceptionThrown = True
            self.assertEquals("Unable to create an async http client from configured library", str(e))
        self.assertTrue(exceptionThrown)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()