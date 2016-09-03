#usr/bin/env python

import unittest
import urllib2

URL_Dict = {"https://iris.vaisala.com/health": "200 OK",
            "https://iris.vaisala.com": "com.vaisala.fire.client.login.LoginStrings"}

class testUrlResponses(unittest.TestCase):
    ''' Tests that the given string is found at the given URL '''
    def test_url_responses(self):
        for URL in URL_Dict.keys():
            print "Checking that : " + URL_Dict[URL] + " is found at " + URL
            response = urllib2.urlopen(URL)
            self.assertIn(URL_Dict[URL], response.read())


if __name__ == '__main__':
    unittest.main()