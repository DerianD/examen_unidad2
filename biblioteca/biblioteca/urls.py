"""biblioteca URL Configuration

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

from libros import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^libros/$', views.lista_libros2, name='libros'),
    url(r'^detalle/(?P<object_id>\d+)/$', views.detalle_libro, name='detalle'),
    url(r'^detalle/(?P<slug>[\w-]+)/$', views.detalle_s, name='detalle_s'),
    url(r'^detalle/(?P<slug>[\w-]+)/$', views.detalle_slug, name='detalle_slug'),
    url(r'^detalle/(?P<object_id>\d+)/editar/$', views.actualizar, name='actualizar'),
    url(r'^crear_libro/$', views.agregar_libro, name='nuevo_libro'),
]

