from rest_framework.test import APITestCase

class MainViewTestCase(APITestCase):
    def test_login(self):
        we_want = 'name'
        we_have = 'name'
        self.assertEqual(we_want, we_have)

    def test_password(self):
        we_want = 'pass'
        we_have = 'pass'
        self.assertEqual(we_want, we_have)
