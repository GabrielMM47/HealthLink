{% load static %}

<!DOCTYPE html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Healthlink</title>

    <link rel="stylesheet" href="{% static 'css/register.css' %}">
  </head>

<form method="post">
    {% csrf_token %}

    <!-- Campo para selecionar o tipo de usuário -->
    <label for="usertype">Tipo de Usuário:</label>
    <select name="user_type" id="user_type" onchange="showProfileForm(this.value)">
        <option value="">Selecione...</option>
        <option value="patient">Paciente</option>
        <option value="doctor">Médico</option>
    </select>

    <!-- Exibe o Formulário com informações comuns aos médicos e pacientes -->
    {{ user_form.as_p }}

    <!-- Campos específicos para paciente ou médico -->
    <div id="patient_form" style="display:none;">
        {{ patient_profile_form.as_p }}
    </div>

    <div id="doctor_form" style="display:none;">
        {{ doctor_profile_form.as_p }}
    </div>

    <button type="submit">Registrar</button>
</form>

<script>
    function showProfileForm(value) {
        var patientForm = document.getElementById('patient_form');
        var doctorForm = document.getElementById('doctor_form');

        patientForm.style.display = 'none';
        doctorForm.style.display = 'none';

        if (value === 'patient') {
            patientForm.style.display = 'block';
        } else if (value === 'doctor') {
            doctorForm.style.display = 'block';
        }
    }
</script>

