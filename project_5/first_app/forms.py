from django import forms
from django.core import validators

# widgets == field to html input 
class contactForm(forms.Form):
    name = forms.CharField(label = "Full Name :",help_text=" Total length must be within 70 characters", required=False, widget = forms.TextInput(attrs={ 'id':'text_area','class':'class1 class2','placeholder':'Enter your name'}))
    # file = forms.FileField() 
    email = forms.EmailField(label = "User Email")
    age  = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES = [ ('S', 'S'), ('M', 'M'), ('L', 'L')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [ ('B', 'Beef'), ('P', 'Pepperoni'), ('M', 'Mashroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name is too short')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com')
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name is too short')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com')


# def length_check(value):
#     if len(value) < 10:
#         raise forms.ValidationError('At least 10 characters')

# class StudentData(forms.Form):
#     name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Name is at least 10 characters")])
#     text = forms.CharField(widget=forms.TextInput, validators=[length_check])
#     email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter valid email")])
#     age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),
#                     validators.MinValueValidator(24, message="age must be at least 24")])
#     file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message="Only pdf and png files are allowed")])



class PasswordValidationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")

    
