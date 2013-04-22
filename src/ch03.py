import unittest
from pyramid import testing

class Test(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_greeting(self):
        from ch02 import hello_world
        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(b'Hello World!', response.body)

if __name__ == '__main__':
    unittest.main()
