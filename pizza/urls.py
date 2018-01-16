from django.urls import path, include
from main.views import IndexView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', IndexView.as_view()),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('docs/', include_docs_urls(title='Pizza Heaven API Documentation'))
]
