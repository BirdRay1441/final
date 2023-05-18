from django import forms
from django.contrib.auth.models import User
from .models import Courses, UserProfileInfo

class CoursesForm(forms.ModelForm):
    class Meta():
        model = Courses
        fields = ('course_name', 'category', 'info', 'image', 'duration', 'price', 'priority')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        all_cleaned_data = super().clean()
        pswd = all_cleaned_data["password"]
        conf = all_cleaned_data["confirim_password"]

        if pswd != conf:
            raise forms.ValidationError("Password do not match!")

    class Meta():
        model = User
        fields = ('username', "email", 'password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('institution',)