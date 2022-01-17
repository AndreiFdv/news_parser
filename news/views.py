from django.views import generic
from news.models import Article,Subscriber
from django.views.generic.edit import FormView,CreateView

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    paginate_by = 12

    def get_queryset(self):
        return Article.objects.all().order_by('date')


class DetailView(generic.DetailView):
    model = Article
    template_name = 'news/article.html'



class SubscriberView(CreateView):
    model = Subscriber
    fields = ['email_address']
    template_name = 'news/subscribe.html'
    success_url = '/'

    def form_valid(self, form):
        return super(SubscriberView, self).form_valid(form)
