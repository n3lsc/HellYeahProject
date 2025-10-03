from django.test import TestCase, Client
from .models import Post
from django.utils import timezone

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title ="Test Title",
            content ="Test Content",
            author = "Test Author"
        )
    
    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.author, "Test Author")
        self.assertTrue(self.post.created_at <= timezone.now())

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Title")
#        self.assertEqual(str(self.post), "Test Content")
class PostViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        Post.objects.create(title="Test Title1", content="Test Content1", author="Test Author1")
        Post.objects.create(title="Test Title2", content="Test Content2", author="Test Author2")

    def test_post_list_view_status(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_view_content(self):
        response = self.client.get('/posts/')
        self.assertContains(response, "Test Title1")
        self.assertContains(response, "Test Title2")


# Create your tests here.
