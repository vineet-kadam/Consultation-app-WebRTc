import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_consultation.settings')
django.setup()

from django.contrib.auth import get_user_model
from consultation.models import Meeting, Clinic

User = get_user_model()

def setup_data():
    # 1. Create Clinics
    print("Creating clinics...")
    clinics_data = [
        {"id": "CFC1", "name": "Centro Fertility Center 1"},
        {"id": "INOVA", "name": "INOVAVITA"},
    ]
    clinics = {}
    for c in clinics_data:
        clinic, _ = Clinic.objects.get_or_create(clinic_id=c["id"], defaults={"name": c["name"]})
        clinics[c["id"]] = clinic

    # 2. Create Patients
    print("Creating patients...")
    patients_data = [
        {"username": "CFC1-36", "first_name": "Gracy", "last_name": "Wade", "password": "CFC1-36"},
        {"username": "CFC1-164", "first_name": "Natalia", "last_name": "Byer", "password": "CFC1-164"},
        {"username": "CFC1-40", "first_name": "Lily", "last_name": "Martin", "password": "CFC1-40"},
        {"username": "CFC1-166", "first_name": "Nancy", "last_name": "Carter", "password": "CFC1-166"},
        {"username": "CFC1-162", "first_name": "Dyna", "last_name": "Flare", "password": "CFC1-162"},
    ]
    for u in patients_data:
        if not User.objects.filter(username=u["username"]).exists():
            user = User.objects.create_user(
                username=u["username"],
                first_name=u["first_name"],
                last_name=u["last_name"],
                password=u["password"],
                role="patient"
            )
    print("DONE: Users created with role = patient")

    # 3. Create Doctors
    print("Creating doctors...")
    doctors_data = [
        {"username": "daniel_lee", "first_name": "Daniel", "last_name": "Lee", "password": "daniel_lee"},
        {"username": "charles_fisher", "first_name": "Charles", "last_name": "Fisher", "password": "charles_fisher"},
        {"username": "david_kim", "first_name": "David", "last_name": "Kim", "password": "david_kim"},
        {"username": "henry_foster", "first_name": "Henry", "last_name": "Foster", "password": "henry_foster"},
        {"username": "amelia_scott", "first_name": "Amelia", "last_name": "Scott", "password": "amelia_scott"},
    ]
    for u in doctors_data:
        if not User.objects.filter(username=u["username"]).exists():
            user = User.objects.create_user(
                username=u["username"],
                first_name=u["first_name"],
                last_name=u["last_name"],
                password=u["password"],
                role="doctor",
                clinic=clinics["CFC1"] # Assign to first clinic by default
            )
    print("DONE: Doctors created successfully")

    # 4. Create Sample Meeting (Optional, for testing)
    print("Creating sample meeting...")
    pat = User.objects.get(username="CFC1-36")
    doc = User.objects.get(username="daniel_lee")
    Meeting.objects.get_or_create(
        room_id='TEST_ROOM_NEW',
        defaults={
            'patient': pat,
            'doctor': doc,
            'clinic': clinics["CFC1"],
            'scheduled_time': timezone.now() + timedelta(hours=1),
            'duration': 30,
            'status': 'scheduled',
            'appointment_type': 'consultation',
            'department': 'Fertility',
            'appointment_reason': 'Initial Visit'
        }
    )

    print("\nTest data setup complete.")
    print("Clinics: Centro Fertility Center 1, INOVAVITA")
    print(f"Sample Meeting ID: TEST_ROOM_NEW")

if __name__ == "__main__":
    setup_data()
