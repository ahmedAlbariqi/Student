from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/courses.html', {'courses': courses})
