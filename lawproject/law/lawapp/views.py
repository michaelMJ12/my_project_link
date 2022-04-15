from django.shortcuts import render,redirect
from .forms import AppointmentForm
from .forms import ConsultantForm
from .models import Appointment
from .models import Consultant
from .models import Message




def appoint(request):
    appointform = AppointmentForm()
    if request.method == "POST":
       appointform = AppointmentForm(request.POST) 
       if appointform.is_valid():
           appointform.save()
           return redirect('index')
       else:
           return redirect('appoint')     
    return render(request , 'appoint.html' ,{ 'appointform': appointform  })



def consult(request):
    consultform = ConsultantForm()
    if request.method == "POST":
       consultform = ConsultantForm(request.POST ) 
       if consultform.is_valid():
           consultform.save()
           return redirect('index')
       else:
           return redirect('consult')     
    return render(request , 'consult.html' ,{ 'consultform': consultform  })  




def appointlist(request):
    appointmentlists = Appointment.objects.all()
    return render(request, 'appointlist.html', {'appointmentlists' : appointmentlists})



def appointdelete(request, id):
    appointmentdelete = Appointment.objects.get(id=id)
    appointmentdelete.delete()
    return redirect('appointlist')



def appointview(request, id):
    appointmentview = Appointment.objects.get(id=id)
    return render(request, 'appointview.html', {'appointmentview' : appointmentview})



def consultlist(request):
    consultantlists = Consultant.objects.all()
    return render(request, 'consultlist.html', {'consultantlists' : consultantlists})



def consultdelete(request, id):
    consultantdelete = Consultant.objects.get(id=id)
    consultantdelete.delete()
    return redirect('consultlist')


def consultview(request, id):
    consultantview = Consultant.objects.get(id=id)
    return render(request, 'consultview.html', {'consultantview' : consultantview})


def learn(request):
    return render(request , 'learn.html' )    

def civil(request):
    return render(request , 'civil.html' )        


def family(request):
    return render(request , 'family.html' )    

def business(request):
    return render(request , 'business.html' )    

def education(request):
    return render(request , 'education.html' )    


def criminal(request):
    return render(request , 'criminal.html' )        

def cyber(request):
    return render(request , 'cyber.html' )      


def index(request):
    return render(request, 'index.html')      

def about(request):
    return render(request, 'about.html')          

def blog(request):
    return render(request, 'blog.html')              

def portfolio(request):
    return render(request, 'portfolio.html')                  

def team(request):
    return render(request, 'team.html')                      

def service(request):
    return render(request, 'service.html')                          

def contact(request):
    return render(request, 'contact.html')                              


def message(request):  
    if request.method == 'POST':
        nameM = request.POST['name']  
        emailM = request.POST['email']  
        phoneM = request.POST['phone']  
        messageM = request.POST['message'] 

        form = Message(nameM=nameM, emailM=emailM, phoneM=phoneM, messagesM=messageM ) 
        form.save()
        return redirect('contact')
    return render(request, 'contact.html', {'form':form})    


def messagelist(request):
    messagelists = Message.objects.all()
    return render(request, 'messagelist.html', {'messagelists' : messagelists})



def messagedelete(request, id):
    messagedelete = Message.objects.get(id=id)
    messagedelete.delete()
    return redirect('messagelist')



def home(request):
    return render(request, 'home.html')          

