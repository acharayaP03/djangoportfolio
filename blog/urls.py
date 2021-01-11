
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_view, name="blog_view"),
    path('<int:blog_id>', views.blog_detail_view, name="blog_detail")
]