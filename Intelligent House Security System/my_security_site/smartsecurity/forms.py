from .models import UserInfo
from django import forms


class UserInfoForm(forms.ModelForm):
    class Meta(object):
        model = UserInfo
        fields = ['name', 'age', 'flat_no', 'phone_no',
                  'profession', 'address', 'marig_status']

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'age': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'flat_no': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'phone_no': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'profession': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),


        }
