from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.db.models import Case, When, Value
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, PatientProfile, DoctorProfile

class PatientProfileInline(admin.StackedInline):
  model = PatientProfile
  can_delete = False
  verbose_name_plural = 'Perfil do Paciente'
  fields = ['plano_saude']

class DoctorProfileInline(admin.StackedInline):
  model = DoctorProfile
  can_delete = False
  verbose_name_plural = 'Perfil do Médico'
  fields = ['especialidade', 'CRM', 'aceita_plano']

class CustomUserAdmin(UserAdmin):
  model = CustomUser
  inlines = []
  list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
  list_filter = ('is_active', 'is_staff', 'is_superuser')
  search_fields = ('email',)
  ordering = ('email',)

  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (_('Personal info'), {'fields': ('nome_completo', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'estado', 'cidade', 'bairro')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
      }),
  )

  def get_inline_instances(self, request, obj=None):
      if not obj:
          return []
      if hasattr(obj, 'patientprofile'):
          self.inlines = [PatientProfileInline]
      elif hasattr(obj, 'doctorprofile'):
          self.inlines = [DoctorProfileInline]
      return super(CustomUserAdmin, self).get_inline_instances(request, obj)

  def get_queryset(self, request):
    qs = super().get_queryset(request)
    qs = qs.annotate(
        custom_order=Case(
            When(is_superuser=True, then=Value(0)),
            default=Value(1),
            output_field=models.IntegerField(),
        )
    ).order_by('custom_order', 'email')
    return qs

# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
