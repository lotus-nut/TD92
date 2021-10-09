from django.db import models

from .widgets import AdminRichTextWidget


class RichTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs.update(widget=AdminRichTextWidget)

        return super().formfield(**kwargs)
