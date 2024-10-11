from django.urls import path, include

from .views import ContactPageView, ResumePageView, ProjectsPageView


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
