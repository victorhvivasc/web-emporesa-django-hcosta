from django.shortcuts import render, reverse, redirect
from django.core.mail import EmailMessage
from contact import forms

# Create your views here.
def contact(request):
    comunicado = forms.ContactForm()

    if request.method == 'POST':
        comunicado = forms.ContactForm(data=request.POST)
        if comunicado.is_valid():
            name= request.POST.get('name', '')
            mail= request.POST.get('mail', '')
            content = request.POST.get('content', '')
            email= EmailMessage(subject="Le escribieron de su emprendimiento",
                                body="De: {} <{}>\n\n Escribio: \n\n{}".format(name, mail, content), 
                                from_email=mail, 
                                to=["victor-7d2e03@inbox.mailtrap.io",],
                                reply_to=[mail,])
            try:
                email.send()
                return redirect(reverse('contacto')+'?ok')
            except:
                return redirect(reverse('contacto')+'?fail')                        

            

    return render(request, "contact/contact.html", {'correo':comunicado})

