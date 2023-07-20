from django.shortcuts import render,redirect
from marpetapp.models import Mech_Cad,Elect_Cad,Civil_Cad,Train_Cad,Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):

    elect_unit = Elect_Cad.objects.get(id=5)
    mech_unit = Mech_Cad.objects.get(id=13)
    civil_unit = Civil_Cad.objects.get(id=16)
    train_unit = Train_Cad.objects.get(id=1)

    my_dict = {
          'mech_unit':mech_unit,
          'elect_unit':elect_unit,
          'civil_unit':civil_unit,
          'train_unit':train_unit,
    }

    return render(request,'marpetapp/index.html',context=my_dict)



def mech_list(request):
    mech = Mech_Cad.objects.all()

    my_dict = {
          'mech':mech,

        }
    return render(request,'marpetapp/list.html',context=my_dict)

def civil_list(request):
    civil = Civil_Cad.objects.all()

    my_dict = {
          'civil':civil,
        }
    return render(request,'marpetapp/list.html',context=my_dict)

def elect_list(request):
    elect = Elect_Cad.objects.all()

    my_dict = {
          'elect':elect,
        }
    return render(request,'marpetapp/list.html',context=my_dict)

def train_list(request):
    train = Train_Cad.objects.all()

    my_dict = {
          'train':train,
        }
    return render(request,'marpetapp/train_list.html',context=my_dict)


def mech_detail(request,id):
    mech = Mech_Cad.objects.get(id=id)
    my_dict = {
          'mech':mech,
            }
    return render(request,'marpetapp/detail.html',context=my_dict)

def civil_detail(request,id):
    civil = Civil_Cad.objects.get(id=id)

    my_dict = {
            'civil':civil,
        }
    return render(request,'marpetapp/detail.html',context=my_dict)

def elect_detail(request,id):
    elect = Elect_Cad.objects.get(id=id)

    my_dict = {
            'elect':elect,
        }
    return render(request,'marpetapp/detail.html',context=my_dict)

def about(request):
    return render(request,'marpetapp/about.html')

def contactpage(request):
    if request.method == "POST":
        contact = Contact()
        name =  request.POST.get('name')
        email =  request.POST.get('email')
        subject = request.POST.get('subject')
        message =  request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        send_mail(
        subject+' from '+name+' whose email is: '+email, #title
        message, #message
        'settings.EMAIL_HOST_USER',#sender
        ['peter_modo@yahoo.com',], #receiver
        fail_silently=False)
        
        return redirect('thankyou')

    return render(request,'marpetapp/contact.html')

def thankyoupage(request):
    return render(request,'marpetapp/thankyou.html')
