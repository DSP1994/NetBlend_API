from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
# List View Test
class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='david', password='password')

    def test_can_list_posts(self):
        david = User.objects.get(username='david')
        Post.objects.create(owner=david, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='david', password='password')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# Detail View Tests
class PostDetailViewTest(APITestCase):
    def setUp(self):
        david = User.objects.create_user(
            username='david', password='password2')
        brian = User.objects.create_user(
            username='brian', password='password2')
        Post.objects.create(
            owner=david, title='test title', content='test content'
        )
        Post.objects.create(
            owner=brian, title='another title', content='test content 2'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_post_with_an_invalid_id(self):
        response = self.client.get('/posts/666')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_any_posts_they_own(self):
        self.client.login(username='david', password='password2')
        response = self.client.put(
            '/posts/1/', {'title': 'a second test title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a second test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_posts(self):
        self.client.login(username='david', password='password')
        response = self.client.put('/posts/2/', {'title': 'my new title'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
