from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),

]

4
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)