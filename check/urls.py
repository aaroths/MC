"""checkup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Use include() to add URLS from the catalog application
from django.conf.urls import include

urlpatterns += [
    url(r'^MC/', include('MC.urls')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#Add URL maps to redirect the base URL to our application
#redirects site from basic IP to /check
from django.views.generic import RedirectView
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

urlpatterns += [url(r'^$', RedirectView.as_view(url='/MC/', permanent=True)),]
urlpatterns += [url(r'accounts/profile$', RedirectView.as_view(url='/', permanent=True)),]
urlpatterns += [url(r'accounts/profile', RedirectView.as_view(url='/', permanent=True)),]

#redirect to home
#url(r'^accounts/profile$', RedirectView.as_view(permanent=False))
#url(r'^$', RedirectView.as_view(url=reverse_lazy('app_dashboard')), name='index'),
#urlpatterns = [(r'^accounts/profile$', views.url_redirect, name="url-redirect"),]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns = [url(r'^accounts/profile/$', RedirectView.as_view(url='/MC/', permanent=True)),]
