"""Auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from app01 import views
from app01 import urls as app01_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login),
    url(r'^register/',views.register),
    url(r'^home/',views.home),
    url(r'^logout/',views.logout),
    url(r'^set_password/',views.set_password),
    url(r'^middle/',views.middle),
    url(r'^v_code/',views.v_code),
    url(r'^login2/',views.login2),
    url(r'^pcgetcaptcha/',views.pcgetcaptcha),
    url(r'^reg/',views.reg),

    # media路由配置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

    url(r'^app01/',include(app01_urls))
]



#第二步，配置toolbar
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       url(r'^__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns






