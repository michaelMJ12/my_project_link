from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class  AdminUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
  
    class Meta:
       model = User
       fields = ('username', 'email', 'first_name', 'last_name','password1','password2')
       widgets = {
              'username' : forms.TextInput(attrs={'class':'form-control'}),
              'email' : forms.EmailInput(attrs={'class':'form-control'}),
              'first_name' : forms.TextInput(attrs={'class':'form-control'}),
              'last_name' : forms.TextInput(attrs={'class':'form-control'}),
              'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
              'password2' : forms.PasswordInput(attrs={'class':'form-control'}),

       }  


    def save(self, commit=True):
        user=super(AdminUserCreationForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]  
        if commit:
            user.save()
        return user     