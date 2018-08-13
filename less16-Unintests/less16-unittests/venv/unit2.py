import unittest
import requests
import re
import responses
import json
import logging
import sys

if name == 'main':
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
else:
    log = logging.getLogger(name)

log.info('PASS')
log.debug('Something about %r in %s', log, name)

url = 'https://jsonplaceholder.typicode.com/'

class JsonPlaceholderTests(unittest.TestCase):
    def test_request_get(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_get_postcomments_negative(self):
        response = requests.get(url + 'comments/-40000')
        self.assertEqual(response.status_code, 404)
        logging.info('[PASS]')

if name=='main':
    unittest.main()

