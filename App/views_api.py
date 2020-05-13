import json

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
from .models import *
# Create your models here.

def getContext(status, message, data):
    context = {}
    context['status'] = status
    context['message'] = message
    context['data'] = data
    return context

# ------------------------------------------------------------------
# ClassName   : SignupAPI
# Description : 회원가입 API
# ------------------------------------------------------------------
def SignupAPI(request):

    type = request.POST.get('type', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    business_name = request.POST.get('business_name', None)
    business_number = request.POST.get('business_number', None)
    business_license = request.FILES.get('business_license', None)
    portfolio = request.FILES.get('portfolio', None)
    phone = request.POST.get('phone', None)

    hash_id = get_default_hash_id()
    try:
        User.objects.get(email=email)
        context = getContext('error', '이미 가입된 이메일입니다.', {})
        return HttpResponse(json.dumps(context), content_type="application/json")
    except:
        if type == 1:
            user = User.objects.create_user(
                username=hash_id, email=email, password=password, type=type, phone=phone
            )
        else:
            user = User.objects.create_user(
                username=hash_id, email=email, password=password, type=type,
                business_name=business_name, business_number=business_number,
                business_license=business_license, portfolio=portfolio, phone=phone
            )
        print(user)
        print(login(request, user))
        context = getContext('success', '성공', {})
        return HttpResponse(json.dumps(context), content_type="application/json")

# ------------------------------------------------------------------
# ClassName   : LoginAPI
# Description : 로그인 API
# ------------------------------------------------------------------
def LoginAPI(request):

    email = request.POST.get('email', None)
    password = request.POST.get('password', None)

    try:
        user = authenticate(email=email, password=password)
        login(request, user)
        context = getContext('success', '회원가입에 성공했습니다.', {})
        return HttpResponse(json.dumps(context), content_type="application/json")
    except:
        context = getContext('error', '아이디와 비밀번호가 일치하지 않습니다.', {})
        return HttpResponse(json.dumps(context), content_type="application/json")

# ------------------------------------------------------------------
# ClassName   : RequestAPI
# Description : 매칭 API
# ------------------------------------------------------------------
def RequestAPI(request):
    # biz_name
    # email
    # phone
    # product
    # budget
    # period
    # file
    company = request.POST.get('biz_name', None)
    email = request.POST.get('email', None)
    phone = request.POST.get('phone', None)
    product = request.POST.get('product', None)
    budget = request.POST.get('budget', None)
    period = request.POST.get('period', None)
    file = request.FILES.get('file', None)

    try:
        Request.objects.create(company=company, email=email, phone=phone, product=product, budget=budget, period=period, file=file)
        context = getContext('success', '매칭 문의가 성공적으로 등록되었습니다.', {})
        return HttpResponse(json.dumps(context), content_type="application/json")
    except:
        context = getContext('error', '의뢰 생성 실패', {})
        return HttpResponse(json.dumps(context), content_type="application/json")

# ------------------------------------------------------------------
# ClassName   : FindPasswordAPI
# Description : 매칭 API
# ------------------------------------------------------------------
def FindPasswordAPI(request):

    email = request.POST.get('email', None)
    user = User.objects.get(email=email)
    print(user)
    print(user.token)
    print(user.uid)

    send_mail(
        'Subject here',
        'Here is the message.',
        'wkddnjset@gamil.com',
        [email],
        fail_silently=False,
    )
    context = getContext('success', '메일보내기 성공.', {})
    return HttpResponse(json.dumps(context), content_type="application/json")
