from django import forms
from . import models
from django.core.exceptions import ValidationError


class AddFotoForm(forms.ModelForm):
    class Meta:
        model = models.Foto
        fields = ['name', 'image', 'text']
        labels = {'name': 'Имя', 'image': 'Фотография', 'text': 'Описание'}
        widgets = {'image': forms.ClearableFileInput(), 'text': forms.Textarea(attrs={'cols': 80})}

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 0:
            raise ValidationError('Поле Имя не должно быть пустым.')
        else:
            return name

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) <= 5:
            raise ValidationError('Слишком мало символов.')
        else:
            return text
