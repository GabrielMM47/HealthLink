from django.shortcuts import render, redirect
#from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserForm, PatientProfileForm, DoctorProfileForm
from django.contrib import messages
# Create your views here.

def home(request):
  return render(request, "home.html")



def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        user_type = request.POST.get('user_type')

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            if user_type == 'patient':
                profile_form = PatientProfileForm(request.POST, instance=new_user.patientprofile)
            elif user_type == 'doctor':
                profile_form = DoctorProfileForm(request.POST, instance=new_user.doctorprofile)
            else:
                messages.error(request, 'Tipo de usuário desconhecido.')
                return redirect('home')

            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Usuário criado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Erro no formulário de perfil. Por favor, corrija os erros abaixo.')
        else:
            messages.error(request, 'Erro no formulário de usuário. Por favor, corrija os erros abaixo.')

    else:
        user_form = CustomUserForm()
        profile_form = None

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})
