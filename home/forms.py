from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'نام',
                'required': True
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'ایمیل',
                'required': True
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'عنوان',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control text-right',
                'placeholder': 'پیام شما',
                'required': True

            })

        }



