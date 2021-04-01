from django.views import generic

from News.models import Article


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all().order_by('date')


class DetailView(generic.DetailView):
    model = Article
    template_name = 'News/article.html'
