from django import forms
from pasta_family import models
from pasta_family.models import CooperationForm, CooperationType, Product
import re
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError
from django.forms.widgets import TextInput


def transliterate(text):
    pieces = str(re.sub('[\W]+', ' ', text)).lower().split(' ')
    result = []

    for piece in pieces:
        try:
            result.append(translit(piece, reversed=True))
        except LanguageDetectionError:
            result.append(piece)
    return '-'.join([r for r in result if r])


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'


class ProductForm(forms.ModelForm):
    def clean_slug(self):
        return transliterate(self.cleaned_data['name_ru'])

    class Meta:
        model = models.Product
        fields = '__all__'


class ProductGroupForm(forms.ModelForm):
    def clean_slug(self):
        return transliterate(self.cleaned_data['name_ru'])

    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductWeightForm(forms.ModelForm):
    class Meta:
        model = models.ProductWeight
        fields = '__all__'


class CooperationTypeForm(forms.ModelForm):
    class Meta:
        model = models.CooperationType
        fields = '__all__'


class CooperationFormForm(forms.ModelForm):
    class Meta:
        model = models.CooperationForm
        fields = '__all__'


class CooperationForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(attrs={'placeholder': 'ПІБ/Назва компанії'}), min_length=4, max_length=150)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email'}), max_length=254)
    phone = forms.CharField(widget=TextInput(attrs={'placeholder': 'Номер телефона'}), min_length=6)
    type = forms.ModelChoiceField(queryset=CooperationType.objects.all(), empty_label='Тип')
    form = forms.ModelChoiceField(queryset=CooperationForm.objects.all(), empty_label='Организационно-правовая форма')

    class Meta:
        model = models.Cooperation
        fields = '__all__'


class ProductTypeForm(forms.ModelForm):
    def clean_slug(self):
        return transliterate(self.cleaned_data['name_ru'])

    class Meta:
        model = models.ProductType
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    name = forms.CharField(min_length=4, max_length=150)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select the product')

    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewNewForm(forms.ModelForm):
    name = forms.CharField(min_length=4, max_length=150)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select the product')

    class Meta:
        model = models.ReviewNew
        fields = '__all__'


class PriceForm(forms.ModelForm):
    class Meta:
        model = models.Price
        fields = '__all__'


class MainPhotoForm(forms.ModelForm):
    class Meta:
        model = models.MainPhoto
        fields = '__all__'


class AboutCompanyPhotoForm(forms.ModelForm):
    class Meta:
        model = models.MainPhoto
        fields = '__all__'
