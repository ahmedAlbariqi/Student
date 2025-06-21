from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان الدورة"
    )
    description = models.TextField(
        verbose_name="وصف الدورة"
    )
    image = models.ImageField(
        upload_to='course_images/',
        null=True,
        blank=True,
        verbose_name="صورة الدورة"
    )
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="المدرّس"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دورة"
        verbose_name_plural = "الدورات"
