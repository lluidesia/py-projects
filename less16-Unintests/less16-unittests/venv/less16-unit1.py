import unittest
import requests
import re
import responses
import json
import logging
import sys

if __name__ == '__main__':
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
else:
    log = logging.getLogger(__name__)

log.info('PASS')
log.debug('Something about %r in %s', log, __name__)

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

    def test_request_get_posts(self):
        response = requests.get(url+'posts/1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_get_posts_comments(self):
        response = requests.get(url+'posts/1/comments')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_get_comments_postId(self):
        response = requests.get(url+'comments?postId=1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_get_posts_userId(self):
        response = requests.get(url+'posts?userId=1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_post(self):
        response = requests.post(url+'posts')
        self.assertEqual(response.status_code, 201)
        logging.info('[PASS]')

    def test_request_put(self):
        response = requests.put(url + 'posts/1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_patch(self):
        response = requests.patch(url + 'posts/1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    #в реальному світі перед тестом delete потрібно створити запис і вже його видаляти під час тесту

    def test_request_delete(self):
        response = requests.delete(url + 'posts/1')
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_post_negative(self):
        response = requests.post(url + 'posts/-1')
        self.assertEqual(response.status_code, 404)
        logging.info('[PASS]')

    def test_request_put_negative(self):
        response = requests.put(url + 'posts/-11')
        self.assertEqual(response.status_code, 404)
        logging.info('[PASS]')

    def test_request_patch_negative(self):
        response = requests.patch(url + 'posts/-11')
        self.assertEqual(response.status_code, 404)
        logging.info('[PASS]')

    def test_request_delete_negative(self):
        response = requests.delete(url + 'posts/-1')
        self.assertEqual(response.status_code, 404)
        logging.info('[PASS]')

    #перевірити респонс боді, чи є тайтл, чи є юзер, id
    #можна зробити трохи більші тести
    #гет реквест респонс код тест
    #ще один тест, кий пеервіряє ключи і ще один логером, вкінці тест




if __name__ == '__main__':
    unittest.main()
