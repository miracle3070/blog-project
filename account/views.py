from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.utils import IntegrityError

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user != None:
            auth.login(request, user)
            return redirect("index")
        else:
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, "login.html", {"error_message":error_message})
    else:
        return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST["username"]
            password = request.POST["password1"]
            # 아이디 생성 시도
            try:
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                return redirect("index")
            # 입력한 아이디가 이미 존재할 경우
            except IntegrityError:
                error_message = username + "은(는) 이미 존재하는 아이디입니다."
                return render(request, "signup.html", {"error_message":error_message})
        # 회원가입시 입력한 두 비밀번호가 일치하지 않을 경우
        else:
            error_message = "두 비밀번호가 서로 일치하지 않습니다"
            return render(request, "signup.html", {"error_message":error_message})

    # GET 방식으로 링크 접속시 회원가입 html 띄우기
    else:
        return render(request, "signup.html")

def logout(request):
    auth.logout(request)
    return redirect("index")