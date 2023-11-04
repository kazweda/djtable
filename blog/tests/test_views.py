from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user1 = User.objects.create_user(username='user1', password='qYi8Vp9S')
    cls.user1.save()
    
    for postid in range(13):
        Post.objects.create(
          author = cls.user1,
          title = 'test title {}'.format(postid), 
          text = '本文です。{}'.format(postid),
        )
            
  def test_list_use_correct_template(self):
    response = self.client.get('/blog/posts/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')
    
  def test_posts_count_correct(self):
    response = self.client.get('/blog/posts/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')
    self.assertEqual(len(response.context.get("post_list")), 13)