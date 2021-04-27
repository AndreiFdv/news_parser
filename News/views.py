from django.views import generic

from News.models import Article


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    paginate_by = 12

    def get_queryset(self):
        return Article.objects.all().order_by('date')


class DetailView(generic.DetailView):
    model = Article
    template_name = 'news/article.html'
