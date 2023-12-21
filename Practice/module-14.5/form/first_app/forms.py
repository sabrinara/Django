import datetime
from django import forms

class contactForm(forms.Form):

    name = forms.CharField(label='Name')
    address = forms.CharField(
        label='Address',
        widget=forms.Textarea(attrs={'rows': 3}),
    )

    description = forms.CharField(widget=forms.Textarea, label='Description')
    
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label='Date of Birth'
        )
    
    email = forms.EmailField(label='Email')

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect,
        label='Gender'
    )

    payment = forms.DecimalField(
        max_digits=10,  
        decimal_places=2, 
        label='Payment'
    )

    job_choices = [
            ('teacher', 'Teacher'),
            ('driver', 'Driver'),
            ('corporate', 'Corporate'),
        ]
        
    job = forms.MultipleChoiceField(
            choices= job_choices,
            widget=forms.CheckboxSelectMultiple,
            label='Choose a job'
        )

    game_choices = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        
    ]
    
    sports = forms.MultipleChoiceField(
        choices=game_choices,
        label='Sports that you like most'
    )
    
 
    click = forms.BooleanField(
        required=False,
        initial=True, 
        label='Click here'
    )