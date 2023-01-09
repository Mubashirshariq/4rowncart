from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='Home'),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

