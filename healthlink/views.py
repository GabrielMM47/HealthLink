from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserForm, PatientProfileForm, DoctorProfileForm
from .models import CustomUser, PatientProfile, DoctorProfile


# Create your views here.

def home(request):
  return render(request, "home.html")


def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        user_type = request.POST.get('user_type')

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            password = request.POST.get('senha')
            if password:
                new_user.set_password(password)
                new_user.save()  # Salvar o usuário após definir a senha

                if user_type == 'patient':
                    profile_form = PatientProfileForm(request.POST)
                    if profile_form.is_valid():
                        profile = profile_form.save(commit=False)
                        profile.user = new_user
                        profile.save()
                        messages.success(request, 'Paciente registrado com sucesso!')
                    else:
                        messages.error(request, 'Erro no formulário de perfil do paciente.')

                elif user_type == 'doctor':
                    profile_form = DoctorProfileForm(request.POST)
                    if profile_form.is_valid():
                        profile = profile_form.save(commit=False)
                        profile.user = new_user
                        profile.save()
                        messages.success(request, 'Médico registrado com sucesso!')
                    else:
                        messages.error(request, 'Erro no formulário de perfil do médico.')

                return redirect('home')  # Redirecionar para a home após o sucesso
            else:
                messages.error(request, 'A senha é obrigatória.')
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




