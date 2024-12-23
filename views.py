from django.shortcuts import render,get_object_or_404
from .models import Doctor, Patient, Appointment

# Create your views here.


def patient_dashboard(request):
    patient = get_object_or_404(Patient, user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('date')
    context = {'patient': patient, 'appointments': appointments}
    return render(request, 'patient_dashboard.html', context)


def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date')
    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, 'doctor_dashboard.html', context)
