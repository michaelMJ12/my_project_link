from django.contrib import admin
from .models import Appointment
from .models import  Consultant
from .models import  Message

class AppointmentAdmin(admin.ModelAdmin):
    list_displace = ['name','phone','email','messages','address']

admin.site.register(Appointment, AppointmentAdmin)    





class ConsultantAdmin(admin.ModelAdmin):
    list_displace = ['nameC','phoneC','emailC','messagesC','addressC']

admin.site.register(Consultant, ConsultantAdmin)    


class MessageAdmin(admin.ModelAdmin):
    list_displace = ['nameM','phoneM','emailM','messagesM']

admin.site.register(Message, MessageAdmin)    
