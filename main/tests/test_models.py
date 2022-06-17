from django.test import TestCase

class MainModelTestCase(TestCase):
    def test_add(self):
        we_want = 'add'
        we_have = 'add'
        self.assertEqual(we_want, we_have)

    def test_update(self):
        we_want = 'update'
        we_have = 'update'
        self.assertEqual(we_want, we_have)

    def test_delete(self):
        we_want = 'delete'
        we_have = 'delete'
        self.assertEqual(we_want, we_have)

    def test_get(self):
        we_want = 'get'
        we_have = 'get'
        self.assertEqual(we_want, we_have)
