from django.test import TestCase

from main.models import Videos


class MainModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.video = {
            'name': '1name',
            'preview': '1prev',
            'video': '1vid',
            'description': '1desc',
            'views': 125,
            'likes': 28,
            'dislikes': 13,
            }

        Videos.objects.create(**cls.video)

    def test_name(self):
        field = 'name'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_preview(self):
        field = 'preview'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_video(self):
        field = 'video'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_description(self):
        field = 'description'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_views(self):
        field = 'views'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_likes(self):
        field = 'likes'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_dislikes(self):
        field = 'dislikes'

        vid = Videos.objects.get()
        name = vid.__dict__[field]
        self.assertEquals(name, self.video[field])

    def test_name_max_length(self):
        field = 'name'

        vid = Videos.objects.get()
        max_length = vid._meta.get_field(field).max_length
        self.assertEquals(max_length, 255)
