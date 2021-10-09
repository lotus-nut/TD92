from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe


class RichText(forms.Textarea):

    def __init__(self, attrs=None, rt_attrs=None):
        super().__init__(attrs)
        #
        rt_attrs = rt_attrs or {}
        self.rt_attrs = rt_attrs

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''

        final_attr = self.build_attrs(self.attrs, attrs)
        final_attr['name'] = name
        class_ = final_attr.get('class')
        final_attr['class'] = f'richtext {class_ if class_ else ""}'

        return mark_safe(
            f'<textarea{flatatt(final_attr)}>{escape(value)}</textarea>\n'
        )

    @property
    def media(self):
        return forms.Media()


class AdminRichTextWidget(RichText, AdminTextareaWidget):
    pass
