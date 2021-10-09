from django.db import models

from utils.richtext.modelfields import RichTextField


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    is_show = models.BooleanField(default=False, verbose_name='是否展示')
    # content = models.TextField(null=True, verbose_name='内容')
    content = RichTextField(null=True, verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'app_notes_note'
        verbose_name = verbose_name_plural = '笔记'
