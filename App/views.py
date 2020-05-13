from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.db.models import Q
from django.core.paginator import Paginator

from .models import *
# Create your views here.

# ------------------------------------------------------------------
# PageName   : MainPage
# Description : 메인페이지
# ------------------------------------------------------------------
def MainPage(request):
    partners = Partner.objects.filter(is_main=True)
    #projects = Project.objects.filter(is_main=True)
    projects = Project.objects.all().order_by('-id')
    if len(projects) > 10:
        projects = projects[0:10]
    return render(request, 'Main/MainPage.html', {
        'title': '볼트앤너트 | 메인',
        'partners': partners,
        'projects': projects,
    })

# ------------------------------------------------------------------
# PageName   : LoginPage
# Description : 로그인 페이지
# ------------------------------------------------------------------
def LoginPage(request):
    return render(request, 'Account/LoginPage.html', {
        'title': '볼트앤너트 | 로그인',
    })

# ------------------------------------------------------------------
# PageName   : LogoutPage
# Description : 로그아웃 페이지
# ------------------------------------------------------------------
def LogoutPage(request):
    logout(request)
    return redirect('/')

# ------------------------------------------------------------------
# PageName   : SignupPage
# Description : 회원가입페이지
# ------------------------------------------------------------------
def SignupPage(request):
    return render(request, 'Account/SignupPage.html', {
        'title': '볼트앤너트 | 회원가입',
    })

# ------------------------------------------------------------------
# PageName   : SignupSuccessPage
# Description : 회원가입 성공 페이지
# ------------------------------------------------------------------
def SignupSuccessPage(request):
    return render(request, 'Account/SignupSuccessPage.html', {
        'title': '볼트앤너트 | 회원가입 성공',
    })

# ------------------------------------------------------------------
# PageName   : FindPWPage
# Description : 비밀번호 재설정 페이지
# ------------------------------------------------------------------
def FindPWPage(request):
    return render(request, 'Account/FindPWPage.html', {
        'title': '볼트앤너트 | 비밀번호 재설정',
    })


# ------------------------------------------------------------------
# PageName   : ExpertPage
# Description : 전문가 찾기 페이지
# ------------------------------------------------------------------
def PartnerPage(request):
    partners = Partner.objects.all()
    return render(request, 'Partner/PartnerPage.html', {
        'title': '볼트앤너트 | 전문가 찾기',
        'partners': partners
    })

# ------------------------------------------------------------------
# PageName   : ExpertDetailPage
# Description : 전문가 찾기 페이지
# ------------------------------------------------------------------
def PartnerDetailPage(request, id):
    partner = Partner.objects.get(id=id)
    portfolios = Portfolio.objects.filter(partner=partner)
    return render(request, 'PartnerDetail/PartnerDetailPage.html', {
        'title': '볼트앤너트 | 전문가 상세',
        'partner': partner,
        'portfolios': portfolios,
    })


# ------------------------------------------------------------------
# PageName   : ProjectPage
# Description : 프로젝트 페이지
# ------------------------------------------------------------------
def ProjectPage(request):
    q = request.GET.get('q')
    if q:
        projects = Project.objects.filter(Q(title__contains=q) | Q(content__contains=q)).order_by('-id')
    else:
        projects = Project.objects.all().order_by('-id')
    return render(request, 'Project/ProjectPage.html', {
        'title': '볼트앤너트 | 프로젝트 목록',
        'projects': projects,
    })

# ------------------------------------------------------------------
# PageName   : ProjectDetailPage
# Description : 프로젝트 페이지
# ------------------------------------------------------------------
def ProjectDetailPage(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'ProjectDetail/ProjectDetailPage.html', {
        'title': '볼트앤너트 | 프로젝트 상',
        'project': project,
    })


# ------------------------------------------------------------------
# PageName   : ConsultingPage
# Description : 뉴스 상세페이지
# ------------------------------------------------------------------
def ConsultingPage(request):

    return render(request, 'Consulting/ConsultingPage.html', {
        'title': '볼트앤너트 | 양산 컨설팅',
    })


# ------------------------------------------------------------------
# PageName   : RequestPage
# Description : 제작의뢰 페이지
# ------------------------------------------------------------------
def RequestPage(request):
    return render(request, 'Request/RequestPage.html', {
        'title': '볼트앤너트 | 시제품 제작의뢰',
    })

# ------------------------------------------------------------------
# PageName   : ProductPage
# Description : 시제품의뢰 페이지
# ------------------------------------------------------------------
def ProductPage(request):
    return render(request, 'product/ProductPage.html', {
        'title': '볼트앤너트 | 시제품 제작의뢰',
    })

# ------------------------------------------------------------------
# PageName   : TermsPage
# Description : 이용약관 페이지
# ------------------------------------------------------------------
def TermsPage(request):
    return render(request, 'Info/TermsPage.html', {
        'title': '볼트앤너트 | 이용약관',
    })

# ------------------------------------------------------------------
# PageName   : PersonalPage
# Description : 이용약관 페이지
# ------------------------------------------------------------------
def PersonalPage(request):
    return render(request, 'Info/PersonalPage.html', {
        'title': '볼트앤너트 | 개인정보취급방안',
    })
