from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import ClientRegisterForm, DoctorRegisterForm
from .models import CustomUser, Client, Doctor, Message
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def home(request):
    if request.user.is_authenticated:
        # If user is logged in, redirect to the appropriate dashboard or show minimal options
        if request.user.is_client:
            return redirect('client_dashboard')
        elif request.user.is_doctor:
            return redirect('doctor_dashboard')
    
    return render(request, 'core/home.html')

def client_register(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_client = True
            user.save()
            Client.objects.create(user=user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = ClientRegisterForm()
    return render(request, 'core/client_register.html', {'form': form})

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            Doctor.objects.create(
                user=user,
                specialization=form.cleaned_data.get('specialization'),
                license_number=form.cleaned_data.get('license_number')
            )
            return redirect('login')  # Redirect to login page after registration
    else:
        form = DoctorRegisterForm()
    return render(request, 'core/doctor_register.html', {'form': form})

@login_required
def client_dashboard(request):
    if request.user.is_client:
        # Fetch messages where the client is the sender
        messages = Message.objects.filter(client=request.user.client)
        
        # Optional: Fetch doctors for additional context
        doctors = Doctor.objects.all()
        
        messages = messages.order_by('timestamp')  # Ensure messages are in the correct order
        
        return render(request, 'core/client_dashboard.html', {'doctors': doctors, 'messages': messages})
    else:
        return redirect('home')



@login_required
def doctor_dashboard(request):
    if request.user.is_doctor:
        # Fetch messages where the doctor is the recipient
        messages = Message.objects.filter(doctor=request.user.doctor)
        
        # Optional: Fetch clients for additional context
        clients = Client.objects.all()
        
        messages = messages.order_by('timestamp')  # Ensure messages are in the correct order
        
        return render(request, 'core/doctor_dashboard.html', {'messages': messages, 'clients': clients})
    else:
        return redirect('home')




@login_required
def send_message(request):
    if request.method == 'POST' and request.user.is_client:
        message_content = request.POST.get('message')
        doctor = Doctor.objects.filter(user__username='doctor9').first()
        if doctor:
            Message.objects.create(client=request.user.client, doctor=doctor, content=message_content)
        return redirect('client_dashboard')
    return redirect('client_dashboard')


@login_required
def send_response(request):
    if request.method == 'POST' and request.user.is_doctor:
        response_content = request.POST.get('response')
        client = Client.objects.filter(user__username='patient9').first()
        if client:
            Message.objects.create(client=client, doctor=request.user.doctor, content=response_content)
        return redirect('doctor_dashboard')
    return redirect('doctor_dashboard')







def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_client:
                    return redirect('client_dashboard')
                elif user.is_doctor:
                    return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')




def csrf_failure(request, reason=""):
    return render(request, 'core/csrf_failure.html', {'reason': reason})