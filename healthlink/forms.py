from django import forms
from .models import CustomUser, PatientProfile, DoctorProfile

class CustomUserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model = CustomUser
      # Inclua todos os campos que você deseja que o usuário preencha no formulário
        fields = ['email', 'senha', 'nome_completo', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'estado', 'cidade', 'bairro']
        
        labels = {
            'email': 'E-mail',
            'nome_completo': 'Nome Completo',
            'data_nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
            'sexo': 'Sexo',
            'telefone': 'Telefone',
            'estado': 'Estado',
            'cidade': 'Cidade',
            'bairro': 'Bairro',
        }

    def __init__(self, *args, **kwargs):
      super(CustomUserForm, self).__init__(*args, **kwargs)
      for fieldname, field in self.fields.items():
          field.label = self.Meta.labels.get(fieldname, fieldname)



class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['plano_saude']
        labels = {'plano_saude': 'Possui Plano de Saúde?'}


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['especialidade', 'crm', 'aceita_plano']
        labels = {
            'especialidade': 'Especialidade Médica',
            'crm': 'CRM Médico',
            'aceita_plano': 'Aceita Plano de Saúde?',
        }

  