from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('', views.index, name='index'),
    path('my_view', views.my_view, name='myview'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog')
]