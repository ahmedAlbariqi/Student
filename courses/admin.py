from django.contrib import admin
from django.utils.html import format_html
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at', 'image_tag')  # ✅ عرض الصورة المصغّرة
    readonly_fields = ('created_at', 'image_tag')                      # ✅ إظهار الصورة في التفاصيل فقط
    search_fields = ('title', 'description')
    list_filter = ('instructor', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'image_tag', 'instructor')
        }),
        ('بيانات إضافية', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="120" style="border-radius:8px;" />', obj.image.url)
        return "لا توجد صورة"
    image_tag.short_description = 'صورة الدورة'
