from django.test import TestCase
from blog.models import Post

class PostTestCase(TestCase):
  def setUp(self):
    Post.objects.create(title="title1", text="ブログ本文1")
    Post.objects.create(title="title2", text="ブログ本文2")
  
  def test_blog_title(self):
    post = Post.objects.get(title="title1")
    self.assertEqual(post.title, "title1")
  
  def test_is_count_two(self):
    posts = Post.objects.all()
    self.assertEqual(posts.count(), 2)

  def test_is_count_three(self):
    post = Post(title='title3', text='ブログ本文3')
    post.save()
    posts = Post.objects.all()
    self.assertEqual(posts.count(), 3)
  