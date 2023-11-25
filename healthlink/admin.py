from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Case, When, Value, IntegerField
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
    fields = ['especialidade', 'crm', 'aceita_plano']

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'user_type_display')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nome_completo')
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
        inlines = []
        if hasattr(obj, 'patientprofile'):
            inlines.append(PatientProfileInline)
        if hasattr(obj, 'doctorprofile'):
            inlines.append(DoctorProfileInline)
        return [inline(self.model, self.admin_site) for inline in inlines]

    def get_queryset(self, request):
      # Obtém o QuerySet original do admin padrão
      qs = super().get_queryset(request)

      # Anota o QuerySet com um novo campo 'custom_order' que determina a ordem dos usuários
      # Superusuários vêm primeiro (0), seguidos de médicos (1), pacientes (2), e outros usuários (3)
      qs = qs.annotate(
          custom_order=Case(
              When(is_superuser=True, then=Value(0)),  # Superusuários
              When(doctorprofile__isnull=False, then=Value(1)),  # Médicos
              When(patientprofile__isnull=False, then=Value(2)),  # Pacientes
              default=Value(3),  # Todos os outros usuários
              output_field=IntegerField(),
          )
      ).order_by('custom_order', 'email')  # Ordena pelo campo 'custom_order', seguido de 'email'
      #print(qs.query)
      #print(list(qs))
      return qs

    def user_type_display(self, obj):
        if hasattr(obj, 'doctorprofile'):
            return 'Médico'
        elif hasattr(obj, 'patientprofile'):
            return 'Paciente'
        return 'Administrador'
    user_type_display.short_description = 'Tipo de Usuário'

admin.site.register(CustomUser, CustomUserAdmin)

