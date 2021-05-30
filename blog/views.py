from django.views.generic import ListView, DetailView
from .models import Post, Tag, Log

import datetime

class PostListView(ListView):
    model = Post
    ordering = ['-timestamp']
    
class FilteredPostListView(ListView):
    model = Post
    ordering = ['-timestamp']
    template_name = 'blog/post_filtered_list.html'

    def get_queryset(self):
        return super(FilteredPostListView, self).get_queryset().filter(tags__in=[Tag.objects.get(name=self.kwargs['tag'])])

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log_request(self.request)
        return context

def log_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    print(request.path)
    log = Log()
    log.path = request.path
    log.ip = ip
    log.timestamp = datetime.datetime.now()
    log.query = request.META.get('QUERY_STRING')
    log.save()
