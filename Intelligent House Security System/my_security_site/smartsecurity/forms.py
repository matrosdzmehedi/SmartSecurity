from .models import UserRegistration
from django import forms


class UserForm(forms.ModelForm):
    class Meta(object):
        model = UserRegistration
        fields = ['name', 'age', 'flat_no', 'phone_no','profession', 'address']

        widgets = {

                'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),'age': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),'flat_no': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),'phone_no': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),'profession': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),


        }
