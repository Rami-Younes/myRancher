
from django import forms
from django.contrib.auth.models import User # i use it to can change first name and last name cos django creates them
from . import models
from .models import UserProfile
from django.shortcuts import render, redirect

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
             'bio', 'slug','join_date'
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User   #meaning ,what do u want to change
        fields = [
            'username', 'first_name', 'last_name', 'email'

        ]


# class ProfileForm2(forms.ModelForm):
#     class Meta:
#         model = models.SaveChkbox
#         fields = [
#              'names'
#         ]



class CommunitySelectForm(forms.Form):

    communities = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),widget=forms.CheckboxSelectMultiple, required=True)










