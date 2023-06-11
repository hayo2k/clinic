from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User


class SignUpUserForm(UserCreationForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Введите имя'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'sign__input', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpUserForm, self).save(commit=True)
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Введите имя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password__input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input__name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input__name', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input__item', 'readonly': True}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input__item'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'avatar__item'}), required=False)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone', 'image')
