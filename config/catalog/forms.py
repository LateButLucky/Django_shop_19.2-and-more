from django import forms
from .models import Product, Contact, BlogPost, Version
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(f'Запрещенное слово в названии: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(f'Запрещенное слово в описании: {word}')
        return description


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview_image', 'published']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_current'].widget.attrs.update({'class': 'form-check-input'})
