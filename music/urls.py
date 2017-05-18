"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from scores.views import all_pieces, show_piece, index, composer_index, show_composer

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^(\w+)pieces_*(\w*).html', all_pieces),
    url(r'^pieces/(\w*).html$', show_piece),
    url(r'^index.html', index),
    url(r'^composers.html', composer_index),
    url(r'^composers/(\w*).html$', show_composer),
]
