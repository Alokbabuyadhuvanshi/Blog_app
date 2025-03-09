from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'image', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow-sm', 
                'placeholder': 'Enter blog title',
                'style': 'border-radius: 10px;'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control shadow-sm',
                'style': 'border-radius: 10px; padding: 10px;',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control shadow-sm', 
                'rows': 6, 
                'placeholder': 'Write your blog content...',
                'style': 'border-radius: 10px;'
            }),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control shadow-sm', 
        'placeholder': 'Enter your email',
        'style': 'border-radius: 10px;'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control shadow-sm', 
        'placeholder': 'Choose a username',
        'style': 'border-radius: 10px;'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control shadow-sm', 
        'placeholder': 'Enter password',
        'style': 'border-radius: 10px;'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control shadow-sm', 
        'placeholder': 'Confirm password',
        'style': 'border-radius: 10px;'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
