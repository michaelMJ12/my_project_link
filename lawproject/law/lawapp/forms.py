from django import forms
from .models import Appointment
from .models import  Consultant





class   AppointmentForm(forms.ModelForm):
        class Meta:
            model =  Appointment
            fields = ('name','phone','email','messages','address')
            widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control'}),
                    'phone': forms.NumberInput(attrs={'class':'form-control'}),
                    'email': forms.EmailInput(attrs={'class':'form-control'}),
                    'messages':forms.Textarea(attrs={'class':'form-control'}),
                    'address':forms.TextInput(attrs={'class':'form-control'}),
        }




class   ConsultantForm(forms.ModelForm):
        class Meta:
            model = Consultant
            fields = ('nameC','phoneC','emailC','messagesC','addressC')
            widgets = {
                    'nameC': forms.TextInput(attrs={'class':'form-control'}),
                    'phoneC': forms.NumberInput(attrs={'class':'form-control'}),
                    'emailC': forms.EmailInput(attrs={'class':'form-control'}),
                    'messagesC':forms.Textarea(attrs={'class':'form-control'}),
                    'addressC':forms.TextInput(attrs={'class':'form-control'}),
        }        
