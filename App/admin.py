from django.contrib import admin
from .models import *
# Register your models here.

from django.forms import TextInput, Textarea
from django.db import models

class PortfolioInline(admin.StackedInline):
    model = Portfolio
    can_delete = True
    extra = 0
    max_num = 15

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'type', 'phone']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'email', 'phone', 'product', 'budget', 'period','created_at', 'file']

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    inlines = [PortfolioInline]
    list_display = ['id', 'name', 'address', 'career', 'created_at', 'is_partner']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']

# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ['id', 'partner', 'img', 'created_at']

@admin.register(Bbs)
class Bbsdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'is_top', 'created_at']
