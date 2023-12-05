from django import forms
from .models import CustomUser, PatientProfile, DoctorProfile

class CustomUserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))
  
    class Meta:
        model = CustomUser
      # Inclua todos os campos que você deseja que o usuário preencha no formulário
        fields = ['email', 'senha', 'nome_completo', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'estado', 'cidade', 'bairro']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input-field'}),
            'nome_completo': forms.TextInput(attrs={'class': 'input-field'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'input-field'}),
            'cpf': forms.TextInput(attrs={'class': 'input-field'}),
            'sexo': forms.TextInput(attrs={'class': 'input-field'}),
            'telefone': forms.TextInput(attrs={'class': 'input-field'}),
            'estado': forms.TextInput(attrs={'class': 'input-field'}),
            'cidade': forms.TextInput(attrs={'class': 'input-field'}),
            'bairro': forms.TextInput(attrs={'class': 'input-field'}),
            # Adicione classes para outros campos conforme necessário
        }
      
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

  