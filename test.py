from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Flask was set up correctly?
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)

    # Does page load correctly?
    def test_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertTrue(b'Place' in  response.data)

    # Does page behaves correctly given the correct credentials outside the MKAD?
    def test_correct_credentials_outside(self):
        tester = app.test_client(self)
        response = tester.post('/',data=dict(place="istanbul"),follow_redirects = True)
        self.assertIn(b'1642 km',  response.data)

    # Does page behaves correctly given the correct credentials outside the MKAD?
    def test_correct_credentials_inside(self):
        tester = app.test_client(self)
        response = tester.post('/',data=dict(place="MKAD"),follow_redirects = True)
        self.assertIn(b'you are inside',  response.data)

    # Does page behaves correctly given the incorrect credentials?
    def test_incorrect_credentials(self):
        tester = app.test_client(self)
        response = tester.post('/',data=dict(place=""),follow_redirects = True)
        self.assertIn(b'Invalid Place Name, try again',  response.data)

    # Does page behaves correctly given the incorrect or unexpected credentials to the api?
    def test_incorrect_api_credentials(self):
        tester = app.test_client(self)
        response = tester.post('/',data=dict(place="mskt"),follow_redirects = True)
        self.assertIn(b'There is a problem, try again',  response.data)


if __name__ == '__main__':
    unittest.main()
