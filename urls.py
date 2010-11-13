from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('encontro_pesca_aquicultura.inscricao.urls')),
    (r'^site_media/(.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT}
    ),
)
