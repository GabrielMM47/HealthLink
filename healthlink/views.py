from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserForm, PatientProfileForm, DoctorProfileForm
#from .models import CustomUser, PatientProfile, DoctorProfile


# Create your views here.

def home(request):
  return render(request, "home.html")

def sobre_nos(request):
  return render(request, "sobrenos.html")

def create_user(request):
  if request.method == 'POST':
      user_form = CustomUserForm(request.POST)
      patient_profile_form = PatientProfileForm()
      doctor_profile_form = DoctorProfileForm()
    
      if user_form.is_valid():
          new_user = user_form.save(commit=False)
          new_user.set_password(user_form.cleaned_data['senha'])
          new_user.save()  # Primeiro, salve o CustomUser

          user_type = request.POST.get('user_type')
          if user_type == 'patient':
              # Cria um PatientProfile para o usuário
              patient_profile_form = PatientProfileForm(request.POST)
              if patient_profile_form.is_valid():
                  patient_profile = patient_profile_form.save(commit=False)
                  patient_profile.user = new_user
                  patient_profile.save()
                  messages.success(request, 'Paciente registrado com sucesso!')
              else:
                  messages.error(request, 'Erro no formulário de perfil do paciente.')

          elif user_type == 'doctor':
              # Cria um DoctorProfile para o usuário
              doctor_profile_form = DoctorProfileForm(request.POST)
              if doctor_profile_form.is_valid():
                  doctor_profile = doctor_profile_form.save(commit=False)
                  doctor_profile.user = new_user
                  doctor_profile.save()
                  messages.success(request, 'Médico registrado com sucesso!')
              else:
                  messages.error(request, 'Erro no formulário de perfil do médico.')

          else:
              messages.error(request, 'Tipo de usuário desconhecido.')

          return redirect('home')  # Redirecionar para a home após o registro
      else:
          messages.error(request, 'Erro no formulário de usuário.')
  else:
      user_form = CustomUserForm()
      patient_profile_form = PatientProfileForm()
      doctor_profile_form = DoctorProfileForm()

  return render(request, 'register.html', {
      'user_form': user_form,
      'patient_profile_form': patient_profile_form,
      'doctor_profile_form': doctor_profile_form
  })

def login_user(request):
  if request.method == "POST":
      email = request.POST.get("email")
      password = request.POST.get("password")
      user = authenticate(request, email=email, password=password)

      if user is not None:
          login(request, user)
          return redirect("home")
      else:
          messages.error(request, "Usuário ou senha inválidos")

  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")