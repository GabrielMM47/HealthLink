from django import forms
from .models import CustomUser, PatientProfile, DoctorProfile

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'nome_completo', 'data_nascimento', 'cpf', 'sexo', 'telefone']
        # Inclua todos os campos que você deseja que o usuário preencha no formulário

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['endereco', 'plano_saude']
        # Assuma que 'endereco' é uma chave estrangeira para um modelo de Endereco
        # Você pode querer adicionar campos adicionais, dependendo dos detalhes do seu modelo

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['endereco_consultorio', 'CRM', 'metodo_pagamento']
        # Novamente, inclua todos os campos relevantes para o perfil do médico