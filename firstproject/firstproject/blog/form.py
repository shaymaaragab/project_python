from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=False)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']
        #exclude = ['full_name']

    def clean_email(self):
            email = self.cleaned_data.get('email')
            email_base,provider = email.split("@")
            domain , extenstion  = provider.split('.')
           # if not domain == "erbil":
             #   raise forms.ValidationError("please make sure using erbil")
          #  if not extenstion == "gov":
              #  raise forms.ValidationError("please enter .gov domain")
            return email
    def clean_fullname(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name