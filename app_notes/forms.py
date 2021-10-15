from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(max_length=64)
