# admin disabled
# from django.contrib import admin
from django.urls import path, include
from main.views import IndexView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('api/', include('rest_framework.urls', namespace='api'))
]
