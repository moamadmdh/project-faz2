from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Patient, Secretary
from django.contrib import messages
from .forms import SignupForm

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print("username")
    print("password")
    try:
        patient = Patient.objects.get(username=username)
        if patient.password == password:
            # Login successful, redirect patient to their page
            return redirect('patient_page')
    except:
          return redirect('Wrong username or password')
        if user is not None:
            print("null")
            request.session['username'] = username
            return redirect('Welcome')
        else:
            return redirect('Wrong username or password')
    else:
        print("nothing")
        return redirect('Method not allowed')


    try: 
        secretary = Secretary.objects.get(username=username)
        if secretary.password == password:
            # Login successful, redirect secretary to their page
            return redirect('secretary_page')
    except Secretary.DoesNotExist:
        pass

    # Invalid login credentials
    messages.error(request, 'Invalid username or password')
    return redirect('login.html')


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
def add_clinic(request):
    if request.method == 'POST':
        clinic_id = request.POST['clinic_id']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        services = request.POST['services']
        try:
            user = ClinicModel.objects.get(email=email)
            return redirect('/login?msg=dup email')
        except:
            pass
        try:
            user = ClinicModel.objects.get(clinic_id=clinic_id)
            return redirect('2 clinic id')
        except:
            pass
        clinic = ClinicModel(clinic_id=clinic_id, email=email,name=name,address=address,phone_number=phone_number, services=services)
        clinic.save()
        return redirect('/panel/')
    else:
        return redirect('method not allowed')
def check_log_or_main(request):
    if 'username' in request.session:
        return redirect('/panel/')
    else:
        return redirect('Please login')

