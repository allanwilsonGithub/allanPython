#usr/bin/env python

import pytest
import urllib2

@pytest.mark.parametrize("url,response_text", [
    ("https://iris.vaisala.com/health", "200 OK"),
    ("https://iris.vaisala.com", "com.vaisala.fire.client.login.LoginStrings"),
])
def test_url_responses(url,response_text):
    ''' Tests that the given response is found at the given URL '''
    print "Checking that : " + response_text + " is found at " + url
    response = urllib2.urlopen(url)
    assert response_text in response.read()