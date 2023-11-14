from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.

#Classe Endereço
class Endereco(models.Model):
  estado = models.CharField(max_length=255)
  cidade = models.CharField(max_length=255)
  bairro = models.CharField(max_length=255)
  rua = models.CharField(max_length=255)
  numero = models.CharField(max_length=10)
  complemento = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
      return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade} - {self.estado}'


#Classe Plano de Saúde
class PlanoSaude(models.Model):
  nome = models.CharField(max_length=255)

  def __str__(self):
      return self.nome

#Classe decustomização do User padrão do django com informações comuns entre médicos e pacientes
class CustomUser(AbstractBaseUser):
  #email = models.EmailField(unique=True) -> Acho que o User padrão do django já pede email
  nome_completo = models.CharField(max_length=255)
  data_nascimento = models.DateField()
  sexo = models.CharField(max_length=9, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
  telefone = models.CharField(max_length=15)

  is_active = models.BooleanField(default=True) #Não sei o motivo
  is_staff = models.BooleanField(default=False) #Não sei o motivo
  
  #objects = UserManager() #Não sei o porque disso
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['nome_completo', 'data_nascimento', 'telefone']

  def __str__(self):
    return self.email


#Classe para pacientes
class PatientProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
  plano_saude = models.ForeignKey(PlanoSaude, on_delete=models.SET_NULL, blank=True, null=True)


#Classe para médicos
class DoctorProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  endereco_consultorio = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  CRM = models.IntegerField(max_legnth=6)