from django.test import TestCase
from django.urls import reverse 
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):

    def setup(self):
        Post.objects.create(text='just testing to see')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.text}'
        self.assertEquals(expected_object_name, 'just testing to see')


class HomePageViewTest(TestCase):

    def setup(self):
        Post.objects.create(text='Another test case')

    def test_view_url_exists_at_proper_location(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)


    def test_view_url_by_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

