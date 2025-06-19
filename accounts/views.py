from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# ✅ النموذج المخصّص لتسجيل المستخدم
from .forms import CustomUserCreationForm


# ────────────────────────────────────────────────
# تسجيل مستخدم جديد
# ────────────────────────────────────────────────
def register_view(request):
    """
    إنشاء حساب جديد باستخدام النموذج المخصّص CustomUserCreationForm.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول مباشرة بعد إنشاء الحساب
            messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
            return redirect('home')
        else:
            # عرض الأخطاء بشكل رسائل
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


# ────────────────────────────────────────────────
# تسجيل الدخول
# ────────────────────────────────────────────────
def login_view(request):
    """
    تسجيل دخول المستخدم باستخدام النموذج الجاهز AuthenticationForm.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✅")
            return redirect('home')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# ────────────────────────────────────────────────
# تسجيل الخروج
# ────────────────────────────────────────────────
def logout_view(request):
    """
    تسجيل خروج المستخدم ثم إعادة توجيهه إلى صفحة تسجيل الدخول.
    """
    logout(request)
    messages.info(request, "تم تسجيل الخروج.")
    return redirect('login')


# ────────────────────────────────────────────────
# الصفحة الرئيسية
# ────────────────────────────────────────────────
def home(request):
    """
    عرض الصفحة الرئيسية للمنصة.
    """
    return render(request, 'home.html')  # ✅ تأكد أن الملف موجود داخل templates/home.html