from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),        # ✅ لتفعيل الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
]
