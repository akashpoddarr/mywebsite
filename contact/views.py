from django.shortcuts import render, redirect
from .models import contact




def Contact(request):
    if request.method=="POST":
        index = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        desc = request.POST.get('desc')
        contact.name= name
        contact.email=email
        contact.num=num
        contact.desc=desc
        contact.save()
        return redirect('/')

    return render(request, 'contact.html')