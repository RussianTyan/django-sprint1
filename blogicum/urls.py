from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),   # главная — blog:index
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
]

# в dev режимe: обслуживаем статику (не для продакшна)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
