from django.contrib import admin

from blog.models import Group, Article


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status', 'group', 'visit', 'show_slider')
    list_editable = ('status', 'show_slider')
