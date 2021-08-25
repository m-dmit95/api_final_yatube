from django.contrib import admin

from .models import Follow


# Register your models here.
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user',)
    empty_value_display = '-пусто-'
