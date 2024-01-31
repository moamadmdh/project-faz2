from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Patient, Secretary
from django.contrib import messages
from .forms import SignupForm

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user_role = form.cleaned_data['user_role']
            
            if user_role == 'patient':
                new_patient = Patient(username=username, email=email, password=password, user_type=user_role)
                new_patient.save()
                return render(request, 'Bimar_dashboard.html')
            elif user_role == 'secretary':
                new_secretary = Secretary(username=username, email=email, password=password, user_type=user_role)
                new_secretary.save()
                destination_url = '/Monshi_dashboard/'

            return redirect(destination_url)
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
