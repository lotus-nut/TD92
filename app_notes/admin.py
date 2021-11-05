from django.contrib import admin

from app_notes.models import Note, UploadFile


# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_show', 'updated_at', 'created_at')


@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('name',)
