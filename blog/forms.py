from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    email = forms.EmailField(label='ایمیل')
    user_role = forms.ChoiceField(choices=[('patient', 'بیمار'), ('secretary', 'منشی')], label='نقش کاربر')
    

class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
