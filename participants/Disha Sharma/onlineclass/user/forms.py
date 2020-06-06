from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField


from user.models import User,Subject

class StudentSignUpForm(UserCreationForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name','college','degree','major','image','lang_approved','phone','year','courses']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    courses = forms.ModelMultipleChoiceField(
    queryset=Subject.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name','college','courses']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff=True
        user.is_teacher = True
        if commit:
            user.save()
        return user