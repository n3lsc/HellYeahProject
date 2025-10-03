from django.test import TestCase
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

# Create your tests here.
