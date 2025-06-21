from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),         # ✅ الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
]

# ✅ عرض الصور المرفوعة أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
