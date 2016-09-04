#usr/bin/env python

import unittest
import urllib2
import dns.resolver

class test_allanwilson_net(unittest.TestCase):
    def test_allanwilson_dot_net(self):
            response = urllib2.urlopen("http://allanwilsongithub.github.io")
            print response
            self.assertIn("allanwilson.net", response.read())

    def test_allanwilson_dot_net_domain(self):
            cname = dns.resolver.query("allanwilson.net", 'A')
            for i in cname.response.answer:
                for j in i.items:
                    print j.to_text()


if __name__ == '__main__':
    unittest.main()