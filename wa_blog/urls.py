
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include
from.import views
from blog import views as blog_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor/', include('autor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', blog_views.post_list, name="home"),
    path('about/', views.about),
    path('blog/', include('blog.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
