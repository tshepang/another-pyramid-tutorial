import unittest

from pyramid import testing

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello(self):
        from ch04 import hello_world
        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(b'Hello World!', response.body)

    def test_goodbye(self):
        from ch04 import goodbye_world
        request = testing.DummyRequest()
        response = goodbye_world(request)
        self.assertEqual(b'Goodbye World!', response.body)


class FunctionalTests(unittest.TestCase):

    def setUp(self):
        from ch04 import main
        import webtest
        self.testapp = webtest.TestApp(main())

    def test_hello(self):
        self.assertIn('Hello World!', self.testapp.get('/'))

    def test_goodbye(self):
        self.assertIn('Goodbye World!', self.testapp.get('/bye'))


if __name__ == '__main__':
    unittest.main()
