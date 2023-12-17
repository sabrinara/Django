from django import forms

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