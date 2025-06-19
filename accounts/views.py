from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# ✅ تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
            return redirect('home')  # يمكنك تغييره لاحقًا
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✅")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج.")
    return redirect('login')
