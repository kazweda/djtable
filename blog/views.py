from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm

class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['num_posts'] = len(posts)
        return context
    
class PostListView(generic.ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し

class PostCreateView(generic.CreateView): # 追加
    model = Post # 作成したい model を指定
    form_class = PostCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('blog:posts') # 記事作成に成功した時のリダイレクト先を指定
    
class HomeView(generic.TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['num_posts'] = len(posts)
        return context