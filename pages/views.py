from django.views.generic import TemplateView


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class ResumePageView(TemplateView):
    template_name = 'resume.html'


class ProjectsPageView(TemplateView):
    template_name = 'projects.html'

