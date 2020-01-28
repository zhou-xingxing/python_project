from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from typeidea.custom_site import custom_site
from .models import Tag, Post, Category
from .adminforms import PostAdminForm
from typeidea.base_admin import BaseOwnerAdmin


# Register your models here.
@admin.register(Category, site=custom_site)  # 类似绑定这个类的感觉
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'post_count', 'created_time')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')


# 自定义过滤器只展示当前用户创建的分类
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '自定义过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ('title', 'category', 'status', 'owner', 'created_time', 'operator')
    list_display_links = ()  # 不填默认是展示项第一个

    list_filter = ('category', 'tag')
    search_fields = ('title', 'category__name')

    actions_on_top = False
    actions_on_bottom = True

    # 编辑页面
    save_on_top = False

    fieldsets = (
        ('基础配置', {'description': '基础配置描述', 'fields': ('title', 'category', 'status')}),
        ('内容', {'fields': ('desc', 'content')}),
        ('额外信息', {'classes': ('collapse',), 'fields': ('tag',)}),
    )
    filter_horizontal = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')
