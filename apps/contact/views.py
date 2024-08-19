from django.shortcuts import render, redirect

from .models import Contact


def contact(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        contact = Contact()

        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.subject = request.POST.get('subject')

        contact.save()

        return redirect(url)

    return render(request, "contact.html")
