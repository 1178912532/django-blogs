from django.contrib import admin
from .models import Text
# Register your models here.
@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content', 'tags')