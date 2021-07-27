from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import About,Contact,Skills,Resume,Certificate,Project,Education
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mess=request.POST['message']
        msg = f"{name.capitalize()},"
        send_mail(
            msg,
            f"{subject}, \n {mess}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        messages.info(request, name.capitalize() + ', ' + "Your message has been sent to 'Mukesh Gupta'. Thank you!!")
        return redirect('home')
    else:
        if not None:
            about=About.objects.all()
            cont=Contact.objects.all()
            skill=Skills.objects.all()
            resume=Resume.objects.all()
            cert=Certificate.objects.all()
            Proj=Project.objects.all()
            edu=Education.objects.all()
        else:
            None
        context={
            'about':about,
            'skills':skill,
            'resume':resume,
            'edu':edu,
            'cert':cert,
            'Proj':Proj,
            'contact':cont

        }
        return render(request,'index.html',context=context)

def project_view(request,pk):
    proj=Project.objects.get(pk=pk)
    context={'project':proj}
    return render(request,'project-details.html',context=context)
