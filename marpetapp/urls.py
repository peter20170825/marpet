from django.urls import path
from . import views


urlpatterns = [

    path('mechlist/',views.mech_list,name='mechlist'),
    path('civillist/',views.civil_list,name='civillist'),
    path('electlist/',views.elect_list,name='electlist'),
    path('trainlist/',views.train_list,name='trainlist'),
    path('mechlist/mechdetail/<int:id>',views.mech_detail,name='mechdetail'),
    path('civillist/civildetail/<int:id>',views.civil_detail,name='civildetail'),
    path('electlist/electdetail/<int:id>',views.elect_detail,name='electdetail'),
    path('about/',views.about,name='about'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('contactpage/thankyou/',views.thankyoupage,name='thankyou'),
]
