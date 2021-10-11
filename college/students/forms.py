from django import forms
from django.forms import fields, models
from college import settings
from students.models import student
from django.core import validators



# class Records(forms.Form):
#     name = forms.CharField(max_length=200)
#     roll = forms.IntegerField()
#     dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enetr your email Again')
#     botCatcher = forms.CharField(required=False, widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])

#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         email2 = all_clean_data['verify_email']

#         if email != email2:
#             raise forms.ValidationError('Make sure email matches')

#     # def clean_botCatcher(self):
#     #     botCatcher = self.cleaned_data['botCatcher']
#     #     if len(botCatcher) > 0:
#     #         raise forms.ValidationError("CAUGHT A BOT")

#     #     return botCatcher

class userForm(forms.ModelForm):
    dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta():
        model = student
        fields = '__all__'