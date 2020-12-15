from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member,Video,Product,RealEstate,Legal
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name=self.cleaned_data['first_name']
    #     user.last_name=self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
        
    #     if commit:
    #         user.save()

    #     return user

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields = ["name", "videofile"]
        

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ["name", "description", "price", "image"]


class RealEstateForm(forms.ModelForm):
    class Meta:
        model= RealEstate
        fields = ["name", "description", "price", "image"]

class LegalForm(forms.ModelForm):
    class Meta:
        model= Legal
        fields = ["description"]

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Member
        fields = [
            'image'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)
    #     f = self.fields.get('member_permissions', None)
    #     if f is not None:
    #         f.queryset = f.queryset.select_related('content_type')