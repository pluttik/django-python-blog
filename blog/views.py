from django.views.generic import ListView
from .models import Post, Tag

class PostListView(ListView):
    model = Post
    ordering = ['-timestamp']
    
class FilteredPostListView(ListView):
    model = Post
    ordering = ['-timestamp']

    def get_queryset(self):
        return super(FilteredPostListView, self).get_queryset().filter(tags__in=[Tag.objects.get(name=self.kwargs['tag'])])
