from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^results$', views.results, name='results'),
    url(r'^_update_lists$', views.update_lists, name='update_lists'),
    url(r'^_preview_branch/([A-Za-z0-9-]+)$', views.preview_branch, name='preview_branch'),
    url(r'^terms', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^about', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^list/(.+)$', views.list_details, name='list'),
    url(r'^download$', RedirectView.as_view(url='/results', permanent=False), name='download'),
    url(r'^download.json$', views.json_download, name='json_download'),
    url(r'^download.csv$', views.csv_download, name='csv_download'),
    url(r'^download.xml$', views.xml_download, name='xml_download'),
]
