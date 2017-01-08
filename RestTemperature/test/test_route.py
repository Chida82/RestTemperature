import unittest
from webtest import TestApp
import resttemp

class Test_route(unittest.TestCase):

    def test_home_route(self):
        app = TestApp(resttemp.bottle.app())
        assert app.get('/').status == '200 OK' 
        assert app.get('/').status == '200 OK' 

    def test_status(self):
        app = TestApp(resttemp.bottle.app())
        result = app.get('/status')
        assert result.status == '200 OK' 
        self.assertEqual(result.json['status'], 'ok')

if __name__ == '__main__':
	unittest.main()
