from django.db import models

from utils.richtext.modelfields import RichTextField


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    is_show = models.BooleanField(default=False, verbose_name='是否展示')
    content = RichTextField(null=True, verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'app_notes_note'
        verbose_name = verbose_name_plural = '笔记'


class UploadFile(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')
    cls = models.CharField(max_length=10, verbose_name='类型')  # 对应 Request Content-Type
    size = models.PositiveIntegerField(verbose_name='大小')  # 单位：字节
    file = models.FileField()  # 文件
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'app_notes_upload_file'
        verbose_name = verbose_name_plural = '上传文件'
