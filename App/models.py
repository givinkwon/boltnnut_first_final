import os, datetime, uuid

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


from hashids import Hashids


# Create your models here.
def get_default_hash_id():
    hashids = Hashids(salt=settings.SECRET_KEY, min_length=6)
    try:
        user_id = User.objects.latest('id').id + 1
    except:
        user_id = 1
    return hashids.encode(user_id)

def business_license_update_filename(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now()
    path = "business_license/" + str(now.year) + "/" + str(now.month) + "/" + str(now.day)
    format = uuid.uuid4().hex + "_" + instance.username + "_business" + "." + ext
    return os.path.join(path, format)

def partner_update_filename(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now()
    path = "partner/" + str(now.year) + "/" + str(now.month) + "/" + str(now.day)
    format = uuid.uuid4().hex + "_partner" + "." + ext
    return os.path.join(path, format)

def portfolio_update_filename(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now()
    path = "portfolio/" + str(now.year) + "/" + str(now.month) + "/" + str(now.day)
    format = uuid.uuid4().hex + "_portfolio" + "." + ext
    return os.path.join(path, format)

def user_portfolio_update_filename(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now()
    path = "user_portfolio/" + str(now.year) + "/" + str(now.month) + "/" + str(now.day)
    format = uuid.uuid4().hex + "_portfolio" + "." + ext
    return os.path.join(path, format)

def request_update_filename(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now()
    path = "request/" + str(now.year) + "/" + str(now.month) + "/" + str(now.day)
    format = uuid.uuid4().hex + "_request" + "." + ext
    return os.path.join(path, format)

# ------------------------------------------------------------------
# Model   : User
# Description : 회원 모델
# ------------------------------------------------------------------
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    first_name = None
    last_name = None
    username = None

    CLIENT = 1
    PARTNER = 2
    TYPE = (
        (CLIENT, '클라이언트'),
        (PARTNER, '파트너'),
    )

    email = models.EmailField('이메일', unique=True)
    username = models.CharField('유저명', max_length=50, default=get_default_hash_id)
    type = models.PositiveSmallIntegerField('유저타입', choices=TYPE, default=1)

    business_name = models.CharField('사업자명', max_length=50, blank=True, null=True)
    business_number = models.CharField('사업자번호', max_length=50, blank=True, null=True)
    business_license = models.FileField('사업자등록증', upload_to=business_license_update_filename, blank=True, null=True)
    portfolio = models.FileField('포트폴리오', upload_to=user_portfolio_update_filename, blank=True, null=True)

    phone = models.CharField('휴대폰 번호', max_length=32, blank=True, null=True)

    REQUIRED_FIELDS = ['username']
    class Meta:
        verbose_name = '      회원'
        verbose_name_plural = '      회원'

    def __str__(self):
        return str(self.email)

# ------------------------------------------------------------------
# Model   : Industry
# Description : 업종 모델
# ------------------------------------------------------------------
class Industry(models.Model):

    name = models.CharField('업종명', max_length=256)

    class Meta:
        verbose_name = '  업종'
        verbose_name_plural = '  업종'

    def __str__(self):
        return str(self.name)

# ------------------------------------------------------------------
# Model   : Partner
# Description : 파트너 모델
# ------------------------------------------------------------------
class Partner(models.Model):

    name = models.CharField('업체명', max_length=256)
    thumbnail = models.ImageField('썸네일', upload_to=partner_update_filename)
    phone = models.CharField('전화번호', max_length=256, blank=True)
    industry = models.ManyToManyField(Industry, verbose_name='업종')
    address = models.CharField('주소', max_length=256, blank=True)
    career = models.IntegerField('경력', default=0)
    products = models.TextField('진행한 제품', blank=True)
    special = models.TextField('특화분야', blank=True)
    info = models.TextField('회사소개', blank=True)
    history = models.TextField('주요이력', blank=True)
    is_main = models.BooleanField('메인노출여부', default=False)
    is_partner = models.BooleanField('파트너여부', default=False)
    created_at = models.DateTimeField('등록일자', auto_now_add=True)

    class Meta:
        verbose_name = '  파트너'
        verbose_name_plural = '  파트너'

    def __str__(self):
        return str(self.name) + " 파트너"


# ------------------------------------------------------------------
# Model   : Portfolio
# Description : 포트폴리오 모델
# ------------------------------------------------------------------
class Portfolio(models.Model):

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="파트너")
    img = models.ImageField('이미지', upload_to=portfolio_update_filename)
    created_at = models.DateTimeField('등록일자', auto_now_add=True)

    class Meta:
        verbose_name = '     포트폴리오'
        verbose_name_plural = '     포트폴리오'

    def __str__(self):
        return str(self.partner.name) + " 포트폴리오"


# ------------------------------------------------------------------
# Model   : Project
# Description : 프로젝트 모델
# ------------------------------------------------------------------
class Project(models.Model):

    title = models.CharField('제목', max_length=40)
    content = RichTextUploadingField('내용')
    is_main = models.BooleanField('메인노출여부', default=False)
    budget = models.CharField('희망 예산', max_length=256, blank=True, null=True)
    started_at = models.DateTimeField('작업시작일시')
    ended_at = models.DateTimeField('작업종료일시')
    created_at = models.DateTimeField('등록일자')

    class Meta:
        verbose_name = '   프로젝트'
        verbose_name_plural = '   프로젝트'

    def __str__(self):
        return str(self.title) + " : 프로젝트"


# ------------------------------------------------------------------
# Model   : Bbs
# Description : 게시판 모델
# ------------------------------------------------------------------
class Bbs(models.Model):

    title = models.CharField('제목', max_length=40)
    content = RichTextUploadingField('내용')
    is_top = models.BooleanField('상단고정여부', default=False)
    created_at = models.DateTimeField('등록일자', auto_now_add=True)

    class Meta:
        verbose_name = '   게시글'
        verbose_name_plural = '   게시글'

    def __str__(self):
        return str(self.star) + " : 게시글"

# ------------------------------------------------------------------
# Model   : product
# Description : 요청 모델
# ------------------------------------------------------------------
class Request(models.Model):

    company = models.CharField('회사명', max_length=256, blank=True, null=True)
    phone = models.CharField('전화번호', max_length=256, blank=True, null=True)
    email = models.CharField('이메일', max_length=256, blank=True, null=True)
    product = models.CharField('제품', max_length=256, blank=True, null=True)
    budget = models.CharField('희망 예산', max_length=256, blank=True, null=True)
    period = models.CharField('희망 기간', max_length=256, blank=True, null=True)
    file = models.FileField('포트폴리오', upload_to=request_update_filename, blank=True, null=True)
    created_at = models.DateTimeField('등록일자', auto_now_add=True)

    class Meta:
        verbose_name = '     요청된 의뢰'
        verbose_name_plural = '     요청된 의뢰'

    def __str__(self):
        return str(self.company) + " : 요청"

