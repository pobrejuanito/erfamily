from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^about.html',TemplateView.as_view(template_name="pages/about.html")),
    url(r'^services.html',TemplateView.as_view(template_name="pages/services.html")),
    url(r'^contact.html',TemplateView.as_view(template_name="pages/contact.html")),
    url(r'^appointment.html',TemplateView.as_view(template_name="pages/appointment.html")),
    url(r'^sendmessage/', views.sendmessage, name='sendmessage'),
    url(r'^appointment/', views.appointment, name='appointment'),
]