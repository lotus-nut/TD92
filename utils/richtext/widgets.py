from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe


class RichText(forms.Textarea):

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        final_attr = self.build_attrs(self.attrs, attrs)
        final_attr['name'] = name
        final_attr['id'] = 'td92-rich-text-id'

        return mark_safe(
            f'<textarea{flatatt(final_attr)}>{escape(value)}</textarea>\n'
        )

    @property
    def media(self):
        return forms.Media(
            css={'all': ['richtext/css/style.css']},
            js=(
                'tinymce/tinymce.min.js',
                'richtext/js/init.js',
            )
        )


class AdminRichTextWidget(RichText, AdminTextareaWidget):
    pass
