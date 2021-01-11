from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.
def blog_view(request):
    blog = Blog.objects

    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_view.html', context)

def blog_detail_view(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail_blog.html', { 'detail_blog': detail_blog})