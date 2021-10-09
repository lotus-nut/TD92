from django.contrib import admin

from app_notes.models import Note


# Register your models here.

@admin.register(Note)
class AppNoteAdmin(admin.ModelAdmin):
    pass
