from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

class LendForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(is_lent=False))
    user = forms.CharField(max_length=100)

class ReturnForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(is_lent=True))
