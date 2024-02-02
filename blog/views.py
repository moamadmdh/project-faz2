from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, ClinicModel
from django.contrib import messages
from .forms import SignupForm, LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                patient = User.objects.get(username=username)
                if patient.password == password:
                    # ورود موفقیت‌آمیز بیمار، هدایت به صفحه بیمار
                    return redirect('/Bimar_dashboard')
            except User.DoesNotExist:
                pass
            
            try:
                secretary = User.objects.get(username=username)
                if secretary.password == password:
                    # ورود موفقیت‌آمیز منشی، هدایت به صفحه منشی
                    return redirect('/Monshi_dashboard')
            except User.DoesNotExist:
                pass
            
            # اطلاعات ورود نامعتبر
            messages.error(request, 'نام کاربری یا رمز عبور نامعتبر است')
            
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user_role = form.cleaned_data['user_role']
            
            if user_role == 'بیمار':
                new_patient = User(username=username, email=email, password=password, user_type=user_role)
                new_patient.save()
                return render(request, 'Bimar_dashboard.html')
            elif user_role == 'منشی':
                new_secretary = User(username=username, email=email, password=password, user_type=user_role)
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
            return redirect('dup email')
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
        def Bimar_dashboard(request):
    return render(request, 'Bimar_dashboard.html')

def Monshi_dashboard(request):
    return render(request, 'Monshi_dashboard.html')
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')    

