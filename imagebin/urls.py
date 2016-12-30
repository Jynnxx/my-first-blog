from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.page, name='page'),
    url(r'^upload/$', views.page, name='page'),
    url(r'^home/$', views.page, name='page'),
    url(r'^media/',views.show, name = 'show')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)