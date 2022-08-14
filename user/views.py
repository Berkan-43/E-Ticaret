from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş Başarılı.")
            return redirect('home')
        else:
             messages.error(request, "Kullanıcı Adı veya Şifre Hatalı..")
    return render(request, 'login.html')


def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Bu Kullanıcı Adı Zaten Var..")
                return render(request, "register.html")
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, "E-mail Adresi Kullanılıyor.")
                    return render(request, "register.html")
                else:
                   user = User.objects.create_user(username=username, email=email, password=password)
                   user.save()
                   messages.success(request, "Üyeliğiniz Eklendi.")
                   return redirect('login')
        else:
            messages.error(request, "Parolalar Eşleşmiyor.")
    return render(request, 'register.html')


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı.')
    return redirect('home')

