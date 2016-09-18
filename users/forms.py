from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        	'first_name', 'last_name', 'email', 'birthday', 'random_number'
        ]
        widgets = {
        	'first_name': forms.TextInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder":  "Enter your first name",

        		}),
        	'last_name': forms.TextInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder":  "Enter your last name",
        		}),
        	'email': forms.EmailInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder":  "Enter your email",
        		}),
        	'birthday': forms.DateInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder":  "Enter your birthday",
        		}),
        	'random_number': forms.NumberInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder":  "Enter your number",
                    "max":          100,
                    "min":          1
        		}),
        }
