from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# counter
entry_count = 0

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def contact(request):
    global entry_count

    if request.method == 'POST':
        entry_count += 1

        name = request.POST.get('name')
        email = request.POST.get('email')
        job = request.POST.get('job')
        resume = request.FILES.get('resume')

        subject = f"New Job Application - Entry {entry_count}"

        message = f"""
        Entry No: {entry_count}

        Name: {name}
        Email: {email}
        Job Applied: {job}
        """

        mail = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['gcc@globalcarrierinfo.in'],
        )

        if resume:
            mail.attach(resume.name, resume.read(), resume.content_type)

        mail.send()

        messages.success(request, "Your application submitted successfully!")

        return redirect('home')

    return redirect('home')