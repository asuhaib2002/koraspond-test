from django import forms
from .models import Category


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Select an CSV File')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Select Category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']