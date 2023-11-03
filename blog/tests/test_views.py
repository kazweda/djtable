from django.test import TestCase
from django.contrib.auth.models import User

class PostListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user1 = User.objects.create_user(username='user1', password='qYi8Vp9S')
    cls.user1.save()
    
  def test_list_use_correct_template(self):
    response = self.client.get('/posts/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')
    