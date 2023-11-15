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
  
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  
  objects = CustomUserManager()

  def __str__(self):
      return self.email

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

#Classe para pacientes
class PatientProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
  plano_saude = models.CharField(max_length=255)


#Classe para médicos
class DoctorProfile(models.Model): 
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  endereco_consultorio = models.OneToOneField(Endereco, on_delete=models.CASCADE)
  CRM = models.CharField(max_length=6)
  metodo_pagamento = models.ManyToManyField('MetodoPagamento')
  
  
#Classe para método de pagamento
class MetodoPagamento(models.Model):
  nome = models.CharField(max_length=50)
  descricao = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
      return self.nome