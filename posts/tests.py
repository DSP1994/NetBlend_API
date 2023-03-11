from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='david', passwords='pass')

    def test_can_list_posts(self):
        david = User.objects.get(username='david')
        Post.objects.create(owner=david, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)