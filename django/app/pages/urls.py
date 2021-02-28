# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(r'xml', views.xml, name='xml')
]
urlpatterns += [
    path(r'parte1',views.parte1, name='home1')
]
urlpatterns +=[
   path(r'xsl',views.ficheroXSLT, name="xsl")
]
urlpatterns +=[
   path(r'parte2',views.parte2,name="home2")
]
