from django.urls import path
from .import views

urlpatterns= [
    path('appoint/', views.appoint,name='appoint'),
    path('consult/',views.consult, name= 'consult'),
    path('appointlist/', views.appointlist, name = 'appointlist'),
    path('appointdelete/<int:id>', views.appointdelete, name = 'appointdelete'),
    path('appointview/<int:id>', views.appointview, name ='appointview'),
    path('consultlist/', views.consultlist, name = 'consultlist'),
    path('consultdelete/<int:id>', views.consultdelete, name = 'consultdelete'),
    path('consultview/<int:id>', views.consultview, name ='consultview'),
    path('learn/', views.learn, name = 'learn'),
    path('civil/', views.civil, name = 'civil'),
    path('family/', views.family, name = 'family'),
    path('business/', views.business, name = 'business'),
    path('education/', views.education, name = 'education'),
    path('criminal/', views.criminal, name = 'criminal'),
    path('cyber/', views.cyber, name = 'cyber'),
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('team/', views.team, name = 'team'),
    path('service/', views.service, name = 'service'),
    path('contact/', views.contact, name = 'contact'),
    path('message/', views.message, name = 'message'),
    path('messagelist/' , views.messagelist, name='messagelist'),
    path('messagedelete/<int:id>' , views.messagedelete, name='messagedelete'),
    path('home/', views.home, name = 'home')







]