from django.contrib import admin

from app_notes.models import Note, UploadFile


# Register your models here.

@admin.register(Note, UploadFile)
class AppNoteAdmin(admin.ModelAdmin):
    pass
