from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
from .forms import PostForm, CommentForm


class UserProfileModelTest(TestCase):
    def test_user_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        profile = UserProfile.objects.create(user=user, bio='Test bio')
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test bio')


class PostModelTest(TestCase):
    def test_post_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        post = Post.objects.create(author=user, content='Test post')
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.content, 'Test post')


class CommentModelTest(TestCase):
    def test_comment_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        post = Post.objects.create(author=user, content='Test post')
        comment = Comment.objects.create(post=post, author=user, text='Test comment')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.author.username, 'testuser')
        self.assertEqual(comment.text, 'Test comment')


class PostFormTest(TestCase):
    def test_post_form_valid(self):
        form_data = {'content': 'Test post content'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        form_data = {'content': ''}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'text': 'Test comment text'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {'text': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class ViewsTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
