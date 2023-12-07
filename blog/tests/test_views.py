from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from myuser.models import MyUser as User

class PostListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user1 = User.objects.create_user(
      username='user1',
      password='qYi8Vp9S',
      email='user1@example.com',
      )
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
    
class PostCreateTests(TestCase):
    """PostCreateビューのテストクラス."""

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        """適当なデータで　POST すると、成功してリダイレクトされることを確認"""
        data = {
            'title': 'test_title',
            'text': 'test_text',
        }
        response = self.client.post(reverse('blog:post_create'), data=data)
        self.assertEqual(response.status_code, 302)
    
    def test_post_null(self):
        """空のデータで POST を行うとリダイレクトも無く 200 だけ返されることを確認"""
        data = {}
        response = self.client.post(reverse('blog:post_create'), data=data)
        self.assertEqual(response.status_code, 200)