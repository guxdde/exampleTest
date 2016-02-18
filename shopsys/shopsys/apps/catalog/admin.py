# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Product
from .forms import ProductAdminForm

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """docstring for CategoryAdmin"""
    list_display = ('name', 'create_at', 'update_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',
                     'meta_keywords', 'meta_description']
    exclude = ('create_at', 'update_at',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin"""
    form = ProductAdminForm

    list_display = ("name", "price", "old_price", "create_at", "update_at",)
    list_display_links = ("name",)
    list_per_page = 50
    ordering = ["-create_at"]
    search_fields = ['name', 'description',
                     'meta_keywords', 'meta_description']
    exclude = ('create_at', 'update_at',)
    prepopulated_fields = {'slug': ('name',)}
