from django.shortcuts import render,redirect
from .forms import AdminUserCreationForm

# Create your views here.



def register(request):
    form = AdminUserCreationForm()
    if request.method == "POST":
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointlist')
    return render(request, 'registration/register.html', {'form':form })        

