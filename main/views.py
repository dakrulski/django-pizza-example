from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    name = 'main'
    template_name = 'main/index.html'
