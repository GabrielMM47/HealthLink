from django import forms
from .models import CustomUser, PatientProfile, DoctorProfile

class CustomUserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model = CustomUser
        fields = ['email', 'senha', 'nome_completo', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'estado', 'cidade', 'bairro']
        # Inclua todos os campos que você deseja que o usuário preencha no formulário

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['plano_saude']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['especialidade', 'CRM', 'aceita_plano']

