from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

# Classe UserManager Customizada
class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
      if not email:
          raise ValueError('O email é obrigatório')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, password=None, **extra_fields):
      extra_fields = {'is_staff': True, 'is_superuser': True}  # Redefinindo extra_fields

      if not email:
          raise ValueError('O email é obrigatório')

      return self.create_user(email=email, password=password, **extra_fields)

#Classe de customização do User padrão do django com informações comuns entre médicos e pacientes
class CustomUser(AbstractBaseUser, PermissionsMixin):
  SEXO = [('M', 'Masculino'), ('F', 'Feminino')]

  email = models.EmailField(unique=True)
  nome_completo = models.CharField(max_length=255, null=True, blank=True)
  data_nascimento = models.DateField(null=True, blank=True)
  cpf = models.CharField(max_length=14, null=True, blank=True)
  sexo = models.CharField(max_length=1, choices=SEXO, null=True, blank=True)
  telefone = models.CharField(max_length=15, null=True, blank=True)
  estado = models.CharField(max_length=2, null=True, blank=True)
  cidade = models.CharField(max_length=255, null=True, blank=True)
  bairro = models.CharField(max_length=255, null=True, blank=True)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'

  objects = CustomUserManager()

  def __str__(self):
      return self.email

#Classe para pacientes
class PatientProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patientprofile')
  plano_saude = models.CharField(max_length=3, choices=[('S', 'Sim'), ('N', 'Não')], null=True, blank=True)


#Classe para médicos
class DoctorProfile(models.Model): 
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctorprofile')
  especialidade = models.CharField(max_length=255, null=True, blank=True)
  crm = models.CharField(max_length=6, null=True, blank=True)
  aceita_plano = models.CharField(max_length=10, choices=[('S', 'Aceita'), ('N', 'Não aceita')], null=True, blank=True)