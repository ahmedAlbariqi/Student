from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at')        # عرض هذه الحقول في القائمة
    readonly_fields = ('created_at',)                            # لا يمكن تعديل التاريخ
    search_fields = ('title', 'description')                     # بحث بالعنوان أو الوصف
    list_filter = ('instructor', 'created_at')                   # فلاتر جانبية
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'instructor')
        }),
        ('بيانات إضافية', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
