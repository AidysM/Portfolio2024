from django.urls import path, include

from .views import ContactPageView


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
