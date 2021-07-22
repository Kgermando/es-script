"""scripting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from scripting.search import GlobalSearchAPIView


handler400 = 'scripting.views_errors_page.handler400'
handler403 = 'scripting.views_errors_page.handler403'
handler404 = 'scripting.views_errors_page.handler404'
handler500 = 'scripting.views_errors_page.handler500'
handler503 = 'scripting.views_errors_page.handler503'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', GlobalSearchAPIView.as_view()),
    path('app/', include('app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('forms/', include('forms.urls')),
    path('pbx/', include('pbx.urls')),
    path('agenda/', include('agenda.urls')),
    path('dat/', include('dat.urls')),
    path('acquisition/', include('acquisition.urls')),
    path('commprom/', include('commprom.urls')),
    path('comptedormant/', include('comptedormant.urls')),
    path('recouvrement/', include('recouvrement.urls')),
    path('renouvellement/', include('renouvellement.urls')),
    path('contacts/', include('contacts.urls')),
    path('issabel/', include('issabel.urls')),
    path('param/', include('paramurl.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
  
